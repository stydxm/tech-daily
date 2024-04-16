from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSerializable
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

llm = ChatOpenAI()
embeddings = OpenAIEmbeddings()

summarize_template = ChatPromptTemplate.from_messages([
    ("system",
     "Generate a concise summary of the passage, and highlight key insights from the text."),
    ("user", "{input}")
])
summarize_chain = summarize_template | llm | StrOutputParser()
translate_template = ChatPromptTemplate.from_messages([
    ("system", "我希望你能担任中文翻译、拼写校对和修辞改进的角色。"
               "我会用英语和你交流，你会将其翻译成中文回答我。"
               "请将生硬的词汇和句子替换成更为通俗易懂的表达方式，确保意思不变。"
               "请仅回答更正和改进的部分，不要写解释。"),
    ("user", "我要你翻译的内容是：{input}")
])
translate_chain = translate_template | llm | StrOutputParser()


def project_summarize(raw_description: str) -> str:
    return make_chain("以下内容是一个开源项目的readme，请你用简短的句子简单概括该项目的用途，总结它的优点，整合成一句话，并以中文输出")\
        .invoke({"input": raw_description})


def summarize(raw_description: str) -> str:
    summarize_result = summarize_chain.invoke({"input": raw_description})
    translate_result = translate_chain.invoke({"input": summarize_result})
    return translate_result


def make_chain(prompt_string: str) -> RunnableSerializable:
    prompt = ChatPromptTemplate.from_messages([
        ("system", prompt_string),
        ("user", "{input}")
    ])
    chain = prompt | llm | StrOutputParser()
    return chain
