

from selenium import webdriver

import time
import pandas as pd

driver=webdriver.Chrome(executable_path=r'C:\Program Files (x86)\chromedriver.exe')
driver.get('https://opentender.eu/all/search/tender')
time.sleep(10)



next_page=driver.find_element_by_class_name('page-btn.page-next')
f_lis=[]
count=0
while next_page:
    time.sleep(10)
    s=driver.find_element_by_tag_name('tbody')
    rows=s.find_elements_by_tag_name('tr')
    
    for i in rows:
        td_=i.find_elements_by_tag_name('td')
        lis=[]
        for j in td_:
            lis.append(j.text)
        f_lis.append(lis[1:])
    count+=1
    if count==10:
        break
    print(count)
    next_page.click()
# print(f_lis)

df=pd.DataFrame(f_lis,columns=['Title','Buyer','Supplier','Bid Price'])

df.to_csv('tenders_data.csv',index=None)