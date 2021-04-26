from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from API_Module.API_keypull import get_api_key
import os.path
import yagmail

pathname = os.path.abspath(os.getcwd())
pathname = pathname + "/Amazon bot/chromedriver"
link = "https://www.amazon.com/gp/product/B08166SLDF?pf_rd_r=BPHWMSB9YKK2RQF8JV44&pf_rd_p=9d9090dd-8b99-4ac3-b4a9-90a1db2ef53b&pd_rd_r=beefadb7-50b4-4446-aa69-fab673fe07b8&pd_rd_w=NJTdN&pd_rd_wg=7ImJ9&ref_=pd_gw_unk"
link2 = "https://www.amazon.com/Promised-Land-Barack-Obama/dp/1524763160/ref=zg_bs_books_home_1?_encoding=UTF8&psc=1&refRID=VFQMA61Z6C9PD0BH1RGX"
name = "paxtondfreeman@gmail.com"
amz_pwd = get_api_key("Amazon")
buyAvailable = "false"

driver = webdriver.Chrome(pathname)
driver.get(link)

def text_link():
    user = REMOVED
    app_password = get_api_key('gmail_app')
    to = REMOVED
    subject = "The 5900x CPU has just become available"# for " + price.text + "."
    content = ["Buy it before it it sells out. ", link]

    with yagmail.SMTP(user, app_password) as yag:
        yag.send(to, subject, content)

# Check for cookies
try:
    cookies = driver.find_element_by_id("sp-cc-accept")
    cookies.click()
except:
    print("no cookies!")

# While loop if product is not yet available
while buyAvailable == "false":
    try:
        buyNow = driver.find_element_by_id("buy-now-button")
        buyNow.click()
        buyAvailable = "true"
    except:
        driver.implicitly_wait(180)
        driver.refresh()
    else:
        # price = driver.find_element_by_id("price_inside_buybox")
        text_link()

# Email
email = driver.find_element_by_id("ap_email")
email.send_keys(name)

# Continue
cn = driver.find_element_by_id("continue")
cn.click()

# Password
passw = driver.find_element_by_id("ap_password")
passw.send_keys(amz_pwd)

# Login
login = driver.find_element_by_id("signInSubmit")
login.click()
