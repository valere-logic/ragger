from typing import List, Annotated
import json

from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from starlette import status
from starlette.responses import JSONResponse

from services.lead_generator_service import LeadGenerator

from models.lead_generator_models import ProposalRequest, ProposalResponse, JobPostingRequest, JobPostingResponse, ProjectInfo, JobPostingInfo, ClientInformation

lead_generator_TAG = "lead_generator"

def init_lead_generator_router():
    """
    Price conversion router which holds endpoints to return a price data from database
    """
    lead_generator_router = APIRouter(
        prefix="/leads",
        tags=[lead_generator_TAG])

    lead_generator_service = LeadGenerator()

    @lead_generator_router.get(
        "/description/{conversation_id}",
        response_model=JobPostingResponse
    )
    async def describe(
        conversion_id: str,
        job_posting_request: JobPostingRequest = Depends(),
      
    ):
        job_posting = job_posting_request.job_posting
        
        response = lead_generator_service.initialize_generate_job_desciption(job_posting)
        parsed_job_description = json.loads(response)
        parsed_job_description
        job_posting_dict = parsed_job_description["project_information"]
        print(parsed_job_description["client_information"])
        project_info = ProjectInfo(
            **job_posting_dict
        )
        client_info = ClientInformation(**parsed_job_description["client_information"])

        job_posting_info = JobPostingInfo(client_information=client_info, project_information=project_info)
        
        return JobPostingResponse(conversation_id=conversion_id, job_posting=job_posting_info)
    
    # lead_generator_router.get(
    #     "/proposal/{conversation_id}",
    #     response_model=QueryResponse,
    #     tags=[lead_generator_TAG],
    # )
    # async def propose(
    #     conversion_id: str,
    #     query_request: QueryRequest = Depends(),
      
    # ):
    #     query = query_request.query
    #     qa_pairs = zip(query_request.question, query_request.answers)
    #     response = response_synthesyzer_service.initialize_synthesizer(query, qa_pairs)
        
    #     return QueryResponse(conversation_id=conversion_id, response=response.response)
    
    return lead_generator_router