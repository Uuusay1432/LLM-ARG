import os
import json

from openai import OpenAI

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
RECORD_PATH = CURRENT_DIR + "/../log/record.txt"
LOG_PATH = CURRENT_DIR + "/../log/log.txt"

def execute_historical_chat():
    with open(RECORD_PATH, 'rb') as f:
        temp  = f.read()
        try:
            historic_messages = json.loads(temp)
        except json.JSONDecodeError:
            return []
    return historic_messages    # return List of dict

def save_chat(messages: list, response: dict):
    # 新しいメッセージを追加し、チャット履歴をファイルに保存
    messages.append(response)
    result = messages
    with open(RECORD_PATH, "wb") as f:
        f.write(json.dumps(messages, indent = 4).encode('utf-8'))
    with open(LOG_PATH, "ab") as f:
        f.write(json.dumps(messages, indent = 4).encode('utf-8'))
    return result

def start_chat(client, model, input):                  # return str
    completion = client.chat.completions.create(
        model = model,
        messages = input
    )
    response = completion.choices[0].message.content
    return response

def create_dict(arg, message):
    if arg == 'prompt':
        return {"role": "user", "content": message}
    elif arg == 'response':
        return {"role": "assistant", "content": message}
    else:
        print("1st Arg has Error!!!!")
        exit(1)


def chat(client, model, prompt):
    #save_chat([], {"role": "user", "content": 'message'})
    # record prompt as 'input'
    input = execute_historical_chat()
    prompt_dict = create_dict('prompt', prompt)
    input.append(prompt_dict)
    response = start_chat(client, model, input)
    # response = 'No Girl Friends'                                # TEST！！！！！！！！！！！！！！！！！！
    response_dict = create_dict('response', response)
    output = save_chat(input, response_dict)
    #print(output)
    return prompt_dict, response_dict

# Test
#CLIENT = OpenAI()
#chat(CLIENT, "gpt-3.5-turbo-0125", "I am Yusei")
#Achat(CLIENT, "gpt-3.5-turbo-0125", "Pleae tell me my name's pronounce")