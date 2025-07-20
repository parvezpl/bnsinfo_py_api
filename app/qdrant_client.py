from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams
from dotenv import load_dotenv
import os

load_dotenv()

# Use cloud or local Qdrant
QDRANT_URL = "http://localhost:6333"


QDRANT_CLOUD_URL = os.getenv("QDRANT_URL_CLOUD")
API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

client = QdrantClient(url=QDRANT_URL)

# if API_KEY and QDRANT_CLOUD_URL:
#     print("qdrent cloud connected")
#     client = QdrantClient(
#         url=QDRANT_CLOUD_URL,
#         api_key=API_KEY
#     )
# else:
#     print("host is connetct qdrent ")
#     client = QdrantClient(url=QDRANT_URL)

# Optional: Create collection (once)
def init_collection():
    if not client.collection_exists(COLLECTION_NAME):
        client.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=384, distance="Cosine")  # 384 for MiniLM
        )
