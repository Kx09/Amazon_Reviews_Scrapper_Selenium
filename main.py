"""
The following bot is designed to scrape the amazon page for reviews, all reviews. 

Opens amazon to the url using selenium. 
gets the reviews and saves them all in csv file.
presses next to get all reveiws


"""



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import math

rev_head = []
rev_body = []


number_reviews_total = 834
times_run = (math.ceil(number_reviews_total /10 )) + 1 

chrome_options = Options()
#options.add_argument("--headless")
chrome_options.add_argument("--disable-logging")
chrome_options.add_argument("--log-level=3")
driver = webdriver.Chrome(options=chrome_options)#options=options)
credentials = {
    "email":"mr.phython909@gmail.com",
    "password": "Amazon@909"
}





driver.get("https://www.amazon.co.uk/product-reviews/B0BCK9SF96/ref=cm_cr_getr_d_paging_btm_next_2?ie=UTF8&filterByStar=critical&reviewerType=all_reviews&pageNumber=26")
time.sleep(60)

#soup = BeautifulSoup(driver.page_source, "html.parser")

#print(soup.find("div", class_="product-title").text)

for i in range(1,times_run):

    print(f"Opened Page {i}")
    titles = driver.find_elements(By.CLASS_NAME, "a-size-base.a-link-normal.review-title.a-color-base.review-title-content.a-text-bold")
    text_body = driver.find_elements(By.CLASS_NAME,"a-size-base.review-text.review-text-content")

    for elem in titles:
        rev_head.append(elem.text.replace('\n', '').replace('\t', ''))

    for elem in text_body:
        #print(elem.text)
        rev_body.append(elem.text.replace('\n', '').replace('\t', ''))

    print(f"scrapped data for page{i}")
    #print(rev_head)
    #print(rev_body)

    try:
        next_button = driver.find_element(By.XPATH, "//ul[@class='a-pagination']//li[@class='a-last']/a")
        next_button.click()
        time.sleep(1)
    except Exception as e:
        print("No more pages or next button not found:", e)
        break  # Exit the loop if no next button


print("All webpages scraped")

output = {'titles': rev_head, 'body': rev_body}
df = pd.DataFrame(output)
df.to_csv('reviews_all.csv', index=False)

print("data sucessfully saved to csv")
#print(driver.page_source)
#driver.quit()

#class="a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold"