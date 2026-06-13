import os,re,subprocess;from openai import OpenAI
c=OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"),base_url="https://api.deepseek.com")
m=[{"role":"system","content":"你可以用```pwsh-action\n命令\n```在用户的电脑上执行pwsh命令，用户会把结果返回给你"}]
while 1:
 if(u:=input("User: ")).lower() in ["exit","quit"]:break
 m.append({"role":"user","content":u})
 while 1:
  r=c.chat.completions.create(model="deepseek-v4-pro",messages=m).choices[0].message.content;print("Agent:",r);m.append({"role":"assistant","content":r})
  if not (a:=[p.strip() for p in re.findall(r"```pwsh-action\s*\n(.*?)\n```",r,re.DOTALL)]):break
  for x in a:o=subprocess.run(["pwsh","-C",x],text=True,encoding="utf-8",errors="replace",stdout=subprocess.PIPE,stderr=subprocess.STDOUT).stdout;print("Output:",o);m.append({"role":"user","content":o})
