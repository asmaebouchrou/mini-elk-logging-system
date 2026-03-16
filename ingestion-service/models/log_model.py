from datetime import datetime

class Log:
    def __init__(self, service, level, message):
        self.service = service
        self.level = level
        self.message = message
        self.timestap = datetime.utcnow().isoformat()

    def to_dict(self):
        return {
            "service": self.service,
            "level": self.level,
            "message": self.message,
            "timestap": self.timestap
        }
