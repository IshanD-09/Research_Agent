from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

global template
def summarize(retrieved_documents):
    template = """Consolidate the key information and findings of this paper in 10-11 bullet points to use in future research. Don't forget context: {paper}"""

    prompt = ChatPromptTemplate.from_template(template)

    model = OllamaLLM(model="llama3.2", temperature=0.7)

    chain = prompt | model

    return chain.invoke({"paper": retrieved_documents})