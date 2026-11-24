from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate a tweet about the topic {topic}?",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate a linkedin post about the topic {topic}?",
    input_variables=["topic"]
)

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

parser = StrOutputParser()

chain = RunnableParallel({
    "tweet": RunnableLambda(prompt1 | llm | parser),
    "linkedin": RunnableLambda(prompt2 | llm | parser)
})

print(chain.invoke({"topic": "AI"}))
