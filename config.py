import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    API_HASH = os.environ.get("API_HASH", "")
    API_ID = os.environ.get("API_ID", "")   