from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableLambda, RunnableParallel, Runnable Passthrough

load_dotenv()

def word_count(text: str) -> int:
    return len(text.split())

prompt = PromptTemplate(
    template="What is the capital of {country}?",
    input_variables=["country"]
    )

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

perser = StrOutputParser()

chain = RunnableSequence(prompt, llm, perser)

parallel_chain = RunnableParallel({
    "text": RunnablePassthrough(chain),
    "capital": RunnableLambda(word_count)
})

print(parallel_chain.invoke({"country": "France"}))
