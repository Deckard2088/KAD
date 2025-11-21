import random
from math import sqrt

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
def normalizacja(dane):
    klucze = dane.keys()
    wynik = {}
    for k in klucze:
        minimum = min(dane[k])
        maksimum = max(dane[k])
        #każda dana zostaje odpowiednio przeskalowana
        wynik[k] = [(x - minimum) / (maksimum - minimum) for x in dane[k]]
    return wynik

def denomalizacja(dane):
    return

#funkcja obliczająca WCSS
def oblicz_WCSS(klastry, centroidy):
    x = len(centroidy)
    suma = 0
    for i in range(x):
        for klaster in klastry[i]:
            d = odleglosc_miedzy_wektorami(centroidy[i], klaster)
            suma += d**2
    return suma

#implementacja algorytmu k-średnich
def k_srednie(dane, liczba_klastrow):
    #Zebrane dane dotyczące pojedynczego irysu przekształcamy w wektor
    #tworzymy listę kluczy ze słownika dane, a zatem kluczami są nazwy cech irysów
    klucze = list(dane.keys())
    #tworzymy liste irysy, złożoną z krotek utworzonych w wyniku użycia zipa
    #zip łączy elementy z kilku iterowalnych obiektów w krotki element-po-elemencie.
    irysy = list(zip(*(dane[i] for i in klucze)))
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