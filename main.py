#algorytm k-srednich zaimplementowany w osobnym module
import algorytmy

#funkcja wczytująca dane z pliku, dane reprezentujące daną cechę kwiatów są zebrane w osobnych listach
def wczytaj_dane_iris_plik(nazwa_pliku):
    nazwy_cech = ['Długość działki kielicha', 'Szerokość działki kielicha',
                  'Długość płatka', 'Szerokość płatka']
    #Przygotowanie struktur na dane, tworzymy słownik z listami - dla każdej cechy osobna lista
    wszystkie_dane = {nazwa: [] for nazwa in nazwy_cech}
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
            for i, nazwa_cechy in enumerate(nazwy_cech):
                #do odpowiedniej listy dodajemy odpowiednie dane
                wszystkie_dane[nazwa_cechy].append(wartosci[i])
    return wszystkie_dane, nazwy_cech

#zrób drugą wersję wczytywania danych zwracając po prostu wektory
def rysuj_wykresy(dane, nazwy_cech):
    return

def main():
    print("\n" + "=" * 80)
    print("GRUPOWANIE DANYCH METODĄ K-ŚREDNICH NA PRZYKŁADZIE ZBIORU DANYCH IRYSÓW")
    print("na 5 impelemntacja")
    print("=" * 80)

    dane, nazwy_cech = wczytaj_dane_iris_plik("data2.csv")
    dane_znormalizowane = algorytmy.normalizacja(dane)

    print("\nGRUPOWANIE DLA RÓŻNEJ LICZBY KLASTRÓW k")
    for i in range(2, 11, 1):
        klastry, centroidy, iteracje = algorytmy.k_srednie(dane_znormalizowane, i)
        wcss = algorytmy.oblicz_WCSS(klastry, centroidy)
        print(f"DLA k={i}: \n-liczba iteracji: {iteracje}; \n-WCSS: {wcss:.4f};\n")

    print("\n" + "=" * 80)
    print("GRUPOWANIE ZAKOŃCZONE")
    print("=" * 80)

if __name__ == "__main__":
    main()