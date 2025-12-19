from langchain_community.llms import Ollama
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

def load_llm_with_memory():
    llm = Ollama(model="llama3.2", temperature=0)

    memory = ConversationBufferMemory(
        memory_key="history",
        return_messages=True
    )

    chain = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=False
    )

    return chain
