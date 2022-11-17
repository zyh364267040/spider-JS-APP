# -*- coding = utf-8 -*-
# @Time: 2022/8/17 22:21
import execjs
import os


os.environ["NODE_PATH"] = "/usr/local/lib/node_modules/"


def learn():
    with open('learn_js.js', 'r', encoding='utf-8') as f:
        js = f.read()

    js = execjs.compile(js)
    res = js.call('func', '123')

    print(res)


def sign2_run():
    url = 'https://www.toutiao.com/hot-event/hot-board/?origin=toutiao_pc'
    with open('sign2.js', 'r', encoding='utf-8') as f:
        js = f.read()

    js = execjs.compile(js)
    res = js.call('get_sign', url)
    print(res)


def main():
    sign2_run()


if __name__ == '__main__':
    main()
