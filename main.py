#### Fonctions secondaires

# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure(
        {
            "layout": {
                "title": {"text": title},
                "xaxis": {"title": {"text": "x"}},
                "yaxis": {"title": {"text": "y"}},
            }
        }
    )

    x = [i for i in range(len(lsyr))]
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color="blue")
    fig.add_trace(t)
    fig.show()
    return None
#######################

def syracuse_l(n):
    """Retourne la suite de Syracuse de source n.

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """
    if n <= 0:
        return []

    l = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        l.append(n)
    return l


def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """
    if not l:
        return 0
    return len(l) - 1


def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """
    if not l:
        return 0
    source = l[0]
    return sum(1 for v in l[1:] if v > source)


def altitude_maximale(l):
    """Retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """
    if not l:
        return 0
    return max(l)


#### Fonction principale
def main():
    # quelques tests
    for n in [1, 2, 3, 6, 15]:
        lsyr = syracuse_l(n)
        print(f"\nn = {n}")
        print("  suite:", lsyr)
        print("  temps_de_vol:", temps_de_vol(lsyr))
        print("  temps_de_vol_en_altitude:", temps_de_vol_en_altitude(lsyr))
        print("  altitude_maximale:", altitude_maximale(lsyr))

    # Affichage graphique pour un cas
    lsyr = syracuse_l(15)
    syr_plot(lsyr)


if __name__ == "__main__":
    main()
