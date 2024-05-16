import csv
from pathlib import Path

from llama_index import VectorStoreIndex, StorageContext, SimpleDirectoryReader
from llama_index.schema import Node
from llama_index.node_parser import SimpleNodeParser
from framework.vector_store import VectorRetriever
from variables import CUR_DIR
from storage import Storage


def parse_nodes():
    rag_path = Path(CUR_DIR, "temp", "Piston")
    node_parser = SimpleNodeParser.from_defaults(chunk_size=256, chunk_overlap=20)
    documents = SimpleDirectoryReader(rag_path, required_exts=['.txt', '.pdf', '.docx', '.csv'], recursive=True).load_data()
    print(len(documents))
    
    nodes = node_parser.get_nodes_from_documents(documents)
    return nodes


class BasicVectorStore(VectorRetriever):

    def __init__(self, store_type="pg_vector"):
        super().__init__(store_type)
        # note: only used with the AutoRetriever, which is currently disabled

    def load_vector_retriever(self):
        if not self.index:
            # todo currently we just create and index if there is no table; we will want to recreate if count of rows
            #  are different than number of principles in our data
            nodes = parse_nodes()
            print(len(nodes))
            if not self.vector_store.check_embeddings(len(nodes)):
                storage_context = StorageContext.from_defaults(vector_store=self.vector_store.vector_store)
                self.index = VectorStoreIndex(nodes, storage_context=storage_context)
            else:
                self.index_from_vector_store()
            self.set_vector_retriever()


_store = BasicVectorStore()


def initialize():
    print("aqui")
    _store.load_vector_retriever()


def get_vector_store():
    _store.load_vector_retriever()
    return _store

if __name__ == '__main__':
    initialize()