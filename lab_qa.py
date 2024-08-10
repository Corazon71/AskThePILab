import os

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationSummaryMemory
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA



ldr = PyPDFLoader("your_lab_manual.pdf")
data = ldr.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=3000, chunk_overlap=700)
txt = splitter.split_documents(data)
db = Chroma.from_documents(txt, OpenAIEmbeddings())
retriever = db.as_retriever(search_type= 'mmr')
llm = ChatOpenAI(model_name="gpt-3.5-turbo")

memory = ConversationSummaryMemory(llm=llm, memory_key="chat_history", return_message=True)
template = """
Answer the question based on the following context (Do not answer from any other source. 
If the context doesn't have the answer say you 
cant answer)
{context}
Question: {question}
"""

prompt = PromptTemplate(input_variables=["context", "question"], template=template)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    memory=memory,
    chain_type_kwargs={'prompt': prompt}
)

def start(message):
    response = qa.invoke(message)
    return response['result']
