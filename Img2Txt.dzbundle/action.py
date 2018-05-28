# Dropzone Action Info
# Name: Img2Txt
# Description: recognize texts in images(jpg/png/bmp) using baidu OCR API
# Handles: Files
# Creator: waysup
# URL: https://qnmlgb.app
# Events: Clicked, Dragged
# KeyModifiers: Command, Option, Control, Shift
# SkipConfig: No
# RunsSandboxed: Yes
# Version: 1.0
# MinDropzoneVersion: 3.0
# PythonPath: /usr/local/bin/python3
# OptionsNIB: ExtendedLogin

import os
import json
import time

access_token = None


def dragged():
    if token_outdated():
        update_access_token()

    dz.begin('开始识别 ' + str(len(items)) + ' 张图.')
    dz.determinate(True)
    dz.percent(10)
    cnt = 0
    ret_texts = ''
    for item in items:
        cnt += 1
        if len(items) / 2 == cnt:
            dz.percent(50)
        ret_texts += get_text(item) + '\n\n'
    dz.percent(100)
    dz.finish('完成识别 ' + str(len(items)) + ' 张图.')
    dz.text(ret_texts[:-1])


def get_text(img_path):
    # get access_token
    global access_token
    if access_token is None:
        access_token = os.environ['access_token']

    CMD = 'base64 -i ' + img_path + ' | curl -s --data-urlencode image@- ' + \
        'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic\?access_token\=' + \
        access_token + ' -H "Content-Type: application/x-www-form-urlencoded"'

    pp = os.popen(CMD)
    ret_dict = json.loads(pp.read())
    pp.close()

    ret_str = ''
    for lines in ret_dict['words_result']:
        for words in lines.values():
            ret_str += words + '\n'

    return ret_str[:-1]


def token_outdated():
    try:
        last_update = os.environ['update_time']
    except KeyError:
        return True
    else:
        # update token every 25 days(2160000 sec)
        PERIOD = 2160000
        return time.time() - float(last_update) > PERIOD


def update_access_token():
    print("It's time to update the access_token...")

    AUTH_URL = 'https://aip.baidubce.com/oauth/2.0/token' + \
    '\?grant_type\=client_credentials'

    client_id = os.environ['username']
    client_secret = os.environ['password']

    p = os.popen('/usr/bin/curl -s ' + AUTH_URL + '\&client_id\=' +
                 client_id + '\&client_secret\=' + client_secret)
    x = p.read()
    p.close()

    global access_token
    access_token = json.loads(x)['access_token']

    dz.save_value('access_token', access_token)
    dz.save_value('update_time', time.time())

    print("access_token update success...")


def clicked():
    dz.finish("Click not supported yet!")
    dz.url(False)
