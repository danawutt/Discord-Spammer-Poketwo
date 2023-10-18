from webserver import keep_alive
import requests

channelID = 1068830747307282493
headers = {
    "authorization":
    MTE1NzYzODY4ODcwNTEwNTk2MA.G3cPmP.PuuB-70TpopACBfrqdCNCgnm9xm-ftpXbmDaww
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
