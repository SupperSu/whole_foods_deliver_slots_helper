import bs4
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import winsound

def getWFSlot(productUrl):
   driver = webdriver.Chrome(ChromeDriverManager().install())
   driver.get(productUrl)
   html = driver.page_source
   soup = bs4.BeautifulSoup(html, "html.parser")
   time.sleep(60)  # 60 seconds
   no_open_slots = True

   while no_open_slots:
      driver.refresh()
      print("refreshed")
      html = driver.page_source
      soup = bs4.BeautifulSoup(html, "html.parser")
      time.sleep(4)  # refersh every 4 seconds

      try:
         not_opened_text = "Not available"
         all_dates = soup.findAll("div", {"class": "ufss-date-select-toggle-text-availability"})
         for each_date in all_dates:
            if not_opened_text not in each_date.text:
               print('SLOTS OPEN!')
               winsound.Beep(2000, 5000)
               no_open_slots = False
               time.sleep(1400)
               break
      except AttributeError:
         # not find the available time slots
         pass
getWFSlot('https://www.amazon.com/gp/buy/shipoptionselect/handlers/display.html?hasWorkingJavascript=1')
