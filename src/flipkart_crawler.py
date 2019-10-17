import requests
from bs4 import BeautifulSoup

# url="https://www.flipkart.com/samsung-super-6-108cm-43-inch-ultra-hd-4k-led-smart-tv/p/itmfdzq6khv2pcvz"
url="https://www.flipkart.com/samsung-super-6-138cm-55-inch-ultra-hd-4k-led-smart-tv/p/itmfdzq6xahtdzur?pid=TVSFDZQ6UPSJBGVN&fm=SEARCH&ppt=Read%20Review&ppn=Read%20Review&ssid=9hgf3clsxs0000001567916341603"
response = requests.get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)
# print(html_soup)
review_container = html_soup.find_all('div', class_ = 'col _390CkK')
print(review_container)