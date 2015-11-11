#-*- coding:utf-8 -*-
__author__ = 'miudodo'

import urllib2
import urlparse
from bs4 import BeautifulSoup
import MySQLdb

url = 'http://giphy.com/'
next_url = ''

for i in range(0,2):
    url = urlparse.urljoin(url, next_url)

    response = urllib2.urlopen(url)
    soup = BeautifulSoup(response)

    gif_data = soup.find_all('a', class_ = 'gif-link')
    gif_data_values = []

    for j in range(len(gif_data)):
        url_media_begin = 'https://media.giphy.com/media/'
        url_media_end = '/giphy.gif'

        gif_id = gif_data[j]['href'].split('gifs/')[1]
        gif_url = url_media_begin + gif_id + url_media_end
        gif_animated = gif_data[j].find('img')['data-animated']
        gif_static = gif_data[j].find('img')['data-static']

        value = [gif_id, gif_url, gif_animated, gif_static]
        gif_data_values.append(value)

    next_url = soup.find(id = 'next-page-arrow')['href']

print gif_data_values
'''
conn = MySQLdb.connect(db="rr7onr4m114ysz3c",
                        user="rr7onr4m114ysz3c",
                        passwd="miaodd",
                        host="rdsrvqrarimnzev.mysql.rds.aliyuncs.com",
                        port=3306)


try:
    cur = conn.cursor()
    cur.executemany('insert into mp3time (mp3id, mp3time) values (%s, %s)', values)

    conn.commit()
    cur.close()
    conn.close()

except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
'''
