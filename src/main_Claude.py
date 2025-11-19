import os
import random
import subprocess
import anthropic

import prompt_reader as pr
from llm_executer import chat, RECORD_PATH, save_chat, execute_historical_chat

ITERATION = 10

#P_MODEL = "gpt-4o"
#MODEL = "gpt-4o"
#MODEL = "gpt-4o-mini"

# claude-3-5-sonnet-latest
# claude-3-5-haiku-latest
# claude-3-haiku-20240307

CLIENT = anthropic.Anthropic()

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CURRENT_DIR)
SWIM_DIR = BASE_DIR + '/swim/swim'
SWIM_COMMAND = "./script.zsh"
SWIM_RESULT_DIR = BASE_DIR + '/swim/results'

def knowledger():
    knowledge0_input, knowledge0_response = chat(CLIENT, MODEL, pr.knoledge01())        # response format: txt
    knowledge1_input, knowledge1_response = chat(CLIENT, MODEL, pr.knoledge02())        # response format: txt
    # knowledge2_response: cpp -> executable
    knowledge2_input, knowledge2_response = chat(CLIENT, P_MODEL, pr.knoledge03())      # initial create, response format: cpp
    return [[knowledge0_input, knowledge0_response],[knowledge1_input, knowledge1_response],[knowledge2_input, knowledge2_response]]

def analyzer(now_utility, csvpath, code):
    chat(CLIENT, MODEL, pr.analyzer01(now_utility, csvpath))    # select area of result, response format: txt
    analyze2_input, analyze2_response = chat(CLIENT, MODEL, pr.analyzer02(code))                # identify the biggest problem, response format: txt
    chat(CLIENT, MODEL, pr.analyzer03(code))                # select area of code, response format: txt
    analyze4_input, analyze4_response = chat(CLIENT, MODEL, pr.analyzer04())                        # explain improvement plan, response format: txt
    # return [[analyze1_input, analyze1_response],[analyze2_input, analyze2_response],[analyze3_input, analyze3_response],[analyze4_input, analyze4_response]]
    return [[],[analyze2_input, analyze2_response],[],[analyze4_input, analyze4_response]]

def planner(arg: int, historicnum: int, problems_plans, max_utility, max_code):
    if arg == 0:
        plan0_input, plan0_response = chat(CLIENT, P_MODEL, pr.planner00(problems_plans))         # create plan initially, response format: cpp
        return [[plan0_input, plan0_response]]
    elif arg < 5:                                                               # create plan, response format: txt, cpp
        planbase_input, planbase_response = chat(CLIENT, P_MODEL, pr.planner_base(historicnum, problems_plans, max_utility, max_code))
        plan_input, plan_response = chat(CLIENT, P_MODEL, pr.planner(arg))
        return [[plan_input, plan_response], [planbase_input, planbase_response]]
    
    else:
        print("Invalid argumernt!")
        exit(1)

def extract_code(text, flag: bool):
    start = text.find("```cpp")
    end = text.find("```", start + 6)  # 開始位置の後で終了位置を探す

    if start != -1 and end != -1:
        return text[start + 6:end].strip()  # コード部分を抽出して前後の空白を削除
    else:
        print("invalid output")
        print()
        chat(CLIENT, MODEL, "You must output only the program this time, never any non-program content. Output only the program again.")

        if flag:
            extract_code(text, False)
        else:
            print("終了")
            exit(1)



def delete_chatlog():
    with open(RECORD_PATH, 'w') as f:
        f.write('')

max_utility = -10000000
utilities = []

knowledge = knowledger()
knowledge_prompt = knowledge[0] + knowledge[1]
simulation_program_dict = knowledge[2][1]

analyze_result = []
for i in range(ITERATION):
    simulation_program = extract_code(simulation_program_dict['content'], True)
    #print(simulation_program)
    with open(SWIM_DIR + "/src/managers/adaptation/MyAdaptationManager.cc", 'w') as f:
        f.write(simulation_program)
    # execute swim simulation
    result = subprocess.run(['zsh', SWIM_COMMAND], cwd=SWIM_DIR, capture_output=True, text=True)
    if result.returncode != 0:
        print("swim unsucccess!")
        print("stdout:",result.stdout)
        print("stderr:",result.stderr)
        utilities.append("ERROR")
        error_chat = chat(CLIENT, P_MODEL, pr.error(simulation_program, result.stderr))
        simulation_program_dict = error_chat[1]
        continue

    # get utility
    with open(SWIM_RESULT_DIR + "/totalUtility.txt", 'r') as f:
        utility = float(f.read())

    utilities.append(utility)
    print("Iteration:", i, ", Utility", utility)



    # update max_utility, max_code
    if utility > max_utility:
        max_utility = utility
        max_code = simulation_program
        print("Update Max Utility！！")

    if i == ITERATION-1:
        break

    # get csvpath
    csvpath = SWIM_RESULT_DIR + "/simResult.txt"




    analyze = analyzer(utility, csvpath, simulation_program)
    problems = analyze[1][1]       # identify the biggest problem
    plans = analyze[3][1]       # explain improvement plan
    analyze_result.insert(0, [problems, plans])

    arg = random.randint(1, 4) if i > 4 else i
    historicnum = min(i, 3)
    plan = planner(arg, historicnum, analyze_result, max_utility, max_code)
    simulation_program_dict = plan[0][1]
    delete_chatlog()
    temp = knowledge_prompt[:]
    if arg != 0:  # plan's arg != 0
        save_chat(temp, plan[1][0])
        save_chat(execute_historical_chat(), plan[1][1])
        save_chat(execute_historical_chat(), plan[0][0])
        save_chat(execute_historical_chat(), plan[0][1])
    else:               # plan's arg == 0
        save_chat(temp, plan[0][0])
        save_chat(execute_historical_chat(), plan[0][1])

print("end", utilities)