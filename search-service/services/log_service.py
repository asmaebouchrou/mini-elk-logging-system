from repositories.log_repository import LogRepository


class LogService:

    @staticmethod
    def get_logs(service=None, level=None):
        return LogRepository.search(service, level)
