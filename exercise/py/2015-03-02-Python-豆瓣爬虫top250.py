#-*- encoding:UTF-8 -*-

"""
简单的豆瓣电影top250爬虫程序
结果写入到文件output.txt
"""

import re
import urllib2
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class DoubanMovieSpider(object):
    """ 抓取豆瓣电影榜的top250"""

    def __init__(self):
        self.source_url = "http://movie.douban.com/top250?start={page}&filter=&type="
        self.pattern = r'class="">.*?<span.*?class="title">(.*?)</span>'
        self.outputfile = "output.txt"

    def getHTMLPage(self, idx):
        """根据idx抓取网页
            @idx ：从1开始 
        """
        try:
            url = self.source_url.format( page = (idx-1)*25 )
            pageData = urllib2.urlopen( url ).read().decode("utf-8")
        except:
            print "some error happend!"
        
        return pageData 

    def goSpider(self):
        """开始抓取数据工作"""
        output_file = open(self.outputfile, "w")

        for _pageIdx in range(1, 11):  # 从第1页到第10页,每页25个
            page_data = self.getHTMLPage(_pageIdx)
            res_data = re.findall(self.pattern, page_data, re.S)

            for index, item in enumerate(res_data):
                output_file.write("top " + str(25 * (_pageIdx-1) + index + 1) + ": " + item + "\n")
     
        output_file.close()


if __name__ == "__main__":

    print "启动豆瓣电影排行榜250爬虫工具。。。"

    spider = DoubanMovieSpider()
    spider.goSpider()

    print " ---- start ---- "
    with open(spider.outputfile, "r") as pages:
        for line in pages:
            print line,
    print " ---- over ---- "

