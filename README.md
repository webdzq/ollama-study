# ollama-study

对ollama的学习，主要在mac上本地部署ollama，然后完成prompt（大模型提示词）的一些功能实现。包括最火的deepseek-r1模型等等。使用的python环境，python环境的配置略，大家自行安排。python的版本在3.9.x以上就行，最好使用最新稳定版本。可以使用vscode、notebook等。我使用的是vscode。

## 1、ollama的安装

1. **安装 ollama**：
   - **下载**：访问[ollama 官网](https://ollama.com/download)，根据你的 Mac 操作系统版本下载对应的 ollama 安装包。
   - **安装**：双击下载好的安装包，按照提示进行安装操作，将 ollama 安装到你的 Mac 上。安装完成后，打开一个新的终端窗口，确保可以使用 `ollama`命令。
2. **下载 LLaMa3 模型**：
   - 在终端中输入 `ollama run llama3`命令，ollama 会自动开始下载 LLaMa3 模型。下载速度取决于你的网络状况，8B 版本的模型大小约为 4.7GB。如果想下载其他版本（如 70B 或 405B），可根据实际需求进行选择，但这些较大的版本对硬件配置要求较高。

3. **配置和使用**：
   - 模型下载完成后，你就可以在终端中与 LLaMa3 进行交互了。在终端中输入问题，LLaMa3 会给出回答。
   - 如果你想要更直观的图形界面进行交互，可以考虑使用一些基于 ollama 的 Web UI 项目，如[ollama-webui-lite](https://github.com/ollama-webui/ollama-webui-lite)。首先需要安装[Node.js](https://nodejs.org/)，然后在终端中执行以下命令来部署 Web UI：
     1. `git clone https://github.com/ollama-webui/ollama-webui-lite.git`：克隆项目到本地。
     2. `cd ollama-webui-lite`：进入项目目录。
     3. `npm install`：安装项目依赖。
     4. `npm run dev`：启动开发服务器。
     5. 启动成功后，在浏览器中访问 `http://localhost:3000`，即可看到图形界面，在界面中输入问题与 LLaMa3 进行交互。
4. **其他**:
   - `ollama `支持的模型非常多，包括文本/对话模型、图片模型和视频模型等等，根据需要安装不同模型。常用的模型有：llama3、DeepSeek-R1、qwen2.5等等。下载模型要主要参数规模，规模越大，本地占用的空间越大，大家量力而行哈！

## 2、demo代码执行

2.1 主要参考llm教材的文档，把openai换成ollama中的模型去验证。

2.2 主要实现了知识问答系统、看图写话、聊天机器人，也使用了gradio图形界面和panel库等实现UI页面访问。

2.3 没有验证内容审核模块，langchain和ollama结合使用等功能。

## 3、ollama的优点

3.1 开源免费，本地安装使用，普通配置的电脑都可以本地运行，对于学习大模型很有帮助。

3.2  ollama相当于npm、pip等包管理工具，它是一个大模型管理工具，支持llama3.2、qwen，phi等很多开源模型的使用。通过 `ollama run xx` 来安装。

## 4、文献

4.1 面向开发者的大模型学习教程：[目录 (datawhalechina.github.io)](https://datawhalechina.github.io/llm-cookbook/#/README)

4.2 ollamad的模型库：[library (ollama.com)](https://ollama.com/library)

4.3 ollama项目介绍：[ollama/ollama: Get up and running with Llama 3.2, Mistral, Gemma 2, and other large language models. (github.com)](https://github.com/ollama/ollama)


## 5、 对AI的看法
 文字也好，图片也好，都是根据一些信息做匹配动作，还是和查字典一样。只是输入的内容形式不用了。要想查询到好的结果，需要好好打磨查询条件。


## 项目目录介绍

- demos里都是源码，包括看图写话、文本问答、gradioUI问答页面、文本转tts语音、deepseek模型使用等。
- llm里是大模型提示词源码，好的提示词模板更能得到想要的结果，所以非常有必要研究一下。