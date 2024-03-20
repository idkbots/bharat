import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
load_dotenv()



#Basic-Setup
OWNER_ID = int(getenv("OWNER_ID", "5032100535"))
LOGGER_ID = int(getenv("LOGGER_ID", "-1001998462941"))

#Bot-Setup
BOT_TOKEN = getenv("BOT_TOKEN", "6310977936:AAF35Z2OH4KwbGpHpaJzrY2De6komPrzag0")

#MongoDB-Setup
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Allen1:Allen1@cluster0.vapqij4.mongodb.net/?retryWrites=true&w=majority")

#Assistant-Setup
API_ID = int(getenv("API_ID", "19825563")
API_HASH = getenv("API_HASH", "8557e95e0dd37df02d12406639157050")

STRING1 = getenv("STRING_SESSION", "AQDDhPvORFqUxNuigB5fhy0Jl_fsNrz3o958sJabszqz9GD6WivLYAGyaSmqQxhX1_JG0-8-r-zszunGhZ7g2_8rm-WzFqnTupy6zdn93JjSDRzsfJPMFD-Z0gOYDMb3KdKFo3Q7bi5s-A1-L5gbiID5LMoh7I4DPJP1utpCLmD9bZTymVcJAMkhnuVT7AQ09XAQDRzLOcTjINXVRF6sLj9qf4dN4aPtg2BVgoJraBOPklim70RyC6U8O5txu2ZMzLXJUesUApYQR1D1Bj8e6_tpRlaidwZJGalb597PL9S3sk94Hjuz6wlevsF428VsCxh_7DiCVIPkeWkY35T9cNeHcr5YsgA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))



SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/StudyXBots")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/StudyxSupport")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv("UPSTREAM_REPO","https://github.com/idkbots/Bharat")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)  # Fill this variable if your upstream repository is private

#Limits
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 250))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 100))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/98496930a33e016edde30.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/98496930a33e016edde30.jpg."
)
STATS_IMG_URL = "https://graph.org/file/98496930a33e016edde30.jpg"
PLAYLIST_IMG_URL = "https://i.pinimg.com/736x/ea/e1/e3/eae1e38f90928b64acf67a85462667ea.jpg"
TELEGRAM_AUDIO_URL = "https://i.pinimg.com/736x/71/e8/4b/71e84b0169197bece76520e3979cf899.jpg"
TELEGRAM_VIDEO_URL = "https://i.pinimg.com/736x/71/e8/4b/71e84b0169197bece76520e3979cf899.jpg"
STREAM_IMG_URL = "https://i.pinimg.com/originals/03/e8/db/03e8db879f8e9a0a83514b135260e182.jpg"
YOUTUBE_IMG_URL = "https://i.pinimg.com/originals/d0/30/eb/d030ebe0b24de823dda499ac37301eb2.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://w0.peakpx.com/wallpaper/407/1022/HD-wallpaper-wets-female-wet-brown-eyes-sexy-cute-short-hair-girl-anime-hot-anime-girl-black-hair-night.jpg"
SPOTIFY_ALBUM_IMG_URL = SPOTIFY_ARTIST_IMG_URL
SPOTIFY_PLAYLIST_IMG_URL = SPOTIFY_ARTIST_IMG_URL


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:6000000"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
