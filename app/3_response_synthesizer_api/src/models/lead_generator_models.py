from datetime import datetime
from typing import Dict, List, Optional
from fastapi import Query

from pydantic import BaseModel, Field

class JobPostingRequest(BaseModel):
    username: str
    user_id: str
    job_posting: str
    service: str

class ClientInformation(BaseModel):
    payment_method: str | None
    rating: int | None
    location: str | None
    local_time: str | None
    number_of_jobs_posted: int | None
    hire_rate: int | None
    open_jobs: int | None
    total_amount_spent: str | None
    number_of_hires: int | None
    active_hires: int | None
    industry: str | None
    membership_since: str | None


class ProjectInfo(BaseModel):
    project_name: str
    job_desctition: str
    objectives: List[str] = []
    technical_requirements: Dict[str,List[str]]
    deliverables: List[str]
    project_duration: str
    selection_criteria: List[str]
    proposal_requirements: List[str] 


class JobPostingInfo(BaseModel):
    client_information: ClientInformation
    project_information: ProjectInfo


class JobPostingResponse(BaseModel):
    conversation_id: str
    job_posting: JobPostingInfo


class ProposalRequest(BaseModel):
    query: str
    question: List[str] = Field(Query([]))
    answers: List[str] =  Field(Query([]))


class ProposalResponse(BaseModel):
    conversation_id: str
    response: str