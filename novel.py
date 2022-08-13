from bs4 import BeautifulSoup
import requests
from random import randint
from re import sub
#pip install lxml
def noveltext():
    rand = randint(1,87000)
    url = "https://18av.tv/novel_"+str(rand)+".html"
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36','Cookie': 'JSESSIONID=FABD50C939A55F2C79969825F6C3A7B1; inccuLan=zh-TW; _ga=GA1.3.429236904.1637247368; key=$BEB4D59278AA5A02.109306062@nccu.edu.tw:109306062:nccu.edu.tw:tw; m2kuid=; m2kps=; NCCUWEBSSO=A121849BB62C0E895C08C860283EC3DF395C22EECAAEDFF2878D94E388D0542CB35CF910D7FF514A494457005F4E6BD92F578B57086009087162CA6D09218D58E2245975226CDF20525E08C384A6AB3EDDED4AC2692BB683CF23F4D2D89ECA880821456FEF6AA7D98E4805A58FCA359BFD21B8A90AADAF95121ECA37FD2C39DAF3F2E319; .LDAPAUTH=E39229106B5F270A6ED6AC6955C33C31CD46B79C88FEB2E42D9E6DC7D5A202AA8E12B26E065E62D5DB01AFAE2B9B5F7AB5D13A75407FD40A851FFB0EC95B9FFE358E7532DCD5EA62006C466D98D899D8C2C8F9F1CAC5F0910D542A10EF5DAAE9B893DB070A0BEE1AFBEAD48D6AFBBCE37475C685B5D911DE664644A677821C65A0AB2728',}

    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    html = soup.prettify()

    tag = soup.find("table")
    td = tag.findChild("td")
    novel = str(td)
    novel = novel[:]

    novel = sub("<br/>","\n",novel)
    novel = sub("</td>","",novel)
    # novel = sub('<tdid="novel_content_txtsize"width="800">',"",novel)

    novel = sub("[	 ]","",novel)
    novel = (novel.replace('<tdid="novel_content_txtsize"width="800">', ""))
    novel = (novel.replace('※ahref="http://www.jkforum.net"target="_blank"www.jkforum.net</a>｜JKF捷克論壇</font></font>', ""))
    # with open("novel/"+str(rand)+".txt",'w',encoding="utf-8") as f:
    #         f.write(novel)
    return novel

# novel = noveltext()
# print(novel)