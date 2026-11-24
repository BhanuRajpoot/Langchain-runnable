from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()

prompt = PromptTemplate(
    template="What is the capital of {country}?",
    input_variables=["country"]
    )

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

perser = StrOutputParser()

chain = RunnableSequence(prompt, llm, perser)

print(chain.invoke({"country": "France"}))
