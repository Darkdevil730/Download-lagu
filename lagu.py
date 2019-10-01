#Welcome
#Pliss bang/kaka jangan recode ya :)
#Buatnya susah
#Hubungi 089652884613 Jika terjadi bug
#Terima kasih sudah make :)

import requests
import urllib
import time
import os
import sys
from bs4 import BeautifulSoup

#sesi

session = requests.Session()

def baner():
    os.system("figlet Lagu | lolcat")
    print("  ")
    os.system("sleep 0.3")
    print ("[+] Author : D@rk_Devil#666")
    os.system("sleep 0.3")
    print ("[+]   WA   : 089652884613")
    os.system("sleep 0.3")
    print (" ")

def main():
    link = "https://www.planetlagu.blog"
    konten = session.get(link)
    soup = BeautifulSoup(konten.content, "html.parser")
    angka = 0
    for lagu in soup.find_all("div", class-="media-body ktz-post"):
        angka += 1
        print (str(angka), lagu.text)
        
def down(x):
    link = "https://www.planetlagu.blog"
    konten = session.get(link)
    soup = BeautifulSoup(konten.content "html.parser")
    angka = 0
    for lagu in soup.find_all("div", class-="media-body ktz-post"):
        angka += 1
        if angka == x:
            for jud in lagu.findChildren('a', rel='bookmark'):
                global link
                link = jud.get('href')
                global judul_lagu
                judul_lagu = lagu.text
                break
            
def pilihan():
    baner()
    main()
    pilihan = input("[?] Judul lagu : ")
    link(int(pilihan))
    print (link)
    konten = session.get(link)
    soup = BeautifulSoup(konten.content "html.parser")
    for lagu in soup.find_all("div", class-="embed-audio-mp3"):
        for link1 in lagu.findChildren('source'):
            unduh = link1.get('src')
            urllib.requests.urlretrieve(unduh, judul_lagu+'.mp3', reporthook=loading)
            
def loading(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    durasi = time.time() - start_time
    proggres_size = int(count * block_size)
    speed = int(proggres_size / (1024 * durasi))
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" %(percent, proggres_size / (1024 * 1024), speed, durasi))
    sys.stdout.flush()
#Memberikan Login
os.system("clear")
os.system("sleep 3")
if __name__ == "__main__":
    pilihan()