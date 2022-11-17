# -*- coding = utf-8 -*-
# @Time: 2022/11/11 21:16
import hashlib


def get_md5():
    obj = hashlib.md5()
    obj.update('123123'.encode('utf-8'))
    res = obj.hexdigest()
    print(res)
    # 4297f44b13955235245b2497399d7a93
    # 4297f44b13955235245b2497399d7a93


def main():
    url = ''
    get_md5()


if __name__ == '__main__':
    main()
