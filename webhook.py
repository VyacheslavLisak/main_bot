import requests
import sys

if __name__ == "__main__":
    WEBHOOK_URL = "DISCORD_WEBHOOK_URL"
    json_content = '```'
    first_param = True
    for param in sys.argv:
        if not first_param:
            json_content = json_content + param + ' '
        first_param = False

    json_content = json_content + '```'
    data = {"content":json_content}
    response = requests.post(WEBHOOK_URL, json=data)

    print(response.status_code)