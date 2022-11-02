from bs4 import BeautifulSoup
import requests
import lxml
header={
    "Accept-Language":"en-US,en;q=0.9,ar;q=0.8",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
AMAZON_LINK = "https://www.amazon.ae/THOMPSON-TEE-Sweatproof-Undershirt-Underarm/dp/B00CIZLWM0/ref=sr_1_1?crid=2UF9G89ROYI9D&keywords=Sweatproof%2BUndershirt%2Bfor%2BMen%2Bwith%2BUnderarm%2BSweat%2BPads%2B(Original%2BFit%2C%2BV-Neck)&qid=1667402463&qu=eyJxc2MiOiIxLjY0IiwicXNhIjoiMC4wMCIsInFzcCI6IjAuMDAifQ%3D%3D&sprefix=sweatproof%2Bundershirt%2Bfor%2Bmen%2Bwith%2Bunderarm%2Bsweat%2Bpads%2Boriginal%2Bfit%2Bv-neck%2B%2Cspecialty-aps%2C558&sr=8-1&th=1&psc=1"
response = requests.get(AMAZON_LINK, headers=header)
# print(response.text)

yc_website = response.text

soup = BeautifulSoup(yc_website, "html.parser")
price = soup.find(class_="a-price-whole", name="span")
print(float(price.get_text()))
