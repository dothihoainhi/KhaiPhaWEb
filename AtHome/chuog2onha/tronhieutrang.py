# import requests
# import os
# from bs4 import BeautifulSoup
 
# url="https://phongtro123.com/tinh-thanh/da-nang"

# Links_ToDo=[url]
# for i in range(2,51):
#     Link="https://truyenfull.vn/the-loai/kiem-hiep/trang=" + str(i)
#     Links_ToDo += [Link]

# str=""
# for url in Links_ToDo:
#     print(url)
#     html = requests.get(url).text
    
#      #Tối ưu hóa code HTML bằng thư viện html5lib
#     soup = BeautifulSoup(html, 'html5lib')
    
#     TieuDe = soup.find_all("h3",class_="post-title")
#     Gia = soup.find_all("span",class_="post-price")
#     Dientich = soup.find_all("span",class_="post-acreage")
#     Diachi = soup.find_all("span",class_="post-location")
#     Ngaydang = soup.find_all("time",class_="post-time")

# # print(str)
#     for i in range(len(TieuDe)):
#         str+=TieuDe[i].text + "\n"
#         str+="- " + Gia[i].text + "\n"  
#         str+="- " + Dientich[i].text + "\n"
#         str+="- " + Diachi[i].text + "\n"  
#         str+="- " + Ngaydang[i].text + "\n"


    