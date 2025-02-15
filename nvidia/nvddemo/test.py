# -*- coding: utf-8 -*-

# 导入必要的库
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings, ChatNVIDIA
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import chain
import os
import gradio as gr
from datetime import datetime

# 假设性回答模板，这里假设是分析数据的趋势相关问题
hyde_template = """Even if you do not know the full answer, generate a one-paragraph hypothetical answer to the below data analysis question:

{question}"""

# 最终回答模板，基于提供的数据上下文回答问题
template = """Answer the data analysis question based only on the following data context:
{context}

Question: {question}
"""

# 定义函数来处理数据分析问题
def process_data_question(data_file_path, api_key, model_name, question):
    # 初始化加载器并加载数据
    loader = TextLoader(data_file_path)
    docs = loader.load()

    # 设置环境变量
    os.environ['NVIDIA_API_KEY'] = api_key

    # 初始化嵌入层
    embeddings = NVIDIAEmbeddings()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    documents = text_splitter.split_documents(docs)
    vector = FAISS.from_documents(documents, embeddings)
    retriever = vector.as_retriever()

    # 初始化模型
    model = ChatNVIDIA(model=model_name)

    # 创建提示模板
    hyde_prompt = ChatPromptTemplate.from_template(hyde_template)
    hyde_query_transformer = hyde_prompt | model | StrOutputParser()

    # 定义检索函数
    @chain
    def hyde_retriever(question):
        hypothetical_document = hyde_query_transformer.invoke({"question": question})
        return retriever.invoke(hypothetical_document)

    # 定义最终回答链
    prompt = ChatPromptTemplate.from_template(template)
    answer_chain = prompt | model | StrOutputParser()

    @chain
    def final_chain(question):
        documents = hyde_retriever.invoke(question)
        response = ""
        for s in answer_chain.stream({"question": question, "context": documents}):
            response += s
        return response

    # 调用最终链获取答案
    return str(datetime.now()) + final_chain.invoke(question)

# 定义可用的模型列表
models = ["mistralai/mistral-7b-instruct-v0.2", "meta/llama-3.1-405b-instruct"]

# 启动Gradio应用
iface = gr.Interface(
    fn=process_data_question,
    inputs=[
        gr.Textbox(label="输入数据文件路径"),
        gr.Textbox(label="NVIDIA API Key"),
        gr.Dropdown(models, label="选择语言模型"),
        gr.Textbox(label="输入数据分析问题")
    ],
    outputs="text",
    title="数据分析问答系统"
)

iface.launch()