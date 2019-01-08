# 多线程下载百思不得姐段子(生产者与消费者模式)
# 百思不得姐 内涵段子网站：http://www.budejie.com/text/

########################### 使用传统方式爬取和下载内涵段子 ###########################
import requests
from lxml import etree
import csv

def parse_page(url):
    headers = {
        'User-Agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"
    }
    response = requests.get(url,headers=headers)
    text = response.text
    html = etree.HTML(text)
    descs = html.xpath("//div[@class='j-r-list-c-desc']")
    for desc in descs:
        jokes = desc.xpath(".//text()")
        joke = '\n'.join(jokes).strip()      # ...做了什么格式处理？
        base_domain = "http://www.budejie.com"
        link = base_domain + desc.xpath(".//a/@href")[0]
        fp = open('bsbdj.csv', 'a', newline='', encoding='utf-8')
        writer = csv.writer(fp)
        writer.writerow((joke, link))

def main():
    for x in range(1,11):    #爬取前10页内容
        url = 'http://www.budejie.com/text/%d' % x    #构建url
        parse_page(url)

if __name__ == '__main__':
    main()
