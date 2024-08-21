from typing import Dict, List, Union

import numpy as np
from elasticsearch import Elasticsearch

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def search(*args, **kwargs) -> List[Dict]:
    connection_string = kwargs.get('connection_string', 'http://localhost:9200')

    index_name = "documents_20240821_4438"

    query = "When is the next cohort?"
    course = "llm_zoomcamp"

    search_query = {
        "size": 5,
        "query": {
            "bool": {
                "must": {
                    "multi_match": {
                        "query": query,
                        "fields": ["question^3", "text", "section"],
                        "type": "best_fields"
                    }
                },
            }
        }
    }

    es_client = Elasticsearch(connection_string)

    response = es_client.search(
        index=index_name,
        body=search_query
    )

    result_docs = []
    
    for hit in response['hits']['hits']:
        result_docs.append(hit['_source'])
    
    print(result_docs)
    return result_docs


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'