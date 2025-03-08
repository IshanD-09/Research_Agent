from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

global template
def summarize(retrieved_documents):
    template = """Consolidate the key information and findings of this paper in 10-11 bullet points: {paper}"""

    prompt = ChatPromptTemplate.from_template(template)

    model = OllamaLLM(model="llama3.2")

    chain = prompt | model

    return chain.invoke({"paper": retrieved_documents})