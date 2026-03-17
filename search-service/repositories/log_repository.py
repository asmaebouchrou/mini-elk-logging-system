from config.elastic_config import es_client

INDEX_NAME = "logs"


class LogRepository():
    @staticmethod
    def search(service=None, level=None):

        query = {
            "bool": {
                "must": []
            }
        }

        if service:
            query["bool"]["must"].append({
                "match": {
                    "service": service
                }
            })

        if level:
            query["bool"]["must"].append({
                "match": {
                    "level": level
                }
            })
        response = es_client.search(
            index=INDEX_NAME,
            query=query
        )
        return response.body
