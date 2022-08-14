from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class classSelenium:

    def __init__(self, driverPath):
        self.driver = webdriver.Chrome(driverPath)

    def setPage(self, page):
        self.driver.get(page)
    
    def getTable(self, tableXpath):
        headers = []
        fila = []
        arrayList = []
        
        table = self.driver.find_element(By.XPATH, tableXpath)
        tableheaders = table.find_elements(By.TAG_NAME,'th') 
        body = table.find_element(By.TAG_NAME,"tbody")
        rows = body.find_elements(By.TAG_NAME,"tr")

        for e in range(len(tableheaders)):
            headers.append(tableheaders[e].text)

        for i in range(len(rows)):
            columns = rows[i].find_elements(By.TAG_NAME,"td")
            
            for u in range(len(columns)):
                fila.append(columns[u].text)
            arrayList.append(fila)
            time.sleep(1)
            fila =[]

        return arrayList, headers




""" driver = webdriver.Chrome('C:\\Users\\juanv\\Desktop\\chromedriver.exe')
driver.get('https://tradingeconomics.com/united-states/stock-market') 

table = driver.find_element(By.XPATH,'/html/body/form/div[6]/div/div[1]/div[5]/div[1]/div/table')
headers = table.find_elements(By.TAG_NAME,'th') 
body = table.find_element(By.TAG_NAME,"tbody")
rows = body.find_elements(By.TAG_NAME,"tr")
cells = table.find_elements(By.TAG_NAME,"td")

header = []
for e in range(len(headers)):
    header.append(headers[e].text)

fila = []
arrayList = []
for i in range(len(rows)):
    columns = rows[i].find_elements(By.TAG_NAME,"td")
    
    for u in range(len(columns)):
        fila.append(columns[u].text)
    arrayList.append(fila)
    time.sleep(1)
    fila =[]
 """




