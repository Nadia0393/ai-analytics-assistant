from fastapi import APIRouter
from app.schemas import QueryRequest
from app.orchestrator import process_query

router = APIRouter()

#@router.get("/test")
#def test():
#    return {"message": "routes working"}

@router.post("/query")
def query_data(request: QueryRequest):
    #question=request.question
    #return {
    #    "question":question,
    #    "answer":"placeholder response"
    #}
    result=process_query(request.question)
    return result
