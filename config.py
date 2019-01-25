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
"https://www.my-proxy.com/free-proxy-list-10.html",
"http://spys.one/proxys/BR/",
"http://spys.one/proxys/US/",
"http://spys.one/proxys/ID/",
"http://spys.one/proxys/CZ/",
"http://spys.one/proxys/ZA/",
"http://spys.one/proxys/TH/",
"http://spys.one/proxys/CO/",
"http://spys.one/proxys/IT/",
"http://spys.one/proxys/EC/",
"http://spys.one/proxys/GB/",
"http://spys.one/proxys/FR/",
"http://spys.one/proxys/MX/",
"http://spys.one/proxys/CA/",
"http://spys.one/proxys/NP/",
"http://spys.one/proxys/NG/",
"http://spys.one/proxys/VN/",
"http://spys.one/proxys/IQ/",
"http://spys.one/proxys/AL/",
"http://spys.one/proxys/RO/",
"http://spys.one/proxys/PH/",
"http://spys.one/proxys/SK/",
"http://spys.one/proxys/LV/",
"http://spys.one/proxys/GE/",
"http://spys.one/proxys/PE/",
"http://spys.one/proxys/CL/",
"http://spys.one/proxys/AU/",
"http://spys.one/proxys/KZ/",
"http://spys.one/proxys/LB/",
"http://spys.one/proxys/MN/",
"http://spys.one/proxys/CM/",
"http://spys.one/proxys/PS/",
"http://spys.one/proxys/KG/",
"http://spys.one/proxys/HN/",
"http://spys.one/proxys/TZ/",
"http://spys.one/proxys/AM/",
"http://spys.one/proxys/PY/",
"http://spys.one/proxys/PR/",
"http://spys.one/proxys/GT/",
"http://spys.one/proxys/PT/",
"http://spys.one/proxys/AZ/",
"http://spys.one/proxys/HR/",
"http://spys.one/proxys/UG/",
"http://spys.one/proxys/DO/",
"http://spys.one/proxys/AE/",
"http://spys.one/proxys/CD/",
"http://spys.one/proxys/MK/",
"http://spys.one/proxys/YE/",
"http://spys.one/proxys/SA/",
"http://spys.one/proxys/AO/",
"http://spys.one/proxys/GH/",
"http://spys.one/proxys/BE/",
"http://spys.one/proxys/IE/",
"http://spys.one/proxys/ZM/",
"http://spys.one/proxys/SO/",
"http://spys.one/proxys/SC/",
"http://spys.one/proxys/CH/",
"http://spys.one/proxys/BI/",
"http://spys.one/proxys/UY/",
"http://spys.one/proxys/ME/",
"http://spys.one/proxys/WS/",
"http://spys.one/proxys/MG/"]

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
