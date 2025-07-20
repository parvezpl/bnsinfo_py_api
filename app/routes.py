from fastapi import APIRouter
from app.qdrant_client import client, COLLECTION_NAME
from app.vector_model import get_vector
from qdrant_client.models import Filter, FieldCondition, MatchValue
import uuid
from typing import Dict, List, Any

router = APIRouter()

@router.get("/findsection/", response_model=None)
def get_content_section(field: str, value: int, limit: int =2 ):

    filter_query = Filter(
        must=[
            FieldCondition(
                key=field,
                match=MatchValue(value=value)
            )
        ]
    )

    results = client.scroll(
        collection_name=COLLECTION_NAME,
        limit=limit,
        scroll_filter=filter_query,
        with_payload=True
    )

    # Clean result for response
    return {
        "results": [
            {
                "id": r.id,
                "payload": r.payload
            } for r in results[0]
        ]
    } 

@router.get("/search/")
def search_text(query: str, limit: int = 5):
    print(query, limit )
    vector = get_vector(query)
    results = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=vector,
        limit=limit
    )

    return {
        "results": [
            {"score": r.score, "chapter":r.payload.get("chapter"), "section":r.payload.get("section"), "content": r.payload.get("content")} for r in results
        ]
    }
