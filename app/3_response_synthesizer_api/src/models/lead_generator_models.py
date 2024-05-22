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
    rating: str | int | None
    location: str | None
    local_time: str | None
    number_of_jobs_posted: str | int | None
    hire_rate: str | int | None
    open_jobs: str | int | None
    total_amount_spent: str | None
    number_of_hires: str | int | None
    active_hires: str | int | None
    industry: str | None
    membership_since: str | None


class ProjectInfo(BaseModel):
    project_name: str
    job_description: str
    objectives: List[str] = []
    technical_requirements: Dict[str,List[str]]
    deliverables: List[str]
    total_project_duration: str
    selection_criteria: List[str]
    proposal_requirements: List[str] 
    job_information: dict

{'project_name': 'Web-based Accounting Platform with AI Support', 'job_description': 'We are looking for a talented developer to build a web-based accounting platform with integrated AI-support. The platform should have the following features:  - User-friendly interface that allows users to easily manage their finances - AI capabilities to automate tasks such as booking entries, invoice generation, and financial analysis', 'objectives': ['User-friendly interface', 'AI capabilities to automate tasks'], 'technical_requirements': {'languages': ['HTML', 'CSS', 'JavaScript'], 'frameworks': ['Node.js', 'Django']}, 'deliverables': ['A fully functional web-based accounting platform with AI support.'], 'timeline': {'total_project_duration': '3 to 6 months'}, 'selection_criteria': ['Proficiency in web development languages', 'Experience with backend development using frameworks like Node.js or Django', 'Knowledge of accounting principles and practices', 'Familiarity with AI and machine learning technologies'], 'proposal_requirements': ['Outline your approach to the project.', 'Provide a timeline with milestones and deliverables.', 'Include any questions you have about the project scope or technical aspects.'], 'job_information': {'experience_level': 'Intermediate', 'compensation': '$15.00 - $35.00 Hourly', 'job_commitment': 'Less than 30 hrs/week', 'estimated_duration': '3 to 6 months', 'skills_and_expertise': ['HTML', 'CSS', 'JavaScript', 'Node.js', 'Django', 'Accounting Principles', 'AI and Machine Learning Technologies']}}
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