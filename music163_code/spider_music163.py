import playlist
import record
import songs
import time
from tqdm import tqdm
# from retrying import retry
import random

if __name__ == '__main__':
    # -------record---------------------
    url_record = 'https://music.163.com/weapi/v1/play/record?csrf_token='
    record.record(url_record)
    # ----------------------------------

    # -------playlist-------------------
    url_playlist = 'https://music.163.com/weapi/user/playlist?csrf_token='
    # 返回两个列表
    idlist, namelist = playlist.playlist(url_playlist)
    # ----------------------------------
    browser = songs.chromedriver()
    # -------songs----------------------
    pbar = tqdm(idlist)
    for i, id in enumerate(pbar):
        pbar.set_description("Processing Topic:%s..." % namelist[i])
        songs.songs(browser, id)
        time.sleep(random.randint(0, 2))
    # ----------------------------------
