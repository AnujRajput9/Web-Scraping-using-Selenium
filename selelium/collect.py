from bs4 import BeautifulSoup
import pandas as pd
import os

d={'Title' : [] ,'Price':[]}

for file in os.listdir('data'):
    try:
        with open(f"data/{file}") as f:
            html_dock = f.read()
        soup = BeautifulSoup(html_dock,"html.parser")
        t=soup.find(attrs={"class": "KzDlHZ"})
        title = t.get_text()
        
        p=soup.find(attrs={"class": "Nx9bqj _4b5DiR"})
        price = p.get_text()

        d["Title"].append(title)
        d["Price"].append(price[3:])
    except Exception as e:
        print(e)
    
df =pd.DataFrame(data=d)
df.to_csv('data1.csv')        