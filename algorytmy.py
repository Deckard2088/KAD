import random
from math import sqrt

from numpy.ma.core import minimum


#Funkcja do obliczania odległości między wektorami; jako argumenty przyjmuje dwa wektory;
#To w ilowymiarowej przestrzeni znajdują się owe wektory uzależnione jest od pierwszego wektora
#algorytm ten oblicza odległość Euklidesową
def odleglosc_miedzy_wektorami(a, b):
    liczbaWym = len(a)
    suma = 0
    for i in range(liczbaWym):
        suma += (a[i]- b[i])**2
    return sqrt(suma)

#funkcja obliczająca wektor ze średnimi danymi
def srednia_punkow(klaster):
    #pobieramy długość pierwszego wektora w klastrze
    dim = len(klaster[0])
    srednia_punkow = [
        sum(v[i] for v in klaster) / len(klaster)
        for i in range(dim)
    ]
    return srednia_punkow

#funkcja, która przeprowadza normalizację danych
def normalizacja(wektory):
    liczbaCech = len(wektory[0])
    # Tworzymy kopię, aby nie modyfikować danych wejściowych
    wynik = [list(w) for w in wektory]

    for k in range(liczbaCech):
        daneCechy = [w[k] for w in wektory]
        minimum = min(daneCechy)
        maksimum = max(daneCechy)

        #zabezpieczenie na wypadek gdyby dane były jednolite
        if maksimum == minimum:
            for w in wynik:
                w[k] = 0.5
        else:
            # każda dana zostaje odpowiednio przeskalowana
            for w in wynik:
                w[k] = (w[k] - minimum) / (maksimum - minimum)
    return wynik

#funkcja obliczająca WCSS
def oblicz_WCSS(klastry, centroidy):
    x = len(centroidy)
    suma = 0
    for i in range(x):
        for punkt in klastry[i]:
            d = odleglosc_miedzy_wektorami(centroidy[i], punkt)
            suma += d**2
    return suma

#implementacja algorytmu k-średnich
def k_srednie(irysy, liczba_klastrow):
    #Zebrane dane dotyczące pojedynczego irysu przekształcamy w wektor
    #tworzymy listę kluczy ze słownika dane, a zatem kluczami są nazwy cech irysów
    #deklarujemy wszystkie klastry
    klastry = [[] for i in range(liczba_klastrow)]

    #wybieramy k losowych wektorów (irysów), które będą centroidami
    centroidy = []
    wylosowane_indexy = random.sample(range(0, len(irysy)), liczba_klastrow)
    for i in range(liczba_klastrow):
        centroidy.append(irysy[wylosowane_indexy[i]])

    #zmienna pomocnicza do policzenia iteracji w pętli
    liczba_iteracji = 0
    while (1):
        #tworzymy kopię klastów, będzie nam potrzebna później
        kopiaKlastrow = [klaster.copy() for klaster in klastry]
        #na początku czyścimy oryginalną tablicę klastrów
        klastry = [[] for i in range(liczba_klastrow)]

        #przyrównujemy do których centroidów kolejne wektory mają najmniejszą odległość
        for irys in irysy:
            index_klastra = 0
            najmniejsza_odleglosc = odleglosc_miedzy_wektorami(centroidy[index_klastra], irys)
            for i in range(1, len(centroidy)):
                if najmniejsza_odleglosc > odleglosc_miedzy_wektorami(centroidy[i], irys):
                    index_klastra = i
                    najmniejsza_odleglosc = odleglosc_miedzy_wektorami(centroidy[index_klastra], irys)
            #wektor (irys) dodajemy do klastra o takim indeksie jak centroid dla którego odległość od wektora była najmniejsza
            klastry[index_klastra].append(irys)

        #aktualizujemy centroidy, od teraz wartość danego centroidu to średnia punktów należących do klastra
        for i in range(liczba_klastrow):
            #centroidy[i] = srednia_punkow(klastry[i])
            if len(klastry[i]) == 0:
                #zebezpieczenie na wypadek gdyby klaster okazał się pusty
                centroidy[i] = random.choice(irysy)
            else:
                centroidy[i] = srednia_punkow(klastry[i])

        liczba_iteracji += 1
        #jeśli po całej iteracji klastry nie uległy zmianie przerywamy pętlę, spełniony zostaje warunek stopu
        if kopiaKlastrow == klastry:
            break

    return klastry, centroidy, liczba_iteracji