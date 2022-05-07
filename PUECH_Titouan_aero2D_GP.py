
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches


"""Energie d'interaction déduite"""
    # taille de la fenêtre et grille
plt.figure(figsize=(12, 8), dpi=80)
plt.subplot(111)

    # Equations
X = np.linspace(0.5, 2.5, 256, endpoint=True)
Ea = -2*(1/X)**6
Er = (1/X)**12
Et = Ea + Er

    # Affichage
plt.title('Graphique du Potentiel de Lennard Jones')
plt.grid(True)

    # titre axe
plt.ylabel("E0/epsilon")
plt.xlabel("r/r0")

    # Affichage courbe
Et, = plt.plot(X, Et, color="green", linewidth=2.5, linestyle="-", label="Energie totale")
Ea, = plt.plot(X, Ea, color="red", linewidth=2.5, linestyle="-", label="Energie attractive")
Er, = plt.plot(X, Er, color="blue", linewidth=2.5, linestyle="-", label="Energie répulsive")

    # graduation x
plt.xlim(0.5, 2.5)
plt.xticks(np.linspace(0.5, 2.5, 5, endpoint=True))

    # graduation y
plt.ylim(-1.5, 1.5)
plt.yticks(np.linspace(-1.5, 1.5, 7, endpoint=True))

    # background color
plt.axvspan(0.5, 1.0, facecolor='lightpink', alpha=0.5)
plt.axvspan(1.0, 2.0, facecolor='lightblue', alpha=0.5)
plt.axvspan(2.0, 2.5, facecolor='lightgreen', alpha=0.5)

    # background legend
patch1 = mpatches.Patch(color='lightpink', label='zone répulsive')
patch2 = mpatches.Patch(color='lightblue', label='zone attractive')
patch3 = mpatches.Patch(color='lightgreen', label='zone sans interaction')
legend = plt.legend(handles=[Et, Ea, Er, patch1, patch2, patch3], loc=1)

    # Flèches
plt.annotate("", xy=(0.5, 0.2), xytext=(1.0, 0.2), arrowprops=dict(arrowstyle="<->"), )
plt.annotate("", xy=(1.0, 0.0), xytext=(1, -1.0), arrowprops=dict(arrowstyle="<->"), )
plt.text(0.7, .22, r'r=r0')
plt.text(1.01, -.25, r"position d'équilibre")

plt.show()



"""Force d'interaction intermoléculaire"""

    # taille de la fenêtre et grille
plt.figure(figsize=(12, 8), dpi=80)
plt.subplot(111)

    # Equations
X = np.linspace(0.5, 2.5, 256, endpoint=True)
Fa = -12/X**7
Fr = 12/X**13
Ft = Fa + Fr

    # Affichage
plt.title('Graphique de la force d\'intéraction intermoléculaire')
plt.grid(True)

    # titre des axes
plt.ylabel("F/F0")
plt.xlabel("r/r0")

Ft, = plt.plot(X, Ft, color="green", linewidth=2.5, linestyle="-", label="Force totale")
Fa, = plt.plot(X, Fa, color="red", linewidth=2.5, linestyle="-", label="Force attractive")
Fr, = plt.plot(X, Fr, color="blue", linewidth=2.5, linestyle="-", label="Force répulsive")
first_legend = plt.legend(handles=[Ft, Fa, Fr], loc=1)
plt.gca().add_artist(first_legend)

    # graduation x
plt.xlim(0.5, 2.5)
plt.xticks(np.linspace(0.5, 2.5, 5, endpoint=True))

    # graduation y
plt.ylim(-6.0, 6.0)
plt.yticks(np.linspace(-6.0, 6.0, 7, endpoint=True))

    # background color
plt.axvspan(.5, 1.0, facecolor='orange', alpha=0.5)

    # background legend
patch = mpatches.Patch(color='pink')
    

plt.show()




"""Représentation mathématique de l'équation des gaz parfait """

    # taille de la fenêtre et grille
plt.figure(figsize=(12, 8), dpi=80)
plt.subplot(111)

    # Equations
X = np.linspace(-5, 5, 256, endpoint=True)
Y1 = 100/X
Y2 = 200/X
Y3 = 400/X

    # Affichage
plt.title('Graphique de l\'équation des gaz parfaits')
plt.grid(True)

    # titre axes
plt.xlabel("Volume")
plt.ylabel("Pression")

Y1, = plt.plot(X, Y1, color="blue", linewidth=2.5, linestyle="-", label="Température 1")
Y2, = plt.plot(X, Y2, color="green", linewidth=2.5, linestyle="-", label="Température 2")
Y3, = plt.plot(X, Y3, color="red", linewidth=2.5, linestyle="-", label="Température 3")


    # graduation x
plt.xlim(-5, 5)
plt.xticks(np.linspace(-5, 5, 11, endpoint=True))

    # graduation y
plt.ylim(-2000.0, 2000)
plt.yticks(np.linspace(-2000, 2000, 9, endpoint=True))

    # background
rect1 = plt.Rectangle((0, 0), 5, 2000, color='pink', label='Domaine de définition physique')
plt.gca().add_artist(rect1)
legend = plt.legend(handles=[Y1, Y2, Y3, rect1], loc=1)

plt.show()




"Représentation mathématique de Van Der Waals"

    # taille de la fenêtre
plt.figure(figsize=(12, 8), dpi=80)
plt.subplot(111)

    # Equations
X = np.linspace(-10, 10, 256, endpoint=True)

a = 1
b = 4

Y1 = 0.2/(X-b) - a/(X**2)
Y2 = 0.1/(X-b) - a/(X**2)
Y3 = 0.02/(X-b) - a/(X**2)

    # Affichage
plt.title('Graphique de l\'équation de Van Der Waals')
plt.grid(True)

    # titre axes
plt.xlabel("Volume")
plt.ylabel("Pression")

Y1, = plt.plot(X, Y1, color="purple", linewidth=2.5, linestyle="-", label="k = 0.2")
Y2, = plt.plot(X, Y2, color="blue", linewidth=2.5, linestyle="-", label="k = 0.1")
Y3, = plt.plot(X, Y3, color="green", linewidth=2.5, linestyle="-", label="k = 0.02")

    # graduation x
plt.xlim(-10, 10)
plt.xticks(np.linspace(-10, 10, 11, endpoint=True))

    # graduation y
plt.ylim(-0.4, 0.2)
plt.yticks(np.linspace(-3, 3, 7, endpoint=True))

    # background
rect1 = plt.Rectangle((4, 0), 10, 3, color='pink', label='Domaine de définition physique')
plt.gca().add_artist(rect1)
second_legend = plt.legend(handles=[Y1, Y2, Y3, rect1], loc=2)

plt.show()



"Isotherme d'un gaz parfait et d'un gaz de Van Der Waals (P en fonction de V)"

    #taille de la fenêtre et grille
plt.figure(figsize=(12,8), dpi=80)
plt.subplot(111)

    #Equation Gaz Parfait
Lx = list()
LGP = []
x = 0
R = 8.314

while x < 10 * (10 ** (-4)):
    x = x + (0.5 * (10 ** (-4)))
    Lx.append(x)


for T in range(300, 1500, 200):
    Ly = list()
    for x in Lx:
        y = (R * T) / x
        Ly.append(y)

    LGP.append(plt.plot(Lx, Ly, 'orange'))



    #Equation Wan Der Waals
LWDW = []
a = 363.7 * (10 ** (-3))
b = 0.0427 * (10 ** (-3))
for T1 in range(300, 1500, 200):
    Ly1 = list()
    for x1 in Lx:
        y1 = ((R * T1) / (x1 - b)) - (a / (x1 ** 2))
        Ly1.append(y1)

    LWDW.append(plt.plot(Lx, Ly1, 'blue'))


for i in range(0, 6):
    LGP[i]
    LWDW[i]


patch1 = mpatches.Patch(color='blue', label='Van der Waals')
patch2 = mpatches.Patch(color='orange', label='Gaz Parfait')
plt.legend(handles=[patch1, patch2], loc=1)

    #Affichage
plt.title("Réseau d'isotherme d'un gaz parfait et d'un gaz de Van Der Waals (P en fonction de V)")
plt.grid(True)

    #titre axes
plt.xlabel("Volume")
plt.ylabel("Pression")

plt.axis([0,10*10**(-4),0,3*10**7])

plt.show()


"Isotherme d'un gaz parfait et d'un gaz de Van Der Waals (P en fonction de T)"
    # taille de la fenêtre et grille
plt.figure(figsize=(12, 8), dpi=80)
plt.subplot(111)

    # déclaration des variables
Lx = [i for i in range(300, 1500, 200)]
Lv = list()

LGP = []
vdw = []

v = 0
R = 8.314
a = 363.7 * 10 ** (-3)
b = 0.0427 * 10 ** (-3)

while v < 10 * 10 ** (-4):
    v = v + 2 * (10 ** (-4))
    Lv.append(v)


for V in Lv:
    Ly = list()
    for x in Lx:
        y = R * x / V
        Ly.append(y)

    LGP.append(plt.plot(Lx, Ly, 'orange'))
LGP.append(plt.plot(Lx, Ly, 'orange', label=r"Gaz parfait"))

    # Equation de Van Der Waals
for V1 in Lv:
    Ly1 = list()
    for x in Lx:
        y1 = R * x / (V1 - b) - (a / V1 ** 2)
        Ly1.append(y1)

    vdw.append(plt.plot(Lx, Ly1, 'blue'))
vdw.append(plt.plot(Lx, Ly1, 'blue', label=r"Van Der Waals"))

for i in range(0, 5):
    LGP[i]
    vdw[i]

    # légende
patch1 = mpatches.Patch(color='orange', label='Van der Waals')
patch2 = mpatches.Patch(color='blue', label='Gaz Parfait')
plt.legend(handles=[patch1, patch2], loc=1)

    # Affichage
plt.title("Graphique du réseau d'isotherme d'un gaz parfait et d'un gaz de Van Der Waals (P en fonction de T)")
plt.grid(True)

    # titre axes
plt.xlabel("Volume")
plt.ylabel("Pression")

plt.axis([300, 1200, 0, 7*10**7])

plt.show()




"Coordonnées d'Amagat (PV en fonction de P) Parabole de Mariotte, Gaz de Van der Waals: CO2"

    # taille de la fenêtre et grille
plt.figure(figsize=(12, 8), dpi=80)
plt.subplot(111)

    # initialisation des variables
LWDW = []
LGP = []
Lv = []

v = 0
R = 8.315
a = 363.7 * 10 ** (-3)
b = 0.0427 * 10 ** (-3)

while v < 1 * 10 ** (-3):
    v = v + 0.05 * 10 ** (-3)
    Lv.append(v)


    # Equation Gaz Parfait
for T in range(300, 1300, 200):
    Ly = []
    Lx = []
    for i in Lv:
        p = R*T/(i - b) - a/i ** 2
        Lx.append(p)
        y = p*i
        Ly.append(y)
    LGP.append(plt.plot(Lx, Ly, 'blue'))


    # Equation Wan Der Waals
for T1 in range(300, 1300, 200):
    Ly1 = []
    Lx1 = []

    for i in Lv:
        Y1 = R*T1/i
        Lx1.append(Y1)
        y1 = Y1*i
        Ly1.append(y1)
    LWDW.append(plt.plot(Lx1, Ly1, 'orange'))

patch1 = mpatches.Patch(color='orange', label='Van der Waals')
patch2 = mpatches.Patch(color='blue', label='Gaz Parfait')
first_legend = plt.legend(handles=[patch1, patch2], loc=1)
plt.gca().add_artist(first_legend)

    # parabole de Mariotte
Lh = []
Lp = []
h = 0
while h < 9*10 ** 3:
    h = h + 0.05*10**3
    Lh.append(h)


for PV in Lh:
    P = (-b*PV**2 + a*PV)/(2*a*b)
    Lp.append(P)

plt.plot(Lp, Lh, 'green', label='température de Mariotte')
second_legend = plt.legend(loc=4)

plt.title('Graphique des coordonnées d\'Amagat (PV en fonction de P) \nParabole de Mariotte, Gaz de Van der Waals: CO2')
plt.xlabel('P')
plt.ylabel('PV')
plt.axis([0, 2.5*10**7, 0, 9*10**3])
plt.grid(True)

plt.show()





"Equation réduite de Van-der-Waals en coordonnées de Clapeyron"
    # taille de la fenêtre et grille
plt.figure(figsize=(12, 8), dpi=80)
plt.subplot(111)

    # Equations
X = np.linspace(0.4, 2., 256, endpoint=True)
Y1 = 8*1/(3*X-1)-3/X**2
Y2 = 8*1.01/(3*X-1)-3/X**2
Y3 = 8*1.02/(3*X-1)-3/X**2
Y4 = 8*1.03/(3*X-1)-3/X**2
Y5 = 8*.99/(3*X-1)-3/X**2
Y6 = 8*.98/(3*X-1)-3/X**2
Y7 = 8*.97/(3*X-1)-3/X**2

    # affichage des équations
Y4, = plt.plot(X, Y4, color="yellow", linewidth=2.5, linestyle="-", label="Tr=1.03")
Y3, = plt.plot(X, Y3, color="orange", linewidth=2.5, linestyle="-", label="Tr=1.02")
Y2, = plt.plot(X, Y2, color="blue", linewidth=2.5, linestyle="-", label="Tr=1.01")
Y1, = plt.plot(X, Y1, color="magenta", linewidth=2.5, linestyle="-", label="Tr=1.")
Y5, = plt.plot(X, Y5, color="grey", linewidth=2.5, linestyle="-", label="Tr=.99")
Y6, = plt.plot(X, Y6, color="cyan", linewidth=2.5, linestyle="-", label="Tr=.98")
Y7, = plt.plot(X, Y7, color="red", linewidth=2.5, linestyle="-", label="Tr=.97")
plt.legend()


plt.xlabel('Volume réduit')
plt.ylabel('Pression réduite')
plt.title('Graphique de l\'équation réduite de Van-der-Waals en coordonnées de Clapeyron')
plt.grid(True)

    # graduation x
plt.xlim(.4, 2.)
plt.xticks(np.linspace(0.4, 2., 9, endpoint=True))

    # graduation y
plt.ylim(.8, 1.4)
plt.yticks(np.linspace(.8, 1.4, 7, endpoint=True))

    #Flêche
plt.annotate("", xy=(.9, 1.), xytext=(1.1, 1.),
            arrowprops=dict(arrowstyle="<->"), )
plt.text(.95, 1.01, r'point fixe')

plt.show()