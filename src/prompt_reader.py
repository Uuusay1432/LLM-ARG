# 1, 2, 3, 4, 5, 6, 7, 10P0(only here), 4,5,6,7, 9, 10P1or2or3or4, (4,5,6,7), 9, 10...

import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CURRENT_DIR)
SWIM_PROMPT_DIR = BASE_DIR + "/prompt/swim/en/"

PROMPT_DIR = SWIM_PROMPT_DIR

def txt_to_template(txt: str, targets: list) -> str:
    i = 0
    n = len(txt)
    result = []

    while i < n:
        if txt[i] == '{':  # 開始の '{' を検出
            end_idx = txt.find('}', i + 1)  # 対応する '}' を探す
            if end_idx != -1:
                key = txt[i + 1:end_idx]  # '{' と '}' の間の文字列を抽出
                if key in targets:
                    result.append(f"{{{key}}}")  # プレースホルダーとして残す
                else:
                    result.append('{{')  # エスケープ処理
                    result.append(key)
                    result.append('}}')
                i = end_idx + 1  # '}' の次に進む
            else:
                raise ValueError("Unmatched '{' in template string.")
        elif txt[i] == '}':  # 単独の '}' はエスケープ
            result.append('}}')
            i += 1
        else:  # 通常の文字
            result.append(txt[i])
            i += 1
    return ''.join(result)

# task descriptions, adaptation goal, variable information
def knoledge01():
    f = open(PROMPT_DIR + "prompt_01en.txt", 'r')
    input = f.read()
    return input

# variable information - related programs
def knoledge02():
    f = open(PROMPT_DIR + "prompt_02en.txt", 'r')
    input = f.read()
    return input

# task descriptions, adaptation goal, variable information (restriction)
def knoledge03():
    f = open(PROMPT_DIR + "prompt_03en.txt", 'r')
    input = f.read()
    return input

def analyzer01(now_utility, csvpath):
    f = open(PROMPT_DIR + "prompt_04en_A1.txt", 'r')
    template = txt_to_template(f.read(), ['NOW_UTILITY', 'CSV'])
    # read CSV file
    r = open(csvpath, 'r')
    csv = r.read()
    input = template.format(NOW_UTILITY = now_utility, CSV = csv)
    return input

def analyzer02(code):
    f = open(PROMPT_DIR + "prompt_05en_A2.txt", 'r')
    template = f.read()
    input = template.format(PROGRAM = code)
    return input

def analyzer03(code):
    f = open(PROMPT_DIR + "prompt_06en_A3.txt", 'r')
    template = txt_to_template(f.read(), ['PROGRAM'])

    input = template.format(PROGRAM = code)
    return input

def analyzer04():
    f = open(PROMPT_DIR + "prompt_07en_A4.txt", 'r')
    input = f.read()
    return input

def planner00(problems_plans):
    f = open(PROMPT_DIR + "prompt_10en_P0.txt", 'r')
    template = f.read()
    input = template.format(PROBLEMS_PLANS = problems_plans[0])
    return input

# 実装要検討
def planner_base(historicnum: int, problems_plans, max_utility: float, max_code):
    # histricnum: 過去何個のデータ取得するか
    # problems: list of problem
    # plan: list of plan
    f = open(PROMPT_DIR + "prompt_09en_P.txt", 'r')
    template = f.read()
    input = template.format(NUM = historicnum, PROBLEMS_PLANS = problems_plans[:min(historicnum+1, 3)], MAX_UTILITY = max_utility, PROGRAM = max_code)
    return input

def planner(arg: int):
    if arg == 1:
        f = open(PROMPT_DIR + "prompt_10en_P1.txt", 'r')
    elif arg == 2:
        f = open(PROMPT_DIR + "prompt_10en_P2.txt", 'r')
    elif arg == 3:
        f = open(PROMPT_DIR + "prompt_10en_P3.txt", 'r')
    elif arg == 4:
        f = open(PROMPT_DIR + "prompt_10en_P4.txt", 'r')
    else:
        print("Invalid argument!!")
        exit(1)
    input = f.read()
    return input

def error(code, stderr):
    f = open(PROMPT_DIR + "prompt_99en_error.txt", 'r')
    template = txt_to_template(f.read(), ['CODE', 'STDERR'])

    input = template.format(CODE = code, STDERR = stderr)
    return input