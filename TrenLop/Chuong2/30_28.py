# import re
# import os
# import requests

# url="https://www.dienmayxanh.com/tivi"
# html = requests.get(url).text

# Tensp=re.findall('<li> class=" item  __cate_1942""><h3></h3></li>', html)
# # Giaban=re.findall('', html)
# Mucgia=re.findall('', html)
# Soluotdanhgia=re.findall('', html)

# str=""
# for i in range(len(Tensp)):
#     str+=Tensp[i] + "\n"
#     str+="- " + Giaban[i] + "\n"    
#     str+="- " + Mucgia[i] + "\n"
#     str+="- " + Soluotdanhgia[i] + "\n"
 
# filename=os.path.join("D:/KPW", "30_28.txt")    
# with open(filename, 'w',encoding='utf-8') as f:
#     f.write(str)
# print(Tensp)

# import re
# import os
# import requests

# url="https://websosanh.vn/laptop/cat-18.htm"

# html = requests.get(url).text

# Tensp = re.findall('<h3><a.*?">(.*?)</a></h3>',html)
# Giaban = re.findall('<span class = "product-meta">(.*?)</span>',html)
# Noiban = re.findall('<span",class="product-bottom">(.*?)</span>',html)
# str=""
# for i in range(len(Tensp)):
#     str+=Tensp[i] + "\n"
#     str+="- " + Giaban[i] + "\n"
#     str+=Noiban[i] + "\n"
    
# filename=os.path.join("D:/KPW", "30_28.txt")    
# with open(filename, 'w',encoding='utf-8') as f:
#     f.write(str)
    
# print(Tensp)
# print(Giaban)
# print(Noiban)

# import requests
# import re
# import os


# path = "https://websosanh.vn/laptop/cat-18.htm"
# html = requests.get(path).text


# TenSP=re.findall('</button><h3><a.*?>(.*?)</a></h3></div>', html)
# GiaBan=re.findall('<span class="product-price".*?>(.*?)</span>',html)
# NoiBan=re.findall('<span class="product-bottom"><span class="product-store.*?">(.*?)</span>',html)




# filename="28-30.txt"
# if os.path.exists(filename):
#      os.remove(filename)
# file = open(filename,"w",encoding="utf-8")


# for i in range(len(TenSP)):
#     file.write("Ten SP: "+TenSP[i]+"\n")
#     file.write("- Gia Ban: "+GiaBan[i]+"\n")
#     file.write("- "+NoiBan[i]+"\n")
#     file.write("")


