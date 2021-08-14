from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def buscarIntroducao(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        introducao = bs.body.h2
    except AttributeError as e:
        return None
    return introducao

introducao = buscarIntroducao("https://www.maujor.com/")
if introducao == None:
    print(" A introdução não foi encontrada. Tente de novo")
else:
    print(introducao)
