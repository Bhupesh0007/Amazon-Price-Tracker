from bs4 import BeautifulSoup
import requests
import smtplib

SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = ""
MY_PASSWORD = ""

product_url = "https://www.amazon.in/dp/B0D49W5KZP/?coliid=I3NGFNVLIAC28R&colid=3OOJRLK5D8OZQ&ref_=list_c_wl_lv_ov_lig_dp_it&th=1"

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
    "Dnt": "1",
    "Priority": "u=0",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36",
}

response = requests.get(product_url, headers=header)

soup = BeautifulSoup(response.content, "html.parser")

price = soup.find(class_="a-price-whole").get_text()

price = float(price.replace(",", "").strip())

title = soup.find(id="productTitle").get_text().strip()

BUY_PRICE = 87000

if price < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{product_url}".encode("utf-8")
        )
    print("The email was sent successfully!!")

else:
    print("The email was not sent!!")
