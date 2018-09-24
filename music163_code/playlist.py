import requests

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/69.0.3497.12 Safari/537.36 '
}


def get_playlist(url):
    params = {
        'params': 'ahdAFr5QFI1WpopideHPfAtQbUMoQGLVCarYZg4DIn52IeSH9YparE936I8knQPMUBsvLeeR5z2b1uYVBFiBceq1NsJHdWXfmeMDivQH3tD9Vv/tKggsP/s23qOlvBl75IZdXNNiV4jwAOtST2nXGUuEnR5ckIFkOMSK/Lit9larw7ulZCT23D/7J8NryKdJ',
        'encSecKey': '653f9acfc49847bf149b4cc34cea052f5b3a502beae3ea871d7ea062cdb4c7b2f65c6652cf9e16bd63a4ac391fa162884de3f4760237c27fd73d74f960ef1d6e30b531b09c03a036f6cd6b6fdfe52ba274f07e016c76446eda20dd8bcca62802b6d5a9e10de31dd250ec911f48d5f5e8eb1527ffab5c89a025811773f5905f05'
    }
    response = requests.post(url, headers=header, params=params)
    return response.json()


def parse_playlist(data):
    playlists = data['playlist']
    print('='*80)
    idlist = []
    namelist = []
    print('---- 全部歌单 ----')
    print('歌单ID', '\t|', '歌单名', '\t|', '播放次数', '\t|', '歌曲数量', '\t|', '创建人')
    for playlist in playlists:
        list_id = playlist['id']
        list_name = playlist['name']
        playCount = playlist['playCount']
        trackCount = playlist['trackCount']
        creator = playlist['creator']['nickname']
        print(list_id, '|', list_name, '|', playCount, '\t|', trackCount, '|', creator)
        idlist.append(list_id)
        namelist.append(list_name)
    return idlist, namelist


def playlist(url_playlist):
    json_playlist = get_playlist(url_playlist)
    return parse_playlist(json_playlist)