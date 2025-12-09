from fastapi import FastAPI
from api import router as rag_router
from api_dropout import router as dropout_router
app = FastAPI()

app.include_router(rag_router, prefix="/rag", tags=["RAG"])
app.include_router(dropout_router, prefix="/dropout", tags=["Dropout Analysis"])

