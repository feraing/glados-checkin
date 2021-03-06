# -*- coding:utf-8 -*-
#

import json
import os
import requests

sever = 'off'
sckey = 'off'
cookie = os.environ["COOKIE"]


def start():
    url = "https://glados.rocks/api/user/checkin"
    url2 = "https://glados.rocks/api/user/status"
    referer = 'https://glados.rocks/console/checkin'
    checkin = requests.post(url, headers={'cookie': cookie, 'referer': referer})
    state = requests.get(url2, headers={'cookie': cookie, 'referer': referer})

    if 'message' in checkin.text:
        print(checkin.json())
        mess = checkin.json()['message']
        time = state.json()['data']['leftDays']
        time = time.split('.')[0]
        print(time)
        if sever == 'on':
            requests.get('https://sc.ftqq.com/' + sckey + '.send?text='+mess+'，you have '+time+' days left')
    else:
        requests.get('https://sc.ftqq.com/' + sckey + '.send?text=cookie过期')


def main_handler(event, context):
    return start()


if __name__ == '__main__':
    start()






