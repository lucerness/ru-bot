import os
import requests
import json
import pyfiglet
import lxml
from bs4 import BeautifulSoup
def icon_bot():
  icon = pyfiglet.figlet_format("RU BOT")
  print(icon)


def locationphone(phone=''):
    try:

       response1 = requests.get(f'https://mobile-tracker.biz/emulator/check?driver=geo&country=RU&provider=phone&uid=+{phone}&mode=undefined&_=1648381248958')
       textdecode = json.loads(response1.text)
       results = textdecode.get('location')
       data = {
          'coordinates =': results.get('geo_city'),
          'CITY =': results.get('city'),
          'COUNTRY = ': results.get('country'),
          'OPERATOR = ': results.get('operator'),
       }
       print(data)
    except:
        print('eror')





def isheyka(phone=''):
    try:
        responseisheyka = requests.get(f'https://ищейка.com/tel/986/91_189638/{phone}/')
        soup = BeautifulSoup(responseisheyka.text,'lxml')
        quote1 = soup.find_all('td')
        quote2 = soup.find_all('th')
        responsedatacol1 = []
        responsedatacol2 = []
        for quote1s in quote1:
          responsedatacol1.append(quote1s.text)
        for quote2s in quote1:
          responsedatacol2.append(quote2s.text)
        results = {
          'Country': responsedatacol1[0] and responsedatacol2[0], 
          'Code-Country': responsedatacol1[1] and responsedatacol2[1],
          'Operator': responsedatacol1[2] and responsedatacol2[2],
          'Numberphone': responsedatacol1[4] and responsedatacol2[4],
          'Location': responsedatacol1[5] and responsedatacol2[5],
          'Rating': responsedatacol1[6] and responsedatacol2[6],
          'Name': responsedatacol1[7] and responsedatacol2[7],
          'Abonent': responsedatacol1[8] and responsedatacol2[8],
          'Geolocation': responsedatacol1[9] and responsedatacol2[9],
        }
        print(results)
    except:
        print("Error")


def vksearch(id=''):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'} 
        cookies = {'enwiki_session': '17ab96bd8ffbe8ca58a78657a918558'}
        response3 = requests.get(f'https://vk.watch/{id}/profile', cookies=cookies, headers=headers)
        soup = BeautifulSoup(response3.text, 'lxml')
        search1 = soup.find_all('div', class_='profile_info_row')
        results = []
        for search in search1:
          results.append(search.text.replace('Имя','').replace('Фамилия', '').replace('ID', '').replace('Знаменитость', '').replace('В сети', '').replace('Был сети', '').replace('Имеет мобильный', '').replace('Подписчиков', ''))
        print(results)
        vkwatch = {
          'SITE': 'vk.watch',
          'ID': results[0],
          'NAME': results[2],
          'SURNAME': results[3],
          'POPULAR': results[4],
          'ONLINE': results[10],
          'LAST ACTIVITY': results[12],
          'HAVEMOBILENUMBER': results[13],
        }
        print(vkwatch)
    except Exception as e:
        print(e)
  

def main():
    icon_bot()
    choice = int(input('1 - phone location:\n2 - internet footprints\n3 - vksearch\n'))
    os.system('clear')
    if choice == 1:
       os.system('clear')
       icon_bot()
       phoneslocation = int(input('number phone: '))
       locationphone(phone=phoneslocation)
    elif choice == 2:
        os.system('clear')
        icon_bot()
        phoneisheyka = int(input('phone number: \n'))
        isheyka(phone=phoneisheyka)
    elif choice == 3:
        os.system('clear')
        icon_bot()
        id = input('id username: \n')
        vksearch(id=id)
        

if __name__ == '__main__':
    main()
