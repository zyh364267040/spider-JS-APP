# -*- coding = utf-8 -*-
# @Time: 2022/8/7 下午3:57
import requests
import os
import execjs


def main():
    os.environ['NODE_PATH'] = '/usr/local/lib/node_modules'
    print(os.environ['NODE_PATH'])
    url = 'https://www.toutiao.com/api/pc/list/feed?channel_id=3189399007&min_behot_time=0&refresh_count=1&category=pc_profile_channel&client_extra_params=%7B%22short_video_item%22:%22filter%22%7D&aid=24&app_name=toutiao_web'

    with open('sign2.js', 'r', encoding='utf-8') as f:
        js = f.read()

    js = execjs.compile(js)
    signature = js.call('get_sign', url)

    final_url = f'{url}&_signature={signature}'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }

    res = requests.get(final_url, headers=headers)
    print(res.text)


if __name__ == '__main__':
    main()
