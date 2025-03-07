import pinecone
from langchain.vectorstores import Pinecone
from dotenv import load_dotenv

load_dotenv()

pinecone.init(api_key="PINECONE_API_KEY", environment="us-east-1")
pinecone.list_indexes()
