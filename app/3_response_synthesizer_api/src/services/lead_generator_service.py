from pathlib import Path
import json
from string import Template
import variables as vars
from llama_index.callbacks import (
    CallbackManager,
    LlamaDebugHandler,
    OpenInferenceCallbackHandler,
)
from llama_index import get_response_synthesizer

from llama_index.embeddings import HuggingFaceEmbedding
from llama_index.prompts.base import PromptTemplate
from llama_index.prompts.prompt_type import PromptType
from llama_index.schema import NodeWithScore, QueryBundle, TextNode
from llama_index import VectorStoreIndex, StorageContext, ServiceContext
from llama_index.llms.openai import OpenAI
from variables import CUR_DIR
from vector_stores.lead_gen.lead_gen_vector_store import get_vector_store, LeadGenVectorStore
from llm_utils import Config

from gen_deps.logger import create_logger


_logger = create_logger("response_synthesizer:model")


class LeadGenerator(object):
    

    def __init__(self) -> None:
        with open(Path(CUR_DIR, "prompts", "lead_gen", "project_description_prompt.txt")) as file:  # promp template
            project_description_prompt = file.read() 
        with open(Path(CUR_DIR, "prompts", "lead_gen","job_posting.json")) as file:
            job_posting_str = json.dumps(json.loads(file.read()), indent=2)

        self.project_description_template = Template(project_description_prompt)
        self.job_posting_str = job_posting_str
        self.context_length = vars.CONTEXT_WINDOW
        llama_debug = LlamaDebugHandler(print_trace_on_end=True)
        callback_handler = OpenInferenceCallbackHandler()
        self.callback_manager = CallbackManager([llama_debug, callback_handler])
        self.embed_model = HuggingFaceEmbedding(model_name=vars.EMBEDDING_MODEL)
        self.llm = OpenAI(model="gpt-4")
        self.service_context = ServiceContext.from_defaults(llm=self.llm)
        self.vector_store: LeadGenVectorStore = get_vector_store()
        _logger.info("Response Synthesizer initilized")

    def _create_nodes(self, qa_pairs):
        nodes = []
        for question, answer in qa_pairs.items():
            node_text = f"Sub question: {question}\nResponse: {answer}"
            nodes.append(NodeWithScore(node=TextNode(text=node_text)))
        return nodes

    # update parameters
    def _create_instance(self):
        prompt_template = PromptTemplate(
            self.lead_prompt_template, prompt_type=PromptType.QUESTION_ANSWER
        )
        self.summarizer = get_response_synthesizer(
            response_mode="no_text",
            text_qa_template=prompt_template,
        )
        nodes = []
        for name, retriever in self.vector_store.retrievers.items():
            nodes.append(retriever["retriever"].vector_retriever.retrieve())
         
        streamer = self.synthesize(
            self.query_str,
            nodes
        )
        return streamer
    

    def _create_job_description_instance(self):
        self.summarizer = get_response_synthesizer(
            response_mode="simple_summarize",
            service_context=self.service_context
        )
         
        streamer = self.synthesize(
            self.query_str,
            []
        )
        return streamer


    def initialize_generate_job_desciption(self, query):
        self.query_str = self.project_description_template.substitute(
            project_requirement=query,
            json_output_str=self.job_posting_str
        )
        

        return self._create_job_description_instance()

    def synthesize(self, query, nodes):
        _logger.info(f"Synthesizing answer")
        if len(nodes):
            response = self.summarizer.synthesize(
                query=query,
                nodes=nodes
            ).response
            
        else:
            response = self.llm.complete(query).text
            print(response)

        return response
