import random
import turtle
t=turtle.Pen()

def losuj_slowo():
    return random.choice([
        'kalarepa', 'ziemniak', 'chleb', 'drogowskaz', 'dom', 'mazak'
    ])

def generuj_maske(slowo, podane_litery):
    maska = []
    for litera in slowo:
        if litera in podane_litery:
            maska.append(litera)
        else:
            maska.append('_')
    return maska 

def podaj_litere(stare_litery):
    while True:
        litera = input('Podaj literę: ')
        if not litera:
            print('ej, miałeś podać!')
        elif len(litera) > 1:
            print('nie, JEDNĄ literę')
        elif litera in stare_litery:
            print('OK, ale taką, której jeszcze nie nie było')
        else:
            return litera

def grafika(belk_szub):
    if belk_szub == 1:
        t.fd(150)
        t.back(75)
        t.left(90)
    if belk_szub == 2 or belk_szub == 3:
        t.fd(150)
    if belk_szub == 4:
        t.back(75)
        t.right(45)
        t.fd(106.06601717798213)
        t.right(45)
        t.up()
        t.back(75)
        t.down()
    if belk_szub == 5:
        t.fd(200)
    if belk_szub == 6:
        t.right(90)
        t.fd(75)
    if belk_szub == 7:
        t.right(90)
        t.circle(25)
    if belk_szub == 8:
        t.up()
        t.left(90)
        t.fd(50)
        t.down()
        t.fd(100)
    if belk_szub == 9:
        t.right(30)
        t.fd(40)
        t.back(40)
        t.left(60)
        t.fd(40)
        t.back(40)
        t.right(30)
        t.back(60)
    if belk_szub == 10:
        t.right(30)
        t.fd(40)
        t.back(40)
        t.left(60)
        t.fd(40)
        t.back(40)
        t.right(30)
        
def wisielec():
    slowo = losuj_slowo()
    slowo_s = set(slowo)
    podane_litery = set()
    belki_szubienicy = 0
    while True:
        maska = generuj_maske(slowo, podane_litery)
        print(' '.join(maska))
        litera = podaj_litere(podane_litery)
        podane_litery.add(litera)
        if litera not in slowo:
            belki_szubienicy += 1
            print('pudło') 
            grafika(belki_szubienicy)
        if belki_szubienicy == 10:
            print('wisisz')
            break
        if not (slowo_s - podane_litery):
            print('wygrales')
            break

if __name__ == '__main__':
    wisielec()         
