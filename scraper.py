from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")

item = input("Jakiego produktu szukasz: ")
item.replace(" ", "-")
city = input("W jakim mieście szukasz: ")
start_url = "https://www.olx.pl/" + city + "/q-" + item 
driver = webdriver.Chrome(options=chrome_options)
driver.get(start_url)
sleep(1)
driver.find_element_by_id("onetrust-accept-btn-handler").click()
sleep(1)
driver.find_element_by_class_name("numeric-item").click()
driver.find_element_by_xpath("/html/body/div[1]/header/div[3]/div/form/noindex/div/fieldset[2]/ul/li[1]/ul/li/div[2]/div[1]/ul/li[7]/a").click()
sleep(1)
soup = BeautifulSoup(driver.page_source, 'html.parser')
file = open('offers.html', 'w')
offers = soup.findAll("a", {"class": "detailsLink"})
file.write(str(offers))
print(offers)