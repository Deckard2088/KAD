#algorytm k-srednich zaimplementowany w osobnym module
import algorytmy
#algorytmy do wykresów zaimplementowane w osobnym module
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

#funkcja pomocnicza zwracająca najlepsze grupowanie (domyślnie z 10 prób)
def znajdz_najlepsze_grupowanie(dane_znormalizowane, k, liczba_prob=10):
    #Uruchamia algorytm k-średnich wielokrotnie i zwraca najlepsze grupowanie (to z najmniejszym WCSS)
    #ustwawiamy najmniejsze WCSS na nieskończoność
    min_wcss = float('inf')
    najlepsze_klastry = None
    najlepsze_centroidy = None
    najlepsze_iteracje = 0

    for _ in range(liczba_prob):
        klastry, centroidy, iteracje = algorytmy.k_srednie(dane_znormalizowane, k)
        wcss = algorytmy.oblicz_WCSS(klastry, centroidy)

        if wcss < min_wcss:
            min_wcss = wcss
            najlepsze_klastry = klastry
            najlepsze_centroidy = centroidy
            najlepsze_iteracje = iteracje

    return najlepsze_klastry, najlepsze_centroidy, najlepsze_iteracje, min_wcss

def main():
    print("\n" + "=" * 80)
    print("GRUPOWANIE DANYCH METODĄ K-ŚREDNICH NA PRZYKŁADZIE ZBIORU DANYCH IRYSÓW")
    print("na 5 impelemntacja")
    print("=" * 80)

    #Wczytujemy dane i przeprowadzamy ich normalizacje
    dane = wczytaj_dane_iris_plik("data2.csv")
    dane_znormalizowane = algorytmy.normalizacja(dane)

    #klastryZnorm, centroidyZnorm, iteracjeZnorm = algorytmy.k_srednie(dane_znormalizowane, 3)
    #klastryDoWykresu, centroidyDoWykresu = algorytmy.mapujNaOryginalne(dane, klastryZnorm, centroidyZnorm)
    najlepsze_klastry, najlepsze_centroidy, najlepsze_iteracje, min_wcss = znajdz_najlepsze_grupowanie(
        dane_znormalizowane, 3)
    #przed narysowaniem wykresów mapujemy dane, które zostały znormalizowane z powrotem na oryginalne dane
    klastry_do_wykresu, centroidy_do_wykresu = algorytmy.mapujNaOryginalne(
        dane, najlepsze_klastry, najlepsze_centroidy
    )
    wykresy.rysujWykresyZGrupowaniem(klastry_do_wykresu, centroidy_do_wykresu)

    dane = wczytaj_dane_iris_plik("data2.csv")
    dane_znormalizowane = algorytmy.normalizacja(dane)


    print("=" * 80)
    print("\nGRUPOWANIE DLA RÓŻNEJ LICZBY KLASTRÓW k\n")
    print(f"|{'Liczba klastrów k':>16} | {'Liczba iteracji':>16} | {'WCSS':>8} |")
    print("|"+"-" * 18 + "|" + "-"*18 + "|" + "-"*10 + "|")
    #minWcss = 0
    tabelaWCSS = []
    for k in range(2, 11, 1):
        #powtarzamy sobie algorytm kilka razy żeby uzyskać jak najmniejsze WCSS
        najlepsze_klastry, najlepsze_centroidy, najlepsze_iteracje, minWcss = znajdz_najlepsze_grupowanie(
            dane_znormalizowane, k
        )
        tabelaWCSS.append(minWcss)

        print(f"| {k:>16} | {najlepsze_iteracje:>16} | {minWcss:>8.2f} |")
        print("|"+"-" * 18 + "|" + "-"*18 + "|" + "-"*10 + "|")

    wykresy.rysujWykresWCSS(tabelaWCSS)
    print("\n" + "=" * 80)
    print("GRUPOWANIE ZAKOŃCZONE")
    print("=" * 80)

if __name__ == "__main__":
    main()