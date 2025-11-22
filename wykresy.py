import matplotlib.pyplot as plt

def rysujKlastry(klastry, cecha_x, cecha_y):
    return

def rysujWykresyZGrupowaniem(klastry, centroidy):
    #w takiej kolejności występują dane w wektorach
    pary_cech = [
        ('Długość działki kielicha', 'Szerokość działki kielicha'),
        ('Długość działki kielicha', 'Długość płatka'),
        ('Długość działki kielicha', 'Szerokość płatka'),
        ('Szerokość działki kielicha', 'Długość płatka'),
        ('Szerokość działki kielicha', 'Szerokość płatka'),
        ('Długość płatka', 'Szerokość płatka')
    ]
    indeksy_par_cech = [
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 2),
        (1, 3),
        (2, 3)
    ]
    kolory = [
        '#FF0000'
        '#00FF00'
        '#0000FF'
        '#FFFF00'
        '#00FFFF'
        '#FF00FF'
    ]
    #przechodzimy po każdej parze cech (dla każdej pary osobny wykres)
    for i, j in indeksy_par_cech:
        fig, ax = plt.subplots(figsize=(10, 7))
        fig.suptitle('Współzależności pomiędzy cechami irysów', fontsize=16, fontweight='bold')
        #przechodzimy po każdym klastrze (dla każdego będzie inny kolor)
        for klaster in klastry:
            x = [punkt[i] for punkt in klaster]
            y = [punkt[j] for punkt in klaster]
            nazwa_cechy_x = pary_cech[i]
            nazwa_cechy_y = pary_cech[j]
            print(f"CECHY: {nazwa_cechy_x}, {nazwa_cechy_y}")
            print("Generowanie wykresu...")
            ax.scatter(x, y, alpha=0.6, s=30, color=kolory[0], edgecolor='black', linewidth=0.5)

            

    plt.show()