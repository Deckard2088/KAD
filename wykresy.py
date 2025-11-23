import matplotlib.pyplot as plt

def rysujWykresyZGrupowaniem(klastry, centroidy):
    nazwy_cech = [
        'Długość działki kielicha',
        'Szerokość działki kielicha',
        'Długość płatka',
        'Szerokość płatka'
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
        '#FF0000',
        '#00FF00',
        '#0000FF',
        '#FFFF00',
        '#00FFFF',
        '#FF00FF'
    ]
    #przechodzimy po każdej parze cech (dla każdej pary osobny wykres)
    for i, j in indeksy_par_cech:
        fig, ax = plt.subplots(figsize=(10, 7))
        #fig.suptitle('Współzależności pomiędzy cechami irysów', fontsize=16, fontweight='bold')
        #przechodzimy po każdym klastrze (dla każdego będzie inny kolor)
        for k in range(len(klastry)):
            x = [punkt[i] for punkt in klastry[k]]
            y = [punkt[j] for punkt in klastry[k]]

            ax.set_xlabel(f'{nazwy_cech[i]} (cm)', fontsize=9)
            ax.set_ylabel(f'{nazwy_cech[j]} (cm)', fontsize=9)

            ax.scatter(
                    x, y,
                    #Przezroczystość punktu
                    alpha=0.6,
                    s=30,
                    color=kolory[k],
                    edgecolor='black',
                    linewidth=0.5)

            centroid = centroidy[k]
            ax.scatter(
                #współrzędne centroidu w przestrzni 2D
                centroid[i], centroid[j],
                #Rysuj centroid jako romb
                marker='D',
                s=200,
                #kolor taki sam jak kolor klastra
                color=kolory[k],
                #kolor konturu
                edgecolor='black',
                linewidth=1,
                label=f'Centroid {k + 1}'
            )
        ax.grid(alpha=0.3)
        ax.legend(fontsize=8)
        print("Generowanie wykresu...")
        plt.tight_layout()
        plt.savefig(f'wykres{i}_{j}.png', dpi=300, bbox_inches='tight')
        print(f"\nZapisano: wykres{i}_{j}.png")
        plt.show()
            

    plt.show()

def rysujWykresWCSS(zebraneWCSS):
    liczbaK = [x for x in range(2, 2 + len(zebraneWCSS))]

    fig, ax = plt.subplots(figsize=(10, 7))
    fig.suptitle('Zależność WCSS od liczby klastrów', fontsize=16, fontweight='bold')
    ax.set_xlabel("Liczba klastrów k")
    ax.set_ylabel("WCSS")
    ax.scatter(liczbaK, zebraneWCSS, color='blue', s=50, label='WCSS')
    ax.plot(liczbaK, zebraneWCSS, color='blue', linestyle='--')
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend()
    print("Generowanie wykresu...")
    plt.tight_layout()
    plt.savefig("ZaleznoscKlastryWCSS.png", dpi=300, bbox_inches='tight')
    print("ZaleznoscKlastryWCSS.png")
    plt.show()