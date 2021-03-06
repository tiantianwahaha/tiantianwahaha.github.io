# 爬取4今日热点事件排行榜
import requests
import json
import re
from bs4 import BeautifulSoup

require = 9


def get_data_baidu(url, headers):
    r = requests.get(url, headers=headers)
    r.encoding = r.apparent_encoding
    html = r.text

    data = []
    soup = BeautifulSoup(html, 'lxml')
    content = soup.find_all(class_="list-title")
    for i in range(len(content)):
        topic_name = content[i].get_text().strip()
        topic_url = content[i]['href'].strip()
        # print(topic_name, topic_url)
        tmp = "<a href='{}' class='list-group-item list-group-item-action' target='blank'> <span class='float-left text-primary'>{}</span><span class='title'>{}</span> </a>".format(
            topic_url, i+1, topic_name)
        data.append(tmp)
        if (i >= require):
            break
    return data


def get_data_zhihu(url, headers):
    r = requests.get(url, headers=headers)
    r.encoding = r.apparent_encoding
    html = r.text

    data = []
    soup = BeautifulSoup(html, "html.parser")
    hot_data = soup.find('script', id='js-initialData').string
    hot_json = json.loads(hot_data)
    hot_list = hot_json['initialState']['topstory']['hotList']
    print(type(hot_list))
    for i in range(len(hot_list)):
        topic_name = hot_list[i]['target']['titleArea']['text']
        topic_url = hot_list[i]['target']['link']['url']
        print(topic_name, topic_url)
        tmp = "<a href='{}' class='list-group-item list-group-item-action' target='blank'> <span class='float-left text-primary'>{}</span><span class='title'>{}</span> </a>".format(
            topic_url, i+1, topic_name)
        data.append(tmp)
        if (i >= require):
            break
    return data


def get_data_weibo(url, headers):
    r = requests.get(url, headers=headers)
    html = r.text

    data = []
    soup = BeautifulSoup(html, 'lxml')
    urls_titles = soup.select(
        '#pl_top_realtimehot > table > tbody > tr > td.td-02 > a')
    # hotness = soup.select('#pl_top_realtimehot > table > tbody > tr > td.td-02 > span')
    for i in range(len(urls_titles)):
        topic_name = urls_titles[i+1].get_text()
        topic_url = "https://s.weibo.com"+urls_titles[i+1]['href']
        # print(topic_name, topic_url)
        tmp = "<a href='{}' class='list-group-item list-group-item-action' target='blank'> <span class='float-left text-primary'>{}</span><span class='title'>{}</span> </a>".format(
            topic_url, i+1, topic_name)
        data.append(tmp)
        if (i >= require):
            break
    return data


def main():
    url_baidu = 'http://top.baidu.com/buzz?b=1&c=513&fr=topbuzz_b1_c513'
    url_zhihu = 'https://www.zhihu.com/billboard'
    url_weibo = 'https://s.weibo.com/top/summary'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36', 'Cookie': ''}

    baidu = get_data_baidu(url_baidu, headers)
    zhihu = get_data_zhihu(url_zhihu, headers)
    weibo = get_data_weibo(url_weibo, headers)

    result = {"baidu": baidu, "zhihu": zhihu, "weibo": weibo, "hupu": baidu}
    with open("content.json", "w") as f:
        f.write("var data = ")
        f.write(json.dumps(result, indent=4))


if __name__ == '__main__':
    main()
