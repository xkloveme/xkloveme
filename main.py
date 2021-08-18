#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pathlib
import requests
import re
import datetime
import bs4
import tools
from bs4 import BeautifulSoup
import urllib

root = pathlib.Path(__file__).parent.resolve()


class Source (object):

    def __init__(self):
        self.T = tools.Tools()

    def getSource(self):
        header = {
      "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
        Imgjson = requests.get('https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=ZH-CN?utm_source=cyhour.com',
                    headers=header).json()
        # 正则表达式寻找图片URL并尝试将之更改为高分辨率图片地址
        img_uhd = Imgjson["images"][0]['url'].replace('1920x1080', 'UHD')
        img_url = "https://cn.bing.com"+img_uhd
        return img_url


if __name__ == '__main__':
    obj = Source()
    urllib.request.urlretrieve(obj.getSource(),root / ('img/'+str(datetime.date.today())+'.png'))
    img = '[![每日壁纸](' + obj.getSource() + ')](https://www.jixiaokang.com)'
    readme = root / "README.md"
    readme_contents = open(readme, 'w')
    md = "\n".join(
        [
          '[![xkloveme](https://raw.githubusercontent.com/xkloveme/xkloveme/master/logo.svg)](https://www.jixiaokang.com)',
          '[![forthebadge](https://forthebadge.com/images/badges/ages-20-30.svg)](https://www.jixiaokang.com)  '
          '[![forthebadge](https://forthebadge.com/images/badges/for-you.svg)](https://www.jixiaokang.com)  '
          '[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.jixiaokang.com)',
          '[![xkloveme](https://raw.githubusercontent.com/xkloveme/xkloveme/master/slogan.svg)](https://www.jixiaokang.com)',
          "# 每日壁纸",
          img,
          '# 推荐链接🔗',
          '> [项目说明](https://github.com/xkloveme/xkloveme/blob/master/PROJECT.md)如果想展示您的主页🔗请`pr`,如有喜欢请关注\n',
        ]
    )
    link = root / "LINK.md"
    link_contents = open(link, 'r')
    link_list = link_contents.readlines()
    readme_contents.write(md)
    readme_contents.writelines(link_list)
    readme_contents.close()