import random


def losuj_slowo():
    return random.choice([
        'kalarepa', 'ziemniak', 'chleb', 'drogowskaz', 'bleble', 'bobek'
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
        if belki_szubienicy == 10:
            print('wisisz')
            break
        if not (slowo_s - podane_litery):
            print('wygrales')
            break

if __name__ == '__main__':
    wisielec()         