import requests
from bs4 import BeautifulSoup
import html2text
import subprocess
import re
import json
from openai import OpenAI
def remove_blank_lines(text):
    lines = text.splitlines()
    non_blank_lines = [line for line in lines if line.strip() != ""]
    return "\n".join(non_blank_lines)

def extract_english_text(text):
    # Split the text by lines
    lines = text.split('\n')
    english = []
    flag = False
    for i in lines:
      if flag:
        english.append(i)
      #かならずこの文言から問題が始まっているためこれを基準にしている
      if i == "###  Problem Statement":
        english.append(i)
        flag = True

    # Join the English lines back into a single string
    return '\n'.join(english)

# URLの指定
url = "https://atcoder.jp/contests/abc356/tasks/abc356_d"

# HTTPリクエストの送信
response = requests.get(url)
response.raise_for_status()  # リクエストが成功したか確認
result = ""

# BeautifulSoupによるHTML解析
soup = BeautifulSoup(response.text, 'html.parser')

# headerタグで囲まれている部分を抽出
header = soup.find_all("div" ,class_="part")

# 各part要素の内容を表示
for part in header:
    result += part.prettify()

#
markdown = html2text.html2text(result)
result = remove_blank_lines(markdown)
print(result)
# client = OpenAI()

# completion = client.chat.completions.create(
#   model="gpt-4o",
#   messages=[
#     {"role": "system", "content": "あなたはプログラムのエキスパートかつアルゴリズムデータ構造のエキスパートです。"},
#     {"role": "user", "content": f"{result}\nplease output python"}
#   ]
# )
# response = completion.choices[0].message
# print(response)
# a = response.split("\n")
# output = []
# for i in range(len(a)):
#   if i == 0 or i == len(a)-1:
#     continue
#   else:
#     output.append(a[i])
# print('\n'.join(output))
# with open('main.py', 'w') as file:
#     file.write('\n'.join(output))