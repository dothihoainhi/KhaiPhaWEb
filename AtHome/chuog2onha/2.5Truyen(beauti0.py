
# import requests
# import os
# from bs4 import BeautifulSoup

# url="https://truyenfull.vn/the-loai/kiem-hiep/"
# html = requests.get(url).text
# #Tối ưu hóa code HTML bằng thư viện html5lib 
# soup = BeautifulSoup(html, 'html5lib')

# #Sử dụng thư viện BeautifulSoup để bóc tách dữ liệu
# TieuDe = soup.find_all("h3",class_="truyen-title")
# Tacgia = soup.find_all("span",class_="author")
# Chuong = soup.find_all("div",class_="col-xs-2 text-info")


# str=""
# for i in range(len(TieuDe)):
#     str+=TieuDe[i].text + "\n"
#     str+="- " + Tacgia[i].text + "\n"    
#     str+="- " + Chuong[i].text + "\n"

# print(str)

# filename=os.path.join("D:/KPW", "Truyenkiemhiep.txt")    
# with open(filename, 'w',encoding='utf-8') as f:
#     f.write(str)
