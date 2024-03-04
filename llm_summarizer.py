from llama_cpp import Llama
import openai 
from transformers import pipeline
from utils import Model 

# put your on path to the txt which contains the key
with open("C:/Users/tyran/OneDrive/Desktop/Backups/key.txt", "r", encoding="utf-8") as file:
    key = file.readline()

# the GPT API key
openai.api_key = key
COMMAND_GPT = "Summarize the following content in the form short news. Don't add a title. Give at the Ende of the Article #Tags fitting to the content of the article" # "Summarize the following content. Give A title for the content at the top. Don't call it summary and add the link to the content given in the data at the end: "

'''
Depending on the given model parameter, the function calls the corresponding function to summarize the given content and returns the result.  
'''
def create_content_summary(model: Model, content: str) -> str:
    if model == Model.Llama2:
        return create_content_summary_llama(content)
    elif model == Model.FalconsAI:
        return create_content_summary_FalconsAI(content)   
    else: 
        return create_content_summary_gpt(content)

'''
Summarizes the given content using the GPT API.  
'''
def create_content_summary_gpt(content: str) -> str:
    print("-----------Calling GPT API------------")
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "you are a helpful research assistant."},
            {"role": "user", "content": COMMAND_GPT + "\n" + content} 
        ]
    )
    reply = response.choices[0].message.content
    print(reply)
    return reply

'''
Summarizes the given content using the Llama2 model.  
'''
def create_content_summary_llama(content: str) -> str:
    llm = Llama(model_path="E:\Daniel\BA\llama\llama-2-7b.Q5_K_M.gguf", chat_format="llama-2", n_ctx=1024)
    print("-----------Start Llama model------------")
    response = llm("summarize: " + content, max_tokens= 800, temperature = 0.5, repeat_penalty=1.3)
    reply = response["choices"][0]["text"].strip()
    print(reply)
    return reply 

'''
Summarizes the given content using the FalconsAI model.  
'''
def create_content_summary_FalconsAI(content: str) -> str:
    model_pipeline = pipeline("summarization", model="Falconsai/text_summarization")
    print("-----------Start FalconsAI model------------")
    return(model_pipeline(content, max_length=content.count(" "), min_length=int(content.count(" ")/3),do_sample=False)[0]["summary_text"])