#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import urllib.error
import ssl
import random

class Tools (object):

    def __init__(self):
        pass

    def getPage(self, url, requestHeader=[], postData={}):
        fakeIp = self.fakeIp()
        requestHeader.append('CLIENT-IP:' + fakeIp)
        requestHeader.append('X-FORWARDED-FOR:' + fakeIp)

        if postData == {}:
            request = urllib.request.Request(url)
        elif isinstance(postData, str):
            request = urllib.request.Request(url, postData)
        else:
            request = urllib.request.Request(
                url, urllib.parse.urlencode(postData).encode('utf-8'))

        for x in requestHeader:
            headerType = x.split(':')[0]
            headerCon = x.replace(headerType + ':', '')
            request.add_header(headerType, headerCon)

        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            response = urllib.request.urlopen(request, context=ctx)
            header = response.headers
            body = response.read().decode('utf-8')
            code = response.code
        except urllib.error.HTTPError as e:
            header = e.headers
            body = e.read().decode('utf-8')
            code = e.code
        except:
            header = ''
            body = ''
            code = 500

        result = {
            'code': code,
            'header': header,
            'body': body
        }

        return result

    def fakeIp (self) :
        fakeIpList = []

        for x in range(0, 4):
            fakeIpList.append(str(int(random.uniform(0, 255))))

        fakeIp = '.'.join(fakeIpList)

        return fakeIp