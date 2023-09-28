# import requests
# import re
# import os
# from urllib.parse import urljoin, urlsplit
# url = "http://baovanhoa.vn/kinh-te/doanh-nghiep"
# link_seen = []
# links_todo=[]
# for i in range(2,93):
#     links_todo += ["http://baovanhoa.vn/kinh-te/doanh-nghiep/pgrid/591/pageid/" +str(i)]
    
# def getLink(url):
#     print('**Now visiting:',url)

#     html = requests.get(url).text
#     links= re.findall('<h2 class="edn_articleTitle"><a href="(.*?)" target="_self">',html)
    
#     for link in links:
#         if link not in links_todo and link not in url and link not in link_seen:
#             link_seen.append(link)
#     if links_todo: 
#         getLink(links_todo.pop())
#     else:
#         return
    
# getLink(links_todo.pop())

# str=""
# for i in  link_seen:
#     str += i + '\n'
# filename=os.path.join("D:/KPW", "Vanhoa.txt")    
# with open(filename, 'w',encoding='utf-8') as f:
#     f.write(str)