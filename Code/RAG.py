import pinecone
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from dotenv import load_dotenv

load_dotenv()

embeddings = OllamaEmbeddings(model="nomic-embed-text")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=75, length_function=len, is_separator_regex=False)

vector_store = Chroma(collection_name="research_paper_collection", embedding_function=embeddings, persist_directory="C:\CodeWin\Research_Agent\Code\Vector_data", )
