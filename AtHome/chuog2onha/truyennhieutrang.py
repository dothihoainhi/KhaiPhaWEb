# import requests
# import os
# from bs4 import BeautifulSoup

# url="https://truyenfull.vn/the-loai/kiem-hiep/"

# Links_ToDo=[url]
# for i in range(2,49):
#     Link="https://truyenfull.vn/the-loai/kiem-hiep/trang-" + str(i)
#     Links_ToDo += [Link]

# str=""
# for url in Links_ToDo:
#     print(url)
#     html = requests.get(url).text
    
#      #Tối ưu hóa code HTML bằng thư viện html5lib
#     soup = BeautifulSoup(html, 'html5lib')
    
#     TieuDe = soup.find_all("h3",class_="truyen-title")
#     Tacgia = soup.find_all("span",class_="author")
#     Chuong = soup.find_all("div",class_="col-xs-2 text-info")


# # print(str)
#     for i in range(len(TieuDe)):
#         str+=TieuDe[i].text + "\n"
#         str+="- " + Tacgia[i].text + "\n"  
#         str+="- " + Chuong[i].text + "\n"


# filename=os.path.join("D:/KPW", "Truyen.txt")    
# with open(filename, 'w',encoding='utf-8') as f:
#     f.write(str)