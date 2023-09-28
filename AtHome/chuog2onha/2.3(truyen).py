# import re
# import os
# import requests

# url="https://truyenfull.vn/the-loai/kiem-hiep"
# html = requests.get(url).text

# TieuDe=re.findall('<h3 class="truyen-title" itemprop="name"><a.*?>(.*?)</a></h3>', html)
# TacGia=re.findall('<span class="author" itemprop="author"><span.*?>.*?</span>(.*?)</span>', html)
# Chuong=re.findall('<span class="chapter-text"><span>(.*?)</span></span>(.*?)</a>', html)

# str=""
# for i in range(len(TieuDe)):
#     str+=TieuDe[i].text + "\n"
#     str+="- " + TacGia[i].text + "\n"  
#     str+="- " + Chuong[i].text + "\n"


    
# filename=os.path.join("D:/KPW", "truyenkiemhiep.txt")    
# with open(filename, 'w',encoding='utf-8') as f:
#     f.write(str)