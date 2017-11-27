import requests
from lxml import etree
import re
import time


class SinaNew(object):
    
    def __init__(self):
        self.session =  requests.Session()
        self.length = 18 
        self.action = 0
        self.up = 0 
        self.ad = '{"rotate_count":562,"page_url":"https://tech.sina.cn/","channel":"130087","platform":"wap","timestamp":1511668710335,"net":null}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25',
        }
        self.switch = True

    def get_cookies(self):
        """获取cookies"""
        ## 获取cookies
        url = 'http://news.sina.cn/'
        r = self.session.get(url)

    def get_index(self):
        """请求新闻分类网站"""
        url = 'https://sina.cn/Index/nav?vt={}'.format(4)
        r = session.get(url, headers=headers)

        ## 提取分类
        content = r.text
        content = etree.HTML(content)
        # 按类分析
        big_category = content.xpath("//nav/a[@class='map_nav_a map_nav_a_tit']/@href")
        small_category = content.xpath("//nav/a[@class='map_nav_a']/@href")
        hot_category = content.xpath("//nav/a[@class='map_nav_a hot']/@href")
        gov_category = content.xpath("//nav/a[@class='map_nav_a f4']/@href")
        print(big_category, '\n\n', small_category, '\n\n', hot_category, '\n\n', gov_category)
        return [big_category, small_category, hot_category, gov_category] #不然变成元组

    def get_each(self):
        """提取分类下的标题和详情页url"""
        # for url in big_category:导入get_index中的url
        self.get_cookies()
        
        while self.switch:
            url = 'https://cre.dp.sina.cn/api/v3/get?cateid=1z&cre=tianyi&mod=wtech&merge=3&statics=1&ad={}&action={}&up={}&down=0&length={}&_=1511668710348&callback=Zepto1511668710291'.format(self.ad, self.action, self.up, self.length)
            print("开始请求第%s页-------" % self.up )

            # 注意referer
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36',
                'Referer': 'http://news.sina.cn/'
            }
            r = self.session.get(url, headers=headers)
            content = r.text
            # 设置出口 
            if not re.findall('"surl":\"(\S+?)\"\,?', content):
                print("没有网页了！！！")
                break
            # titles = re.findall('"ltitle":\"(\D+?)\"\,', content)
            # js类型，用re提取url
            urls = re.findall('"surl":\"(\S+?)\"\,?', content)
            for url in urls:
                url = url.replace('\/', '/')
                time.sleep(2)
                self.get_content(url) 
            self.length = 12
            self.action = 1
            self.up += 1
    
    def get_content(self, url):
        """爬取标题，内容"""
        r = self.session.get(url)
        r.encoding = 'utf-8'
        content = r.text
        content = etree.HTML(content) 
        # 可能页面是一个专题，里面有详情页url和内容，提取出来，分别再次请求
        if len(content.xpath("//section[@class='card_module']/div/h2/text()")) > 0:
            title = content.xpath("//section[@class='card_module']/div/h2/text()")
            print(title)
        if len(content.xpath("//article/h1/text()")) > 0:
            title = content.xpath("//article/h1/text()")
            print(title)
    
    def save_data(self):
        pass
        
         


        


if __name__ == "__main__":

    sina = SinaNew()
    sina.get_each()
        



