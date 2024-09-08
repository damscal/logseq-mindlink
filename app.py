"""
Enabling Diagnostic Logging
This code configures the logging level to `INFO`, which will output messages that assist in monitoring the application’s operational flow.
"""
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.readers.file import (
    MarkdownReader
)



parser = MarkdownReader()
file_extractor = {".md": parser}

def load_documents(path):
    return SimpleDirectoryReader(
    path, file_extractor=file_extractor
    ).load_data()

documents = load_documents("/logseq/journals")+load_documents("/logseq/pages")


#print(help(VectorStoreIndex))


from dotenv import load_dotenv
load_dotenv()
import os
cohere_api_key = os.environ["COHERE_API_KEY"]
#from langchain_cohere import CohereEmbeddings, ChatCohere
from llama_index.embeddings.cohere import CohereEmbedding

#help(CohereEmbedding)
embed_model = CohereEmbedding(
    api_key=cohere_api_key,
    model_name="embed-multilingual-v3.0",
)


from llama_index.llms.cohere import Cohere
llm = Cohere(
    api_key=cohere_api_key,
    temperature=0,
    model="command-r",
    max_tokens=512
)

from llama_index.core import Settings
Settings.llm = llm
Settings.embed_model = embed_model

index = VectorStoreIndex.from_documents(documents)


query_engine = index.as_query_engine() #no history preserved
response = query_engine.query("In che data ho incontrato il geometra Lovecchio?")
print(response)

quit()


