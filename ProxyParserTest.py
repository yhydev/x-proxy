#!/usr/bin/env python
#--* coding: utf-8 *--
import re, ProxyParser, logging
logging.basicConfig(level = logging.DEBUG)


text = """

FREE SERVICES
USA PROXIES
U.K. PROXIES
PAID PROXY LIST
PROXY LIST (IP:PORT)
Proxies on this list are sorted by SOCKS Type

    89.201.7.196:4145
    1.220.9.68:4145
    119.198.247.15:1080
    119.198.247.31:1080
    59.22.96.114:1080
    109.201.161.62:4145
    85.113.28.249:4145
    92.62.72.212:1080
    109.201.190.190:4145
    212.42.99.32:4145
    92.62.72.252:4145
    89.201.83.52:4145
    84.15.208.122:4145
    77.38.154.62:4145
    80.90.40.218:4145
    88.207.201.116:4145
    92.55.73.124:4145
    115.134.4.112:4145
    124.195.199.225:4145
    103.110.110.196:1080
    124.195.199.237:4145
    188.172.94.72:4145
    195.158.81.42:4145
    195.158.91.236:4145
    195.158.99.111:4145
    195.158.92.104:4145
    41.72.193.38:4145
    187.189.66.196:4145
    200.56.60.157:4145
    189.201.241.69:4145
    175.141.186.32:4145
    103.58.16.57:4145
    78.157.21.40:4145
    89.205.31.36:4145
    31.3.89.194:4145
    185.204.59.8:4145
    41.188.49.110:1080
    41.217.219.161:4145

Want thousands of public proxies? Buy our Paid Proxy and SOCKS list membership.
Tired of slow and bad free proxies? Try our fast and reliable Premium Proxies and SOCKS from USA and Europe!
 SamAirPrivacy Policy
Other Languages: Русский
"""







proxyre = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{2,4}'
ipre = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
portre = [':\d{2,5}', '\d{2,5}']
prore = ''
res = re.findall(proxyre, text)
logging.debug(res)

pp = ProxyParser.ProxyParser(proxyre, ipre, portre, prore)
proxys = pp.parse(text)

for proxy in proxys:
    logging.debug("%s %s", proxy.ip, proxy.port)


