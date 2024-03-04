The news_summarization_tool has the purpose to summarize articles from cybersecurity news websites using different large language models.
At the moment the Scraper class only reads the content of the website https://www.schneier.com/. 

#Requirements
In order to run the program some libraries need to be installed:
```
pip install requests
pip install beautifulsoup4
```
For each LLM you need to install specific libraries.
- for the GPT model:
```
pip install openai
```
To be able to use the API, an unique API key needs to be generated on the [OpenAI](https://platform.openai.com/api-keys) website.
The key can either be stored inside a txt file which will be read in the module llm_summarizer or set the value of the key variable directly in the same module. 

- for the Llama 2 model:
```
pip install llama-cpp-python
```
To be able to use GPU acceleration for Nvidia graphic cards, the following environmental variables will need to be set before the previous pip install:
```
set CMAKE_ARGS=-DLLAMA_CUBLAS=on
set FORCE_CMAKE=1
```
Further GPU acceleration backends can be found [here](https://github.com/abetlen/llama-cpp-python). 

- for the FalconsAI/text_summarization model:
```
pip install transformers
```

#How to start the program
By default the news_summarization_tool will be started with GPT model, but you can choose a different model with the following commands: 
```
python3.11 .\news_summarization_tool.py 
python3.11 .\news_summarization_tool.py -m GPT
python3.11 .\news_summarization_tool.py -m Llama2
python3.11 .\news_summarization_tool.py -m FalconsAI
```
