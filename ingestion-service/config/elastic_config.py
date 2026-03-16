from elasticsearch import Elasticsearch
import os
from dotenv import load_dotenv

load_dotenv()

ELASTIC_HOST= os.getenv("ELASTIC_HOST", "http://localhost:9200")
ELASTIC_USER = os.getenv("ELASTIC_USER", "elastic")
ELASTIC_PASSWORD = os.getenv("ELASTIC_PASSWORD")

es_client = Elasticsearch(
    ELASTIC_HOST,
    basic_auth=(ELASTIC_USER, ELASTIC_PASSWORD)
)