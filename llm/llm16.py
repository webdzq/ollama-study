import ollama
import time
from redlines import Redlines
from IPython.display import display, Markdown

def ollama_image_caption(msg):
    client = ollama.Client(host='http://localhost:11434')
    # 设置提示语
    prompt_v = msg or "hello world"
    response = client.generate(
        model='llava', prompt=prompt_v)
    return response

# 调用
# 指令内容，使用 ``` 来分隔指令和待总结的内容
# 拼写及语法纠正
text = f"""
Got this for my daughter for her birthday cuz she keeps taking \
mine from my room.  Yes, adults also like pandas too.  She takes \
it everywhere with her, and it's super soft and cute.  One of the \
ears is a bit lower than the other, and I don't think that was \
designed to be asymmetrical. It's a bit small for what I paid for it \
though. I think there might be other options that are bigger for \
the same price.  It arrived a day earlier than expected, so I got \
to play with it myself before I gave it to my daughter.
"""


# Prompt ：基于说明书创建营销描述
prompt = f"校对并更正以下商品评论：```{text}```"

response = ollama_image_caption(prompt)

diff = Redlines(text,response['response'])
# print(diff.output_markdown)
display(Markdown(diff.output_markdown))

# caption = ollama_image_caption(prompt)

# print(caption['response'])

'''


'''