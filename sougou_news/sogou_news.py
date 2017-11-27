import requests
from lxml import etree

class SogouNews(object):
    
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36',
            'Referer': 'http://weixin.sogou.com/',
            'Accept-Language': 'zh-CN,zh;q=0.8'
        }
        self.switch = True
        self.url = 'http://weixin.sogou.com/'

    def get_cookies(self):
        r = self.session.get(self.url)

    def get_bigCategory(self):
        self.get_cookies()
        content = self.session.get(self.url)
        content.encoding = 'utf-8'
        html = content.text
        html = etree.HTML(html)
        # 大类名称
        big_cate = html.xpath("//div[@class='fieed-box' or @class='tab-box-pop']/a/text() ")
        for each in big_cate:
            if each == '更多':
                continue
            print(each)
        

    def first_page_content(self, html):

        # 每类的api 
        cate_url = 'http://weixin.sogou.com/pcindex/pc/pc_%d/pc_%d.html '　% (range(1,22), range(1,22))
        content_url = 'http://weixin.sogou.com/pcindex/pc/pc_%d/%d.html' % (range(1,22, ++1))

        content = html.xpath("//div[@class='news-box']/ul/li/div/h3/text()")



if __name__ == '__main__':
    
    sg = SogouNews()
    sg.get_bigCategory()
