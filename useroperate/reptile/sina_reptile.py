import requests
# import lxml
from lxml import etree

res = requests.get('https://s.weibo.com/top/summary?Refer=top_hot')
# print(res.text)
xhtml = etree.HTML(res.text)
# result = etree.tostring(xhtml, encoding='utf-8')
result_text = xhtml.xpath("//td[@class='td-02']/a/text()")
result_href = xhtml.xpath("//td[@class='td-02']/a/@href")
# print([])
# 遍历每一项
# for i in range(len(result_text)):
    # print(result_text[i])
# 热搜文本部分
print(result_text)
# for i in result_href:
#     i
print('---------------------')
print(['https://s.weibo.com/'+ i for i in result_href])
# print(type(result))
# print(xhtml)
# print(type(xhtml))··