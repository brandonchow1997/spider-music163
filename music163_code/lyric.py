import requests
import time
import random

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/69.0.3497.12 Safari/537.36 '
}


def get_json(id):
    api = 'http://music.163.com/api/song/lyric?os=pc&id=%s&lv=-1&kv=-1&tv=-1' % id
    # print(api)
    response = requests.get(api, headers=header)
    return response.json()


def parse_json(data):
    lyric = data['lrc']['lyric']
    print(lyric)


def lyric(list_id, list_name):
    for i, id in enumerate(list_id):
        # print(id)
        print('||'*20)
        print('正在获取《%s》 的歌词...' % list_name[i])
        time.sleep(random.randint(0, 5))
        json = get_json(id)
        parse_json(json)