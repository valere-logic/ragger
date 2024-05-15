from datetime import datetime
from typing import Dict, List, Optional
from fastapi import Query

from pydantic import BaseModel, Field

class JobPostingRequest(BaseModel):
    query: str
    question: List[str] = Field(Query([]))
    answers: List[str] =  Field(Query([]))


class JobPostingResponse(BaseModel):
    conversation_id: str
    response: str


class ProposalRequest(BaseModel):
    query: str
    question: List[str] = Field(Query([]))
    answers: List[str] =  Field(Query([]))


class ProposalResponse(BaseModel):
    conversation_id: str
    response: str