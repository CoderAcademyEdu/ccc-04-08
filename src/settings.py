import os

class Config(object):
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024 #16MB
    
    @property
    def UPLOAD_FOLDER(self):
        value = os.environ.get("UPLOAD_FOLDER")

        if not value:
            value = "uploads"

        return value

app_config = Config()