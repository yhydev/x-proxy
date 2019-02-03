#!/usr/bin/env python
import base64

proxyre = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{2,4}'
ipre = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
portre = [':\d{2,5}', '\d{2,5}']
prore = ''

urls = ["https://www.my-proxy.com/free-proxy-list-1.html",
"https://www.my-proxy.com/free-proxy-list-2.html",
"https://www.my-proxy.com/free-proxy-list-3.html",
"https://www.my-proxy.com/free-proxy-list-4.html",
"https://www.my-proxy.com/free-proxy-list-5.html",
"https://www.my-proxy.com/free-proxy-list-6.html",
"https://www.my-proxy.com/free-proxy-list-7.html",
"https://www.my-proxy.com/free-proxy-list-8.html",
"https://www.my-proxy.com/free-proxy-list-9.html",
"https://www.my-proxy.com/free-proxy-list-10.html",
"https://www.my-proxy.com/free-elite-proxy.html",
"https://www.my-proxy.com/free-anonymous-proxy.html",
"https://www.my-proxy.com/free-transparent-proxy.html"]

spiderConfig = []





def generateurl():
    urlss = []
    for i in range(1, 3577):
        urlss.append("https://www.xicidaili.com/nn/%s" % i)

    for i in range(1, 725):
        urlss.append("https://www.xicidaili.com/nt/%s" % i)

    for i in range(1, 1591):
        urlss.append("https://www.xicidaili.com/wn/%s" % i)

    for i in range(1, 1938):
        urlss.append("https://www.xicidaili.com/wt/%s" % i)
    return urlss


spiderConfig.append({
    "urls": generateurl(),
    "proxyre": ">\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[\s\S]+?\d{1,5}<",
    "ipre": ipre,
    "portre": [">\d{1,5}<", "\d{1,5}"],
    "prore": "",
})



"""
spiderConfig.append({
    "urls": "http://www.66ip.cn/nmtq.php?getnum=9999",
    "proxyre": proxyre,
    "ipre": ipre,
    "portre": portre,
    "prore": prore  
})
"""

"""

spiderConfig.append({
    "urls": urls,
    "proxyre": proxyre,
    "ipre": ipre,
    "portre": portre,
    "prore" : prore
})

spiderConfig.append({
    "urls": ["https://www.proxy-list.download/api/v0/get?l=en&t=http", "https://www.proxy-list.download/api/v0/get?l=en&t=https"],
    "proxyre": 'IP": "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", "PORT": "\d{1,5}"',
    "ipre": "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
    "portre": ['"\d{1,5}"', "\d{1,5}"],
    "prore": prore
})




spiderConfig.append({
    "urls": "https://free-proxy-list.net/",
    "proxyre": ">\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}</td><td>\d{1,5}<",
    "ipre": ipre,
    "portre": [">\d{2,5}<", "\d{2,5}"],
    "prore" : prore
})


"""
