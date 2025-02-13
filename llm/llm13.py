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
# 示例：产品说明书
user_messages = [
  "La performance du système est plus lente que d'habitude.",  # System performance is slower than normal         
  "Mi monitor tiene píxeles que no se iluminan.",              # My monitor has pixels that are not lighting
  "Il mio mouse non funziona",                                 # My mouse is not working
  "Mój klawisz Ctrl jest zepsuty",                             # My keyboard has a broken control key
  "我的屏幕在闪烁"                                             # My screen is flashing
]
# Prompt ：基于说明书创建营销描述

for issue in user_messages:
    time.sleep(20)
    prompt = f"告诉我以下文本是什么语种，直接输出语种，如法语，无需输出标点符号: ```{issue}```"
    lang = ollama_image_caption(prompt)
    print(f"原始消息 ({lang['response']}): {issue}\n")

    prompt = f"""
    将以下消息分别翻译成英文和中文，并写成
    中文翻译：xxx
    英文翻译：yyy
    的格式：
    ```{issue}```
    """
    response = ollama_image_caption(prompt)
    print(response['response'], "\n=========================================")
# caption = ollama_image_caption(prompt)

# print(caption['response'])

'''
原始消息 ( 法语 ): La performance du système est plus lente que d'habitude.

 La performance du système est plus lente que d'habitude.  
=========================================
原始消息 ( 这段文本属于英语语言。 ): Mi monitor tiene píxeles que no se iluminan.

 中文翻译：嗯嗯嗯，这个 Mi monitor 有 6324 万像素，但是有些像素并不会被亮灯。
英文翻译：Mi monitor has 6324 pixels but some of the pixels do not get lit up.  
=========================================
原始消息 ( It is an Italian language text. ): Il mio mouse non funziona

 ```Il mio mouse non funziona``` 中文翻译：我的鼠标不工作。英文翻译："My mouse doesn't work."  
=========================================
原始消息 ( 英语 ): Mój klawisz Ctrl jest zepsuty

 中文翻译：我的Ctrl键盘上按下了。
英文翻译：My Ctrl key is pressed.  
=========================================
原始消息 ( 这段文本是英语。 ): 我的屏幕在闪烁

 中文翻译：我的屏幕闪烁了

英文翻译：My screen is flickering.  
=========================================



'''