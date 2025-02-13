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
data_json = { "resturant employees" :[ 
    {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},
    {"name":"Bob", "email":"bob32@gmail.com"},
    {"name":"Jai", "email":"jai87@gmail.com"}
]}

# Prompt ：基于说明书创建营销描述

prompt = f"""
将以下Python字典从JSON转换为HTML表格，保留表格标题和列名：{data_json}
"""
caption = ollama_image_caption(prompt)

print(caption['response'])

'''
以下是将Python字典转换为HTML表格的示例代码：
```python
import json

# Python字典
data = {
    "resturant employees": [
        {'name': 'Shyam', 'email': 'shyamjaiswal@gmail.com'},
        {'name': 'Bob', 'email': 'bob32@gmail.com'},
        {'name': 'Jai', 'email': 'jai87@gmail.com'}
    ]
}

# JSON字符串
json_data = json.dumps(data)

# HTML表格字符串
html_table = '<table><thead><tr>' + \
                  '<th>Employee</th>' + \
                  '<th>Email</th></tr></thead><tbody>'
for employee in data["resturant employees"]:
    html_table += '<tr>' + \
                      '<td>{}</td>' + \
                      '<td>{}</td></tr>'.format(employee["name"], employee["email"])
html_table += '</tbody></table>'

# 输出HTML表格字符串
print(html_table)
```
输出的HTML表格如下：
```html
<table>
    <thead>
        <tr>
            <th>Employee</th>
            <th>Email</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Shyam</td>
            <td>shyamjaiswal@gmail.com</td>
        </tr>
        <tr>
            <td>Bob</td>
            <td>bob32@gmail.com</td>
        </tr>
        <tr>
            <td>Jai</td>
            <td>jai87@gmail.com</td>
        </tr>
    </tbody>
</table>
``` 


'''