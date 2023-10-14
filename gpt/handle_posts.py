# -*- coding: utf-8 -*-

import openai

context = """по тексту определи к какой категории отнести этот текст, ответом должен быть номер соответствующей категории
Категории:
1) Cтажировки <предложение от одной отдельной компании>
2) Олимпиады
3) Форумы <подборка IT форумов, ярмарок вакансий, предложения от многих компаний>"""

prompt = "bla bla bla"

openai.api_key = "sk-***"

categories = {"1": "Стажировки",
              "2": "Олимпиады",
              "3": "Форумы",
              "0": "Unknown"}

def ans_by_request(prompt: str) -> str:
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": prompt}
        ],
        temperature=0.1
    )
    return completion.choices[0].message.content

def find_out_key_ctgr(prompt: str) -> str:
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": prompt}
        ],
        temperature=0.1
    )
    key = completion.choices[0].message.content[0]
    if key not in categories.keys():
        key = "0"
    return key

def key_ctgr_by_ans(answer: str):
    key = answer[0]
    if key not in categories.keys():
        key = "0"
    return key

def category_by_request(prompt: str) -> str:
    key = find_out_key_ctgr(prompt)
    return categories[key]


print(category_by_request(prompt))
