import requests
from bs4 import BeautifulSoup
import pandas as pd
all1=[]
all2=[]
print("HII")
for x in range(1,5):
    phys = requests.get('https://www.dogonews.com/page/{}'.format(x))
    soup = BeautifulSoup(phys.text, "html.parser")
#print(soup.prettify())

    heading=soup.find_all('span',itemprop="headline")
    content=soup.find_all('p')


#print(len(heading))
    for heading in heading:
        all1.append(heading.text)
    for content in content:
        all2.append(content.text)
#print(len(all2))
#print(len(all1))
x1=[]
for x in range(0,len(all1)-1):
    x1.append(x+1)
    print(x+1)
    print(all1[x])
    print(all2[x])
data=list(zip(x1,all1,all2))
df = pd.DataFrame(data=data,columns=['ID','Head',"Details"])
df.to_csv("tempDATA.csv", index=False, header=True)
print("ended")