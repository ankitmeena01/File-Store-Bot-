# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

**My Name:** [Thani Oruvan25's Files Store Bot](https://t.me/{BOT_USERNAME})

**Version** - 1.0

**Developer:** @ThaniOruvan25 

👥 **Support Group:** [𝑇𝑎𝑚𝑖𝑙 𝑆𝑒𝑟𝑖𝑎𝑙𝑠 𝐷𝑖𝑠𝑐𝑢𝑠𝑠𝑖𝑜𝑛𝑠](https://t.me/Tamil_Seriala)

📢 **Updates Channel:** [𝑻𝒈 𝑻𝒂𝒎𝒊𝒍 𝑺𝒆𝒓𝒊𝒂𝒍𝒔](https://t.me/TGTamilSerials)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @ThaniOruvan25
 
One Of Fast Video Uploader Admin😇. His First Open Bot Is This [Thani Oruvan25's Files Store Bot](https://t.me/{BOT_USERNAME}). 

Join @TamilSeriala For Serial Videos,🥰

Join @TrueOTTPlatform2 For Movies 🤩
"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is [Thani Oruvan25's Files Store Bot](https://t.me/{BOT_USERNAME})

Here All '#TO UPLOADS💛' Video Link Will Be Send By Me. Thanks For Using Me. 💗💗
"""
