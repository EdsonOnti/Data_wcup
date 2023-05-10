from bs4 import BeautifulSoup as BS
import requests 
import lxml as lxml
import pandas as pd

years = [i for i in range(1930, 2022, 4) if i not in [1942, 1946]]
  


def get_matches(year):

    web=f"https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup"
    response=requests.get(web)
    content=response.text
    soup=BS(content,'lxml')

    matches=soup.find_all('div',class_='footballbox')

    home=[]
    score=[]
    visit=[]

    for match in matches:
        home.append(match.find('th', class_='fhome').get_text())
        score.append(match.find('th', class_='fscore').get_text())
        visit.append(match.find('th', class_='faway').get_text())

    dict_futbol={'Local':home,'Score':score,'Visitante':visit}

    df_futbol=pd.DataFrame(dict_futbol)
    df_futbol['year']= year
    return df_futbol

all_wcups=[get_matches(year) for year in years]
df_all_wcups=pd.concat(all_wcups, ignore_index=True)
df_all_wcups.to_csv('fifa_all_world_data.csv', index=False)

def get_fitxure(url):

    web=f"{url}"
    response=requests.get(web)
    content=response.text
    soup=BS(content,'lxml')

    matches=soup.find_all('div',class_='footballbox')

    home=[]
    score=[]
    visit=[]

    for match in matches:
        home.append(match.find('th', class_='fhome').get_text())
        score.append(match.find('th', class_='fscore').get_text())
        visit.append(match.find('th', class_='faway').get_text())

    dict_futbol={'Local':home,'Score':score,'Visitante':visit}

    df_futbol=pd.DataFrame(dict_futbol)
    df_futbol['year']= 2022
    return df_futbol

df_fitxure=get_fitxure('https://web.archive.org/web/20221115040351/https://en.wikipedia.org/wiki/2022_FIFA_World_Cup')
df_fitxure.to_csv('fitxure_fifa_wordcup_2022.csv', index=False)
    