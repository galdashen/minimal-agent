# minimal-agent

## 快速启动

1. 配置好 API 客户端
2. 配置好 Shell，可以把 Shell 加到环境变量路径里，我这里用的是 pwsh，也可以自己改代码换成别的，最好把字符编码设置为 utf-8
3. 然后直接运行 `ten_line_version.py` 或 `tool_call_version.py` 就可以了

## ten_line_version.py

仅用十行代码实现的一个 coding agent，是根据 [mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent) 的教程 [minimal-agent-tutorial](https://minimal-agent.com/) 写的，我把教程里的代码压成了十行，还把主循环的逻辑修改了，让用户能进行多轮对话

## tool_call_version.py

工具调用版本。`ten_line_version.py` 没有用 `tool_call` 执行命令，而是只接受文字回复，通过提示词规定从文字回复里直接下指令的格式，然后从文字回复里提取指令。此版本 `tool_call_version.py` 则是直接用 `tool_call` 来执行命令

## 效果演示

![效果演示](./demo.png)
