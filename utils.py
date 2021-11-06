import os
import time


class Var(object):

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    API_ID = int(os.environ.get("API_ID", 12345))

    API_HASH = os.environ.get("API_HASH", "")

    BANNED_USERS = set(
        int(x) for x in os.environ.get(
            "BANNED_USERS", "").split())

    BOT_START_TIME = time.time()

    # Genius Api From Here : https://genius.com/api-clients
    API = os.environ.get("GENIUS_API", None)

    # buttons
    PAGENUM = int(os.environ.get("PAGENUM", 20))
