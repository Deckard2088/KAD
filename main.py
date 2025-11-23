#algorytm k-srednich zaimplementowany w osobnym module
import algorytmy
from sklearn.cluster import KMeans

import wykresy


#funkcja wczytująca dane z pliku, dane reprezentujące daną cechę kwiatów są zebrane w osobnych listach
def wczytaj_dane_iris_plik(nazwa_pliku):
    #Przygotowanie struktur na dane, tworzymy słownik z listami - dla każdej cechy osobna lista
    wszystkie_dane = []
    #otwieramy wskazany nazwą plik w trybie read, po wyjściu z bloku with plik się zamyka automatycznie
    with open(nazwa_pliku, "r") as f:
        #odczytujemy plik linia po linii
        for linia in f:
            #jeśli linia jest pusta to ją pomijamy
            if linia.strip() == "":
                continue
            #tworzymy tablicę floatów 'wartości' w której znajdują się dane z pojedynczej linii
            #dane te powstały na skutek podziału tej linijki (separatorem jest tutaj przecinek
            wartosci = [float(x) for x in linia.strip().split(",")]
            wszystkie_dane.append(wartosci)
    #Na koniec otrzymujemy tablicę zawierającą waktory, gdzie pojedyczny wektor zawiera dane jednego irysu
    return wszystkie_dane


def main():
    print("\n" + "=" * 80)
    print("GRUPOWANIE DANYCH METODĄ K-ŚREDNICH NA PRZYKŁADZIE ZBIORU DANYCH IRYSÓW")
    print("na 5 impelemntacja")
    print("=" * 80)

    dane = wczytaj_dane_iris_plik("data2.csv")
    dane_znormalizowane = algorytmy.normalizacja(dane)

    klastryZnorm, centroidyZnorm, iteracjeZnorm = algorytmy.k_srednie(dane_znormalizowane, 3)
    klastryDoWykresu, centroidyDoWykresu = algorytmy.mapujNaOryginalne(dane, klastryZnorm, centroidyZnorm)
    #wykresy.rysujWykresyZGrupowaniem(klastryDoWykresu, centroidyDoWykresu)

    dane = wczytaj_dane_iris_plik("data2.csv")
    dane_znormalizowane = algorytmy.normalizacja(dane)


    print("=" * 80)
    print("\nGRUPOWANIE DLA RÓŻNEJ LICZBY KLASTRÓW k\n")
    print(f"|{'Liczba klastrów k':>16} | {'Liczba iteracji':>16} | {'WCSS':>8} |")
    print("|"+"-" * 18 + "|" + "-"*18 + "|" + "-"*10 + "|")
    minWcss = 0
    tabelaWCSS = []
    for k in range(2, 11, 1):
        #powtarzamy sobie algorytm kilka razy żeby uzyskać jak najmniejsze WCSS
        klastry, centroidy, iteracje = algorytmy.k_srednie(dane_znormalizowane, k)
        wcss = algorytmy.oblicz_WCSS(klastry, centroidy)
        minWcss = wcss
        finalIteracje = iteracje
        for j in range(10):
            klastry, centroidy, iteracje = algorytmy.k_srednie(dane_znormalizowane, k)
            wcss = algorytmy.oblicz_WCSS(klastry, centroidy)
            if minWcss > wcss:
                minWcss = wcss
                finalIteracje = iteracje
        tabelaWCSS.append(minWcss)

        print(f"| {k:>16} | {finalIteracje:>16} | {minWcss:>8.4f} |")
        print("|"+"-" * 18 + "|" + "-"*18 + "|" + "-"*10 + "|")

    wykresy.rysujWykresWCSS(tabelaWCSS)
    print("\n" + "=" * 80)
    print("GRUPOWANIE ZAKOŃCZONE")
    print("=" * 80)

if __name__ == "__main__":
    main()