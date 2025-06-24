from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from algorithm import bellman_ford

app = FastAPI()

class Edge(BaseModel):
    from_node: str
    to_node: str
    weight: float

class GraphInput(BaseModel):
    nodes: List[str]
    edges: List[Edge]
    source: str

@app.post("/run")
def run_algorithm(data: GraphInput):
    return bellman_ford(data.nodes, [e.dict() for e in data.edges], data.source)
