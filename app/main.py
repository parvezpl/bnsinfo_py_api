from fastapi import FastAPI
from app.qdrant_client import init_collection
from app.routes import router
from app.insert_routes import inset_router
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware




load_dotenv()
app = FastAPI(title="Qdrant + SentenceTransformer API")

origins = [
    "http://localhost:3000",  # Next.js dev server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,             # or ["*"] for all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello Parvez Alam from FastAPI!"}

# Initialize collection on startup
# @app.on_event("startup")
# def startup():
#     init_collection()
# Include routes
app.include_router(router)
app.include_router(inset_router)
