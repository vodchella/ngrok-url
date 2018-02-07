#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests

if __name__ == '__main__':
    try:
        req = requests.get('http://127.0.0.1:4040/status')
        if req.status_code == 200:
            for line in req.text.split('\n'):
                line = line.strip()
                if line[:28] == 'window.common = JSON.parse("':
                    json_text = line[28:-3].replace(r'\"', '"')
                    json_object = json.loads(json_text)
                    print(json_object['Session']['Tunnels']['command_line']['URL'])
    except:
        pass
