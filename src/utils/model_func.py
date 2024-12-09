from langchain_ollama.chat_models import ChatOllama
from langchain_ollama import OllamaEmbeddings
from utils.database_func import getData

model_name = "andresinho20049/lumin"
base_url = "http://ollama:11434"

def getContext():
    ollama_embedding = OllamaEmbeddings(
        model = model_name,
        base_url = base_url
    )

    collection = []
    two_vectors = ollama_embedding.embed_documents(getData())
    for vector in two_vectors:
        collection.append(str(vector)[:100])

    return collection


def getModel():
    return ChatOllama(
        model = model_name,
        base_url = base_url,
        temperature = 0.8,
        num_predict = -2,
    )

def chatServiceStream(text):
    model = getModel()
    return model.stream(text)

def chatService(text):
    model = getModel()
    return model.invoke(text)