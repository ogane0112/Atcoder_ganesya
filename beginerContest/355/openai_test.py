from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "あなたはプログラムのエキスパートかつアルゴリズムデータ構造のエキスパートです。"},
    {"role": "user", "content": f"連立方程式の解き方を教えてください(pythonでの)"}
  ]
)

print(completion.choices[0].message)

