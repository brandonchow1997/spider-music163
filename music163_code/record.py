import requests


header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/69.0.3497.12 Safari/537.36 '
}


def get_record(url):

    params = {
        'params': 'USvHovPxlOzESu8LC/huUamSLtJyVv7IPq3cT3KRw0KKlCXhXJbEDTR2nL6krXDCNFCIsitUPgb/5wwWgfL20IfmM2H7'
                  '/tKQFAta3ZiKR0WI6iqCtVC1z+Za4f1RkgL+Jcz6ubQ8cPUgOKmHeWEg6XvR+Llxk+bcAn/Tjbgk62CNNle/o'
                  '+SIN655oG5Z24V5',
        'encSecKey': 'b1f7779f38d8aa4f09d965ee446dbb76f139dde4a6fddfec4618f91439c7e03ec7f215bbda36a76f33fc44b1042cbef07867c52395ff891ad56aaf13be1088e7e618da0ce18fb2501a06d1a8bec5aa0d841c34a0e9bab872f82b76b59da25ddc8fc695d6fcd3ac43f5cde8661074895028a4456c75daaa91e7b61f0d9aa72248'
    }
    response = requests.post(url, headers=header, params=params)
    return response.json()


def parse_record(data):
    allsongs = data['allData']
    weeksongs = data['weekData']
    print('---- 总听歌排行 ----')
    print('歌名', '\t|', '歌手', '\t|', '热度', '\t|', '播放次数')
    for song in allsongs:
        score = song['score']
        name = song['song']['name']
        singer = song['song']['ar'][0]['name']
        playTime = song['song']['song']['playTime']
        print(name, '\t|', singer, '\t|', score, '\t|', playTime)

    print('='*80)

    print('---- 周听歌排行 ----')
    print('歌名', '\t|', '歌手', '\t|', '热度', '\t|', '播放次数')
    for song in weeksongs:
        score = song['score']
        name = song['song']['name']
        singer = song['song']['ar'][0]['name']
        playTime = song['song']['song']['playTime']
        print(name, '\t|', singer, '\t|', score, '\t|', playTime)


def record(url_record):
    json_record = get_record(url_record)
    parse_record(json_record)