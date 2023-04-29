import os
import requests


def send_message(channel, message):
    token = os.environ['SLACK_TOKEN']

    headers = {
        'Authorization': f'Bearer {token}'
    }

    data = {
        'channel': f'#{channel}',
        'text': message
    }

    url = 'https://slack.com/api/chat.postMessage'
    return requests.post(url, headers=headers, data=data)


if __name__ == '__main__':
    response = send_message('channel_name', 'Hello, slack!')
    print(response.status_code)

