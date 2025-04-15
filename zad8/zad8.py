import numpy as np
import matplotlib.pyplot as plt

ODCHYLENIE_STANDARDOWE = 0.5

def phi1(x):
    return x**2

def phi2(x):
    return x

def phi3(x):
    return np.sin(x * np.pi)

def phi4(x):
    return np.exp(x)

def F(x):
    return 2*phi1(x) + 2*phi2(x) + phi3(x) - phi4(x)

def F_zaburzone(x, n):
    return F(x) + np.random.normal(0, ODCHYLENIE_STANDARDOWE, n)

def aproksymacja(x_array, y_array):
    phi_functions = [phi1, phi2, phi3, phi4]
    s= len(phi_functions)
    n= len(x_array)
    A = np.zeros((n, s))
    for k in range(n):
        for j in range(s):
            A[k, j] = phi_functions[j](x_array[k])

    G = np.zeros((n, n))
    np.fill_diagonal(G, ODCHYLENIE_STANDARDOWE)

    G_odwrocone = np.zeros((n, n))
    np.fill_diagonal(G_odwrocone, 1/ODCHYLENIE_STANDARDOWE)

    LHS = A.T @ G_odwrocone @ A
    RHS = A.T @ G_odwrocone @ y_array

    p = np.linalg.pinv(LHS) @ RHS

    return p 

def wykres(n) :
    x= np.linspace(-2.5,2.5,300)
    siatka_x= np.linspace(-2.5,2.5, n)
    wartosc_dokladna = F(np.array(x))
    wartosc_zaburzona = F_zaburzone(np.array(siatka_x), n)

    współczynniki = aproksymacja(siatka_x, wartosc_zaburzona)
    wartosc_aproksymacji= współczynniki[0] * phi1(np.array(x)) + współczynniki[1] * phi2(np.array(x)) + współczynniki[2] * phi3(np.array(x)) + współczynniki[3] * phi4(np.array(x))

    print("Wektor wygenerowanych współczynników: ", współczynniki)
    print("Łączna róznica między faktycznymi współczynnikami a wygenerowanymi jest równa", np.linalg.norm([2, 2, 1, -1]- współczynniki, ord=1))

    plt.figure(figsize=(8, 6))

    plt.plot(x, wartosc_dokladna, color='red', linewidth=2, label='Orginalna funkcja')
    plt.plot(siatka_x, wartosc_zaburzona, 'gx', label="Punkty")
    plt.plot(x, wartosc_aproksymacji, color='blue', linewidth=2, label='Wynik aproksymacji', linestyle='-.')

    plt.legend()
    plt.grid()
    plt.title(f'Aproksymacja dla {n} punktów i odchylenia standardowego = {ODCHYLENIE_STANDARDOWE}')
    plt.ylim(-3, 7)
    plt.xlim(-3,3)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.savefig(f"wykres{n}.png")
    plt.text(0, -4.2, f"Wygenerwoane współczynniki: {współczynniki}", ha='center', va='center', fontsize=12)    
    plt.show()

wykres(5)