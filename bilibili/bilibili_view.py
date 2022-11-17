# -*- coding = utf-8 -*-
# @Time: 2022/7/16 下午11:45
import requests
import re
import json
import time
import random
import math
import uuid
from bilibili_api import video
import asyncio


async def run():
    v = video.Video(bvid='BV11d4y1D7fJ')
    info = await v.get_info()
    json.dumps(info)
    return info['stat']['view']


class BiLiBiLi(object):
    def __init__(self):
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }
        print('生成session...')
        self.session = requests.Session()
        self.session.headers.update(headers)

        self.aid = ''
        self.cid = ''

        self.url = 'https://www.bilibili.com/video/BV11d4y1D7fJ'
        self.bvid = self.url.rsplit('/')[-1]

    def get_aid_cid_buvid3(self):
        print('开始获取aid、cid和buvid3...')
        url = 'https://www.bilibili.com/video/BV11d4y1D7fJ'
        # res = requests.get(url)
        res = self.session.get(url)

        buvid3 = res.cookies.get_dict()['buvid3']
        self.session.cookies.set('buvid3', buvid3)
        print(f'buvid3: {buvid3}')
        self.session.cookies.set('buvid3', buvid3)

        id_list = re.findall(r'window.__INITIAL_STATE__=(.*);\(function\(\){var', res.text)

        id_dic = json.loads(id_list[0])
        self.aid = id_dic['aid']
        print(f'aid: {self.aid}')

        self.cid = id_dic['videoData']['cid']
        print(f'cid: {self.cid}')

    def get_b_lsid(self):
        print('开始获取b_lsid...')
        t = int(time.time()*1000)
        t = hex(t)[2:].upper()

        a = ''
        for i in range(8):
            a += hex(math.ceil(16*random.uniform(0, 1)))[2:].upper()

        data = a.rjust(8, '0')
        b_lsid = f'{data}_{t}'
        self.session.cookies.set('b_lsid', b_lsid)
        print(f'b_lsid: {b_lsid}')

    def get_uuid(self):
        print('开始获取_uuid...')
        uuid1 = str(uuid.uuid4()).upper()

        uuid2 = int(time.time() * 1000 % 1e5)
        uuid2 = str(uuid2).rjust(5, '0')

        _uuid = f'{uuid1}{uuid2}infoc'
        self.session.cookies.set('_uuid', _uuid)
        print(f'_uuid: {_uuid}')

    def get_buvid4(self):
        print('开始获取buvid4...')
        url = 'https://api.bilibili.com/x/frontend/finger/spi'
        res = self.session.get(url)
        res_dict = json.loads(res.text)
        buvid4 = res_dict['data']['b_4']
        print(f'buvid4: {buvid4}')
        self.session.cookies.set('buvid4', buvid4)

    def send_post_h5(self):
        form_data = {
            'aid': self.aid,
            'cid': self.cid,
            'bvid': self.bvid,
            'part': 1,
            'mid': 0,
            'lv': 0,
            'ftime': int(time.time()),
            'stime': int(time.time()),
            'jsonp': 'jsonp',
            'type': 3,
            'sub_type': 0,
            'from_spmid': '',
            'auto_continued_play': 0,
            'refer_url': '',
            'bsource': '',
            'spmid': ''
        }

        self.session.cookies.set('b_nut', str(int(time.time())))
        self.session.cookies.set('CURRENT_FNVAL	', '4048')

        h5_url = 'https://api.bilibili.com/x/click-interface/click/web/h5'
        res = self.session.post(h5_url, data=form_data)
        print(res.status_code)

    def main(self):
        # 1.获取aid,cid和buvid3
        self.get_aid_cid_buvid3()

        # 2.获取b_lsid
        self.get_b_lsid()

        # 3.获取_uuid
        self.get_uuid()

        # 4.获取buvid4
        self.get_buvid4()

        # 5.向h5发送post请求
        self.send_post_h5()


if __name__ == '__main__':
    a = r"""
                                   //
             \\                   //
              \\                 //
        ##DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD##
        ## DDDDDDDDDDDDDDDDDDDDDDDDDDDDDD ##   ________   ___   ___        ___   ________   ___   ___        ___
        ## hh                          hh ##   |\   __  \ |\  \ |\  \      |\  \ |\   __  \ |\  \ |\  \      |\  \
        ## hh     //           \\      hh ##   \ \  \|\ /_\ \  \\ \  \     \ \  \\ \  \|\ /_\ \  \\ \  \     \ \  \
        ## hh    //             \\     hh ##    \ \   __  \\ \  \\ \  \     \ \  \\ \   __  \\ \  \\ \  \     \ \  \
        ## hh                          hh ##     \ \  \|\  \\ \  \\ \  \____ \ \  \\ \  \|\  \\ \  \\ \  \____ \ \  \
        ## hh         wwwwww           hh ##      \ \_______\\ \__\\ \_______\\ \__\\ \_______\\ \__\\ \_______\\ \__\
        ## hh                          hh ##       \|_______| \|__| \|_______| \|__| \|_______| \|__| \|_______| \|__|
        ## MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM ##
        ##MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM##                                   Release @bilibili/comment-pc-vue@2.0.31
               \/                  \/                                Powered by @jinkela/webpack-builder-plugin@1.1.16
    """
    print(a)
    main = ''

    for i in range(20):
        bilibili = BiLiBiLi()
        bilibili.main()

        view_count = asyncio.run(run())
        print(f'当前播放量{view_count}')
        time.sleep(10)
