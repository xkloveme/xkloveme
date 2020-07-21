#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pathlib
import re

import bs4
import tools
from bs4 import BeautifulSoup

root = pathlib.Path(__file__).parent.resolve()


class Source (object):

    def __init__(self):
        self.T = tools.Tools()

    def getSource(self):
        img = ''

        url = 'https://cn.bing.com'
        req = [
            'user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36',
        ]
        res = self.T.getPage(url, req)
        if res['code'] == 200:
            soup = BeautifulSoup(res['body'], 'html.parser')
            img = url + soup.find(id='sh_url').get('value')
            return img


if __name__ == '__main__':
    obj = Source()
    img = '[![每日壁纸](' + obj.getSource() + ')](https://www.jixiaokang.com)'
    readme = root / "README.md"
    readme_contents = open(readme, 'w')
    md = "\n".join(
        [
          '[![xkloveme](https://raw.githubusercontent.com/xkloveme/xkloveme/master/logo.svg)](https://www.jixiaokang.com)',
          '[![forthebadge](https://forthebadge.com/images/badges/ages-20-30.svg)](https://www.jixiaokang.com)'
          '[![forthebadge](https://forthebadge.com/images/badges/for-you.svg)](https://www.jixiaokang.com)'
          '[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.jixiaokang.com)',
          '[![xkloveme](https://raw.githubusercontent.com/xkloveme/xkloveme/master/slogan.svg)](https://www.jixiaokang.com)',
          "# 每日壁纸",
          img,
          '# 推荐链接🔗',
          '> [项目说明](./PROJECT.md)下面为推荐链接🔗,如有喜欢请关注\n',
        ]
    )
    link = root / "link.md"
    link_contents = open(link, 'r')
    link_list = link_contents.readlines()
    readme_contents.write(md)
    readme_contents.writelines(link_list)
    readme_contents.close()
