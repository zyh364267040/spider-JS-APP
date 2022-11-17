from bilibili_api import video
import asyncio
import json


async def main():
    v = video.Video(bvid='BV11d4y1D7fJ')
    info = await v.get_info()
    json.dumps(info)
    return info['stat']['view']


def read_view_count():
    view_count = asyncio.run(main())
    return view_count


if __name__ == '__main__':
    view_count = read_view_count()
    print(view_count)
