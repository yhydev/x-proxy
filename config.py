#!/usr/bin/env python


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
"https://www.my-proxy.com/free-proxy-list-10.html"]

spiderConfig = []
spiderConfig.append({
    "urls": urls,
    "proxyre": proxyre,
    "ipre": ipre,
    "portre": portre,
    "prore" : prore
})





spiderConfig.append({
    "urls": "https://free-proxy-list.net/",
    "proxyre": ">\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}</td><td>\d{1,5}<",
    "ipre": ipre,
    "portre": [">\d{2,5}<", "\d{2,5}"],
    "prore" : prore
})
