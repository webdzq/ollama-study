import ollama
def ollama_image_caption(msg):
    client = ollama.Client(host='http://localhost:11434')
    # 设置提示语
    prompt_v = msg or "hello world"
    response = client.generate(
        model='llava', prompt=prompt_v)
    return response

# 调用
# 指令内容，使用 ``` 来分隔指令和待总结的内容
text_1 = f"""
泡一杯茶很容易。首先，需要把水烧开。\
在等待期间，拿一个杯子并把茶包放进去。\
一旦水足够热，就把它倒在茶包上。\
等待一会儿，让茶叶浸泡。几分钟后，取出茶包。\
如果您愿意，可以加一些糖或牛奶调味。\
就这样，您可以享受一杯美味的茶了。
"""
prompt = f"""
您将获得由三个引号括起来的文本。\
如果它包含一系列的指令，则需要按照以下格式重新编写这些指令：

第一步 - ...
第二步 - …
…
第N步 - …

如果文本中不包含一系列的指令，则直接写“未提供步骤”。"
\"\"\"{text_1}\"\"\"
"""

caption = ollama_image_caption(prompt)

print(caption)

'''
{
    'model': 'llava',
    'created_at': '2024-10-30T08:29:47.487568Z',
    'response': ' 第一步 - 把水烧开\n第二步 - 拿一个杯子并把茶包放进去\n第三步 - 等待一会儿，让茶叶浸泡\n第四步 - 几分钟后，取出茶包\n第五步 - 如果您愿意，可以加一些糖或牛奶调味。\n就这样，您可以享受一杯美味的茶了. ',
    'done': True,
    'done_reason': 'stop',
    'context': [733, 16289, 28793, 28705, 13, 29689, 29248, 29072, 29291, 29590, 29492, 28995, 29544, 29170, 30574,
        29676, 29263, 28914, 29019, 29119, 28944, 29118, 29098, 29928, 29333, 29872, 28969, 29401, 29150, 28914,
        29223, 29752, 28924, 29310, 29259, 29059, 29518, 30131, 29074, 29061, 29293, 29122, 29249, 29056, 29402,
        29503, 29176, 29904, 29223, 29752, 28994, 13, 13, 29353, 28969, 29783, 387, 3850, 13, 29353, 29482, 29783,
        387, 8140, 13, 28878, 13, 29353, 28759, 29783, 387, 8140, 13, 13, 29118, 29098, 29019, 29119, 28991, 28988,
        29333, 29872, 28969, 29401, 29150, 28914, 29223, 29752, 28924, 29310, 29589, 29076, 29503, 28835, 29509,
        29279, 29954, 29783, 236, 173, 167, 28838, 28944, 28739, 13, 18552, 13, 233, 182, 164, 28969, 233, 160, 178,
        31713, 30111, 29329, 29945, 28944, 29993, 29596, 28924, 29259, 29059, 29855, 29692, 234, 134, 170, 29177,
        28944, 29010, 29414, 29876, 29275, 29117, 28924, 31191, 28518, 233, 160, 178, 29169, 29457, 29855, 31713,
        29333, 29441, 29258, 29651, 28944, 28969, 233, 154, 169, 29692, 30303, 31194, 30898, 28924, 29379, 29855,
        29928, 31146, 29010, 31713, 29333, 29054, 28944, 29414, 29876, 28969, 29179, 30915, 28924, 30447, 31713,
        31634, 233, 184, 187, 233, 182, 164, 28944, 30523, 29062, 30612, 29120, 28924, 29012, 29065, 31713, 29333,
        28944, 29118, 29098, 29689, 233, 135, 194, 29462, 28924, 29052, 29074, 29058, 28969, 29904, 234, 182, 153,
        29355, 30857, 232, 168, 185, 29231, 31170, 28944, 29379, 29176, 29675, 28924, 29689, 29052, 29074, 30461,
        30154, 28969, 233, 160, 178, 29817, 31170, 28914, 31713, 29105, 28944, 13, 18552, 13, 733, 28748, 16289,
        28793, 28705, 29353, 28969, 29783, 387, 28705, 29855, 29692, 234, 134, 170, 29177, 13, 29353, 29482, 29783,
        387, 28705, 31191, 28518, 233, 160, 178, 29169, 29457, 29855, 31713, 29333, 29441, 29258, 29651, 13, 29353,
        29492, 29783, 387, 28705, 29414, 29876, 28969, 29179, 30915, 28924, 30447, 31713, 31634, 233, 184, 187, 233,
        182, 164, 13, 29353, 29882, 29783, 387, 28705, 30523, 29062, 30612, 29120, 28924, 29012, 29065, 31713,
        29333, 13, 29353, 30108, 29783, 387, 28705, 29118, 29098, 29689, 233, 135, 194, 29462, 28924, 29052, 29074,
        29058, 28969, 29904, 234, 182, 153, 29355, 30857, 232, 168, 185, 29231, 31170, 28944, 13, 29379, 29176,
        29675, 28924, 29689, 29052, 29074, 30461, 30154, 28969, 233, 160, 178, 29817, 31170, 28914, 31713, 29105,
        28723, 28705],
    'total_duration': 70321486621,
    'load_duration': 8578331275,
    'prompt_eval_count': 246,
    'prompt_eval_duration': 32184381000,
    'eval_count': 119,
    'eval_duration': 29549798000
}

'''