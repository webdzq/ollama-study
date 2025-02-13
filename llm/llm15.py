import ollama
import time
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
text = [ 
  "The girl with the black and white puppies have a ball.",  # The girl has a ball.
  "Yolanda has her notebook.", # ok
  "Its going to be a long day. Does the car need it’s oil changed?",  # Homonyms
  "Their goes my freedom. There going to bring they’re suitcases.",  # Homonyms
  "Your going to need you’re notebook.",  # Homonyms
  "That medicine effects my ability to sleep. Have you heard of the butterfly affect?", # Homonyms
  "This phrase is to cherck chatGPT for spelling abilitty"  # spelling
]


# Prompt ：基于说明书创建营销描述

for i in range(len(text)):
    time.sleep(5)
    prompt = f"""请校对并更正以下文本，注意纠正文本保持原始语种，无需输出原始文本。
    如果您没有发现任何错误，请说“未发现错误”。
    
    例如：
    输入：I are happy.
    输出：I am happy.
    ```{text[i]}```"""
    response = ollama_image_caption(prompt)
    print(i, response['response'])

# caption = ollama_image_caption(prompt)

# print(caption['response'])

'''
0  已经纠正的文本：

"这位女孩有一双黑白色的狗仔，有一个球。"

注意：在校对过程中，我认为这是一个正确的句子，因此不需要更正。 
1  未发现错误。 
2  以下是更正后的文本：

例如：

输入：I are happy.

输出：I am happy.

更正原因：词性分析。“I”应该用单数形式，而不是复数形式，因为“I”这个动词的主语是人称代词（它指向的人是 singular），所以需要单数形式。同时，谓词和形容词也应该使用单数形式，例如“am”和“happy”。

更正后的文本：

"It's going to be a long day. Does the car need its oil changed?" 
3  Their goes my freedom. There going to bring their suitcases. 
4  未发现错误 
5  抱歉，我无法发现您提供的文本中的任何错误。所有给定的文本都是正确的，不需要纠正。 
6  很抱歉，我没有找到任何错误。请提供需要校对的文本以便我为您校对。 


'''