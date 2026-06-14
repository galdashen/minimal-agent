import os, subprocess, json
from openai import OpenAI

tools = [
    {
        "type": "function",
        "function": {
            "name": "run_command",
            "description": "在用户的电脑上运行 pwsh 命令并获取输出",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "需要运行的 pwsh 命令",
                    },
                },
                "required": ["command"],
            },
        },
    }
]


def run_command(command):
    result = subprocess.run(
        ["pwsh", "-Command", command],
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return result.stdout


client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com"
)

messages = [
    {
        "role": "system",
        "content": "你可以在用户的电脑上运行 pwsh 命令来帮用户完成代码任务",
    }
]

while True:
    user_input = input("User: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    messages.append({"role": "user", "content": user_input})
    while True:
        response = (
            client.chat.completions.create(
                model="deepseek-v4-pro",
                messages=messages,
                tools=tools,
            )
            .choices[0]
            .message
        )
        reasoning_content = response.reasoning_content
        content = response.content
        tool_calls = response.tool_calls
        if reasoning_content:
            print("Thought:", reasoning_content)
        if content:
            print("Response:", content)
        messages.append(response)
        if response.tool_calls is None:
            break
        for tool in response.tool_calls:
            print(f"Command: {json.loads(tool.function.arguments)['command']}")
            tool_result = run_command(**json.loads(tool.function.arguments))
            print(f"Output: {tool_result}")
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool.id,
                    "content": tool_result,
                }
            )
