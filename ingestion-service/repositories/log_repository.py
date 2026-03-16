from config.elastic_config import es_client

INDEX_NAME= "logs"

class LogRepository:

    @staticmethod
    def save(log_data):
        response = es_client.index(
            index=INDEX_NAME,
            document=log_data
        )
        return response.body
