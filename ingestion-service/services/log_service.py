from models.log_model import Log
from repositories.log_repository import LogRepository


class LogService():
    @staticmethod
    def create_log(service, level, message):
        log = Log(service, level, message)
        return LogRepository.save(log.to_dict())
