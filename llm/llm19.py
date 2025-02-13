import ollama
import time
from redlines import Redlines
from IPython.display import display, Markdown

# curl http://localhost:11434/api/chat -d '{
#   "model": "llama3.2",
#   "messages": [
#     { "role": "user", "content": "why is the sky blue?" }
#   ]
# }'
def ollama_image_caption(msg):
    client = ollama.Client(host='http://localhost:11434')
    # 设置提示语
    prompt_v = msg or {"role":"","content":"hello world"}
    response = client.chat(
        model='llama3.2', messages=prompt_v)
    
    return response

# 调用


messages =  [  
{'role':'system', 'content':'你是个友好的聊天机器人。'},
{'role':'user', 'content':'Hi, 我是Isa'},
{'role':'assistant', 'content': "Hi Isa! 很高兴认识你。今天有什么可以帮到你的吗?"},
{'role':'user', 'content':'是的，你可以提醒我, 我的名字是什么?'}  ]

caption = ollama_image_caption(messages)

print(caption['message'])

'''

{'role': 'assistant', 'content': '好嘞！你的名字叫 Isabella，大家都习惯地称你为 Isa。'}

'''