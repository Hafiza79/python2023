#! /usr/bin/env python3
import time 
import random as rnd

class style():
    RED='\033[31m'
    GREEN='\033[32m'
    BLUE='\033[34m'
    RESET='\033[0m'
print(f'{style.RED}ONE{style.RESET}')
print(f'{style.GREEN}two{style.RESET}')


songlist = {
    'suci dalam debu': 'iklim',
    'isabella': 'search',
    'dia': 'fauziah latif',
    'kekasih awal dan akhir': 'jamal abdillah',
    'bunga angkasa': 'terra rossa',
    'jerat percintaan': 'siti nurhaliza',
    'misteri mimpi shakila':'wing',
    'taman rashidah utama':'wings',
    'bidadari':'meditasi',
    'gugurnya bunga cinta':'laksamana',
    'hanya satu persinggahan':'ekamatra'
    

}
 
score = 0;
tries = 3
time.sleep(3)
print(f'{style.RED}*********************************************{style.RESET}')
print(f'{style.GREEN}            TEKA  LAGU ROCK KAPAK {style.RESET}')
print(f'{style.RED}*********************************************{style.RESET}')
time.sleep(5)

while tries > 0:
    try:
        random_song = rnd.choice(list(songlist.items()))
        intials = []
        for first_letter in random_song[0].split():
            intials.append(first_letter[0].capitalize())
 
        print(f'Klu adalah huruf pertama nama lagu: {" ".join(intials)} dan penyanyi adalah : {random_song[1].title()}')
        print(f'{style.BLUE}TEKA TAJUK LAGU?{style.RESET}')
        song = input('>> ')
        if song.lower().strip() == random_song[0].lower().strip():
            print(f'{style.GREEN} TAHNIAH! You have {tries - 1} percubaan lagi. anda mendapat {score + 5} markah.{style.RESET}')
            tries -= 1
            score += 5
            continue
        else:
            print(f'{style.RED} jawapan anda salah. percubaan anda {tries - 1} tinggal. Skor anda sekarang {score} markah.{style.RESET}')
            tries -= 1
            continue

        break
    except ValueError as error:
        print(error)

