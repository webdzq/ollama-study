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
prompt = f"""
针对以下三个反引号之间的英文评论文本，
首先进行拼写及语法纠错，
然后将其转化成中文，
再将其转化成优质淘宝评论的风格，从各种角度出发，分别说明产品的优点与缺点，并进行总结。
润色一下描述，使评论更具有吸引力。
输出结果格式为：
【优点】xxx
【缺点】xxx
【总结】xxx
注意，只需填写xxx部分，并分段输出。
将结果输出成Markdown格式。
```{text}```
"""

response = ollama_image_caption(prompt)

diff = Redlines(text,response['response'])
print(diff.output_markdown)
# display(Markdown(diff.output_markdown))

# caption = ollama_image_caption(prompt)

# print(caption['response'])

'''
<span style='color:green;font-weight:700;'>| 评论文本 | 拼写及语法纠错 | 中文转换 | 优质淘宝评论风格 | </span>

<span style='color:green;font-weight:700;'>| --- | --- | --- | --- | </span>

<span style='color:green;font-weight:700;'>| </span>Got this for my daughter for her birthday cuz she keeps taking mine from my <span style='color:red;font-weight:700;text-decoration:line-through;'>room.  </span><span style='color:green;font-weight:700;'>room. </span>Yes, adults also like pandas <span style='color:red;font-weight:700;text-decoration:line-through;'>too.  </span><span style='color:green;font-weight:700;'>too. </span>She takes it everywhere with her, and it's super soft and <span style='color:red;font-weight:700;text-decoration:line-through;'>cute.  </span><span style='color:green;font-weight:700;'>cute. </span>One of the ears is a bit lower than the other, and I don't think that was designed to be asymmetrical. It's a bit small for what I paid for it though. I think there might be other options that are bigger for the same <span style='color:red;font-weight:700;text-decoration:line-through;'>price.  </span><span style='color:green;font-weight:700;'>price. </span>It arrived a day earlier than expected, so I got to play with it myself before I gave it to my <span style='color:red;font-weight:700;text-decoration:line-through;'>daughter.</span><span style='color:green;font-weight:700;'>daughter. | Got this for my daughter for her birthday because she keeps taking mine from my room. Yes, adults also like pandas too. She takes it everywhere with her, and it's super soft and cute. One of the ears is a bit lower than the other, and I don't think that was designed to be asymmetrical. It's a bit small for what I paid for it though. I think there might be other options that are bigger for the same price. It arrived a day earlier than expected, so I got to play with it myself before I gave it to my daughter. | 我为女儿的生日送了这只玩具，因为她一直喜欢将我的玩具拿走。大人也愿意喜欢熊猫。她把它带到处就行了，而且很软和可爱。但是一个耳朵比另一个低一点，我觉得不应该设计成不对称的状态。虽然价格的换算是一样的，但是它相比于我所支付的金额有些小，可能还有其他选项更大。我认为这个商品来得比预期的时间早，所以在送给女儿之前，我自己玩玩看看了一下。 | 【优点】 </span>

<span style='color:green;font-weight:700;'>* 很软、可爱，适合女孩喜欢的形状和颜色。 </span>

<span style='color:green;font-weight:700;'>* 有点小，但是非常可爱。 </span>

<span style='color:green;font-weight:700;'>* 吸引力强，可以在不同场景中使用。 </span>

<span style='color:green;font-weight:700;'>【缺点】 </span>

<span style='color:green;font-weight:700;'>* 设计成对称的状态，一个耳朵比另一个低一点，有些不符合预期。 </span>

<span style='color:green;font-weight:700;'>* 相比于我支付的金额，价格的换算是一样的，但是它比预期小了一些。 </span>

<span style='color:green;font-weight:700;'>* 其他选项可能更大。 </span>

<span style='color:green;font-weight:700;'>【总结】 </span>

<span style='color:green;font-weight:700;'>* 女孩喜欢的玩具，非常适合作为礼物。 </span>

<span style='color:green;font-weight:700;'>* 有点小，但是非常可爱。 </span>

<span style='color:green;font-weight:700;'>* 设计不对称，需要注意。 </span>

<span style='color:green;font-weight:700;'>* 价格比预期略低，建议在选择时候考虑其他更大的选项。 |</span>


'''