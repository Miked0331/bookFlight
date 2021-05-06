import time
import colorama
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from colorama import Fore, Back, Style, init
colorama.init()

#Must use path to your own geckodriver file
geckodriver = r'C:\Geckodriver\geckodriver.exe'
 
#This option allows you to run this script in headless mode which allows it to run with no browser being opened
#To enable uncomment line 19
options = webdriver.FirefoxOptions()
# options.add_argument('-headless')
 
browser = webdriver.Firefox(executable_path=geckodriver, options=options)

aalinesHome = r"https://www.aa.com/homePage.do"

browser.get(aalinesHome)
browser.maximize_window()

#departing airport
depart_city_field = browser.find_element_by_name("originAirport")
depart_city_field.clear()
depart_city_field.send_keys("PIT")

#destination airport
arrive_city_field = browser.find_element_by_name("destinationAirport")
arrive_city_field.clear()
arrive_city_field.send_keys("TPA")

#depart date
depart_date_field = browser.find_element_by_name("departDate")
depart_date_field.send_keys("08/19/2021")

#return date
arrive_date_field = browser.find_element_by_name("returnDate")
arrive_date_field.send_keys("08/24/2021")

time.sleep(2)

#finding and clicking the search button
search_button = WebDriverWait(browser, 2).until(
    EC.element_to_be_clickable((By.ID, "flightSearchFormSubmitButton"))
)

search_button.click()

time.sleep(5)

#sorting departing flight based on price aka saving money
departing_dropdown = Select(WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "searchResultsSortOptions"))))
departing_dropdown.select_by_value("price")

# selecting the first  flight for lowest cost for departure
roundtrip_button = WebDriverWait(browser,2).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="slice0Flight17MainCabin"]'))
)
roundtrip_button.click()

time.sleep(4)

#sorting cheapest returning flight
arriving_dropdown = Select(WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "searchResultsSortOptions"))))
arriving_dropdown.select_by_value("price")

# selecting first flight back after being sorted
roundtrip_button2 = WebDriverWait(browser,2).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="slice1Flight1MainCabin"]'))
)
roundtrip_button2.click()

#close pop up that asks for upgrading flight 
popup_close = WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.ID, "mainCabinUpsellDialogClose"))
)
popup_close.click()

#continue as guest
guest_button = WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.ID, "button_continue_guest"))
)
guest_button.click()

#### *** GOOGLE SEARCH FLIGHTS *****

# homePage = r"https://www.southwest.com/"
# googleHome = r"https://google.com/"

# browser.get(googleHome)
# browser.maximize_window()

# search_field = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
# search_field.send_keys("Flight from Pittsburgh to Las Vegas")

# google_search_button = WebDriverWait(browser, 2).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "gNO89b"))
# )
# google_search_button.click()

# show_flights_button = WebDriverWait(browser, 2).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "wUrVib"))
# )
# show_flights_button.click()

# time.sleep(2)

# #fill in your email and password creds "your email" "your pass"
# depart_field = browser.find_element_by_css_selector(".uNiB1 > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)")
# depart_field.click()
# time.sleep(1)
# depart_field.send_keys("Thu, Aug 19")
# arrive_field = browser.find_element_by_css_selector(".uNiB1 > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)")
# arrive_field.click()
# arrive_field.click()
# arrive_field.click()
# time.sleep(1)
# arrive_field.send_keys("Mon, Aug 23")

# #finalize date button
# date_button = WebDriverWait(browser, 2).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "VfPpkd-Jh9lGc"))
# )
# date_button.click()

# time.sleep(5000)
# depart_date_field = browser.find_element_by_xpath("/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div/c-wiz/div[2]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/input")
# depart_date_field.send_keys("3/31")
# return_date_field = browser.find_element_by_id("LandingAirBookingSearchForm_returnDate")
# return_date_field.send_keys("4/04")

# time.sleep(10)

# search_button = WebDriverWait(browser, 2).until(
#             EC.element_to_be_clickable((By.ID, "LandingAirBookingSearchForm_submit-button"))
#             )
# search_button.click()
# print("search button clicked")