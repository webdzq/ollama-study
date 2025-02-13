# detoxify库没有安装成功
import ollama
import pandas as pd
from io import StringIO
# import detoxify

# curl http://localhost:11434/api/chat -d '{
#   "model": "llama3.2",
#   "messages": [
#     { "role": "user", "content": "why is the sky blue?" }
#   ]
# }'
def ollama_image_caption(msg):
    client = ollama.Client(host='http://localhost:11434')
    # 设置提示语
    prompt_v = msg or "hello world"
    response = client.generate(
        model='llama3.2', prompt=prompt_v)
    return response

# 调用

# 敏感词
moderation_output = [
        "kill", "murder", "slay", "violence", "violent", "assault", "attack", "harm", "injure",
        "nigger", "chink", "infidel", "bitch", "faggot",
        "fuck", "porn", "penis", "vagina",
        "drug", "heroin", "gamble", "steal",
        "virus", "malware", "hacker", "phishing"
    ]
moderation_output_df = pd.DataFrame(moderation_output)
res = ollama_image_caption(f"将以下dataframe中的内容翻译成中文：{moderation_output_df.to_csv()}")
print(res['response'])
# pd.read_csv(StringIO(res['response']))

# caption = ollama_image_caption(messages)

# print(caption['message'])

'''



'''