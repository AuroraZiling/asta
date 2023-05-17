UIGF_GACHATYPE = {"2": "2", "1": "1", "11": "11", "12": "12"}
UIGF_VERSION = "Unknown UIGF Version"
UIGF_DATA_MODEL = {"info": {"uid": "", "lang": "zh-cn", "export_time": ""}, "list": []}
GACHATYPE = {"始发跃迁": "2", "群星跃迁": "1", "角色活动跃迁": "11", "光锥活动跃迁": "12"}

SOFTWARE_ANNOUNCEMENT_URL = "https://raw.staticdn.net/AuroraZiling/asta.Metadata/main/announcement.txt"

CHARACTER_URL = "https://wiki.biligame.com/sr/%E8%A7%92%E8%89%B2%E7%AD%9B%E9%80%89"
PERMANENT_CHARACTER_URL = "https://raw.staticdn.net/AuroraZiling/asta.Metadata/main/metadata.json"
WEAPON_URL = "https://wiki.biligame.com/sr/%E5%85%89%E9%94%A5%E4%B8%80%E8%A7%88"
UIGF_ITEM_ID_URL = "https://api.uigf.org/dict/starrail/{lang}.json"
UIGF_MD5_URL = "https://api.uigf.org/dict/starrail/md5.json"

COLOR_MAPPING = {"3": "#1E90FF", "4": "#7B68EE", "5": "#FFA500", "X": "#FF0000"}

FONT_MAPPING = ["StarRailNeue-Sans-Regular.otf", "StarRailNeue-Serif-Regular.otf"]
FONT_NAME_MAPPING = ["Star Rail Neue Sans-", "Star Rail Neue Serif-"]

GITHUB_RELEASE_URL = "https://api.github.com/repos/AuroraZiling/star-rail-asta/releases/latest"

UPDATE_SCRIPT_MODEL = """
echo "DON'T CLOSE THIS WINDOW"
powershell -command \"Start-Sleep -s 3\"
powershell -command \"Get-childitem -Path .. -exclude *.json,*.zip,*.bat,temp -Recurse | Remove-Item -Force -Recurse\"
powershell -command \"Expand-Archive -Path .\\{filename} -DestinationPath ..\\ -Force\"
powershell -command \"Remove-Item -Path .\\{filename}\"
cd ../.
start .\\"Asta.exe\"
powershell -command \"Remove-Item -Path .\\temp\\update.bat\"
exit
"""
