# import requests
# import os
# from bs4 import BeautifulSoup

# url="http://baovanhoa.vn/kinh-te/doanh-nghiep"

# Links_ToDo=[url]
# for i in range(2,92):
#     Link="http://baovanhoa.vn/kinh-te/doanh-nghiep/pgrid/591/pageid/" + str(i)
#     Links_ToDo += [Link]

# str=""
# for url in Links_ToDo:
#     print(url)
#     html = requests.get(url).text
    
#      #Tối ưu hóa code HTML bằng thư viện html5lib
#     soup = BeautifulSoup(html, 'html5lib')
    
#     TieuDe = soup.find_all("h2",class_="edn_articleTitle")
#     Tomtin = soup.find_all("div",class_="edn_articleSummary")
#     Ngaygio = soup.find_all("div",class_="edn_metaDetails")
#     # Nguontin = soup.find_all("span",class_="post-location")
# # print(str)
#     for i in range(len(TieuDe)):
#         str+=TieuDe[i].text + "\n"
#         str+="- " + Tomtin[i].text + "\n"  
#         str+="- " + Ngaygio[i].text + "\n"
#         # str+="- " + Nguontin[i].text + "\n"  
        

# filename=os.path.join("D:/KPW", "cau3.txt")    
# with open(filename, 'w',encoding='utf-8') as f:
#     f.write(str)


    