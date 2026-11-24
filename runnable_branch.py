from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableLambda, RunnableParallel, Runnable Branch

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

prompt = PromptTemplate(
    template="Write a detailed report about the topic {topic}",
    input_variables=["topic"]
)

Prompt2 = PromptTemplate(
    template="Summarised this text \n {text} \n in 100 words",
    input_variables=["text"]
)
perser = StrOutputParser()

chain1 = RunnableSequence(prompt1, llm, perser)

branch_chain = RunnableBranch(
    {
        (lambda x: len(x.split()) > 500, RunnableSequence(Prompt2, llm, perser)),
        (RunnablePassthrough(chain1))
    }
)

final_chain = RunnableSequence(chain1, branch_chain, perser)

print(final_chain.invoke({"topic": "AI"}))
