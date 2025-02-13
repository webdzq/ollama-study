
# 使用gradio的图形界面
'''
官方文档：https://www.gradio.app/docs
pip install gradio

'''
import gradio as gr
import ollama

def generate_text(prompt):
    client = ollama.Client(host='http://localhost:11434')
    response = client.generate(
        model='llava', prompt=prompt)
    return response['response']
# 定义可用的模型列表
models = ["llava"]
# 启动Gradio应用
iface = gr.Interface(
    fn=generate_text,
    inputs=[
        # gr.Dropdown(models, label="选择语言模型"),
        gr.Textbox(label="输入问题")
    ],
    outputs="text",
    title="网页知识问答系统"
)
iface.launch(share=True)

'''
[Running] python -u "/Users/apple/github/ollama-study/demos/gradioUI.py"
输出结果
Running on local URL:  http://127.0.0.1:7860

Could not create share link. Missing file: /Users/apple/opt/anaconda3/lib/python3.9/site-packages/gradio/frpc_darwin_amd64_v0.2. 

Please check your internet connection. This can happen if your antivirus software blocks the download of this file. You can install manually by following these steps: 

1. Download this file: https://cdn-media.huggingface.co/frpc-gradio-0.2/frpc_darwin_amd64
2. Rename the downloaded file to: frpc_darwin_amd64_v0.2
3. Move the file to this location: /Users/apple/opt/anaconda3/lib/python3.9/site-packages/gradio

'''