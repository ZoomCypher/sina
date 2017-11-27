import requests
import re
import json
import time
import pymysql

class GetComment(object):

    def __init__(self):
        self.page = 1
        self.cur = 1
        self.next = ''
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36',
            'Referer': 'http://topic.sina.cn/',
            'Accept-Language': 'zh-CN,zh;q=0.8'
        }
        self.switch = True
        self.newsid = 'topic-6050'
        # self.db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='L516677d', db='sina_topic', charset='utf8')
        # self.cursor = self.db.cursor()

    def get_cookie(self):
        cookie_url = 'http://topic.sina.cn/'
        r = self.ession.get(cookie_url)
    
    # get comment 
    def get_comments(self):
        while self.switch:
            self.next = self.get_zepto()
            self.cur = self.get_cur()
            url = 'http://comment5.news.sina.com.cn/page/info?channel=wap&newsid={}&thread=1&page_size=20&h_size=10&t_size=2&ie=utf-8&oe=utf-8&page={}&_={}&callback={}'.format(self.newsid, self.page, self.cur, self.next)
            # request
            content = self.session.get(url, headers=self.headers)
            content.encoding = 'utf-8'
            html = content.text
            # catch data
            if not re.findall('"content": \"(.*?)\"', html):
                print('程序结束')
                self.db.close()
                break
            comments = re.findall('"content": \"(.*?)\"', html)

            print('####正在爬取第%s页.........' % self.page)
            for comment in comments:
                time.sleep(1)
				# decode string
                try:
                    decoding_comment = json.loads('{"x":"%s"}' % comment)
                    decoded_comment=decoding_comment['x']
                except Exception as e:
                    print("####出现错误, %s" % e)
                    pass
                print(decoded_comment)
                self.save_data(decoded_comment)
            self.page += 1
    
    def save_data(self, decoded_comment):
        with open('child_abuse.txt', 'a+', encoding='utf-8') as f:
            decoded_comment = decoded_comment + '\r\n'
            f.write(decoded_comment)
    
    def save2MySQL(self, decoded_comment):
        sql = 'insert into child_abuse (comment) values ("%s");' % decoded_comment
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            pass
            # db.rollback()

    def get_cur(self):
        # millis 13bit unix timestamp based on Java
        millis = int(round(time.time() * 1000))
        return millis

    def get_zepto(self):
        # notice the order
        millis = int(round(time.time() * 1000))
        zepto = 'Zepto' + str(millis)
        return zepto

if __name__ == '__main__':

    comms =  GetComment()
    comms.get_comments()