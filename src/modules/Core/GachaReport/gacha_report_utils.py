import os
import re
from urllib import parse

from ...Scripts.Utils import log_recorder as log

GAME_LOG_PATH = os.environ["userprofile"] + '/AppData/LocalLow/miHoYo/崩坏：星穹铁道/Player.log'


def getDefaultGameDataPath():
    if not os.path.exists(GAME_LOG_PATH):
        log.infoWrite(f"[GachaReport.utils] Game Path not found")
        return 0, "Game Log Not found"
    with open(GAME_LOG_PATH, 'r', encoding='utf-8') as f:
        logFile = f.read()
    match = re.match(r'Loading player data from (.*)StarRail_Data.*', logFile)
    game_path = match.group(1) if match else None
    log.infoWrite(f"[GachaReport.utils] Game Path get: {game_path}")
    return game_path


def extractAPI(url):
    res = re.findall("https://.+?webview_gacha.+?game_biz=hkrpg_cn", url)
    if res:
        return res[-1]
    else:
        return None


def convertAPI(url):
    if url:
        return "https://api-takumi.mihoyo.com/common/gacha_record/api/getGachaLog?" + url.split("?")[1]
    else:
        return None


def updateAPI(url, gachaType, size, page, end_id):
    apiParameters = dict(parse.parse_qsl(parse.urlparse(url).query))
    apiParameters["size"] = size
    apiParameters["gacha_type"] = gachaType
    apiParameters["page"] = page
    apiParameters["lang"] = "zh-cn"
    apiParameters["end_id"] = end_id
    return f"{str(url).split('?')[0]}?{parse.urlencode(apiParameters)}"
