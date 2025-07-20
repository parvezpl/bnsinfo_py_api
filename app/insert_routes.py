from fastapi import APIRouter
from app.qdrant_client import client, COLLECTION_NAME
from app.vector_model import get_vector
from qdrant_client.models import PointStruct
import uuid

inset_router = APIRouter()

@inset_router.post("/add-content/")
def add_text(content: str, section:int, language:str='hindi'):
    vector = get_vector(content)
    point_id = str(uuid.uuid4())
    client.upsert(
        collection_name=COLLECTION_NAME,
        points=[
            PointStruct(
                id=point_id,
                vector=vector,
                payload={
                        "section":section,
                        "content": content,
                        "language":language,
                        "type":f"cunk-${section}"
                        }
            )
        ]
    )
    return {"status": "Chunk Vector added", "id": point_id}