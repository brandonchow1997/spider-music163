# 接入selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree
# import time


def chromedriver():
    # -----浏览器初始化
    print('=' * 40)
    print('正在初始化无头Chrome浏览器...')
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
    chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    # 添加代理 proxy
    # chrome_options.add_argument('--proxy-server=http://' + proxy)
    browser = webdriver.Chrome(chrome_options=chrome_options)
    print('浏览器初始化完毕')
    # print('=' * 20)
    return browser
    # ------------------


def get_list(browser, id):
    url = 'https://music.163.com/#/playlist?id={id}'.format(id=id)
    browser.get(url)
    browser.switch_to.frame('g_iframe')
    # time.sleep(3)
    html = browser.page_source
    return html


def parse_list(html):
    data = etree.HTML(html)
    items = data.xpath('//*[@class="j-flag"]/table/tbody/tr')
    # print(html)
    print('='*40)
    print('歌名', '\t|', '歌手', '\t|', '专辑')
    for item in items:
        titlelist = item.xpath('./td[2]/div/div/div/span/a/b/@title')
        title = "".join(titlelist)
        singerlist = item.xpath('./td[4]/div/@title')
        singer = "".join(singerlist)
        albumlist = item.xpath('./td[5]/div/a/@title')
        album = "".join(albumlist)
        print(title, '\t|', singer, '\t|', album)
    print('='*80)


def songs(browser, id):
    html = get_list(browser, id)
    parse_list(html)