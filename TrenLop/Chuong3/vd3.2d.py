# from bs4 import BeautifulSoup
# Text = "<html><head><title>Khoa học dữ liệu</title><style>.call {background-color:black;} </style><script>getit</script></head><body>Là một ngành học<div>đáp ứng xu hướng việc làm trong tương lai.</div></body></html>"
# def remove_tags(html):
# # parse html content
#     soup = BeautifulSoup(html, "html.parser")
#     for data in soup(['style', 'script']):
#         data.decompose() # Remove tags
#         return ' '.join(soup.stripped_strings)
# print(remove_tags(Text))