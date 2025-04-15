import numpy as np
import matplotlib.pyplot as plt

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    lower_index = -1 

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] < target:
            lower_index = mid
            left = mid + 1
        else:
            right = mid - 1

    return lower_index

def y(x):
    return 1 / (1 + 10 * x**2)

def siatka(n):
    for i in range(n+1):
        x = -1 + 2*i/n
        yield x

def interpolacja_lagrangea(n):
    x=list(siatka(n))
    f=y(np.array(x))
    x_axis= np.linspace(-1, 1, 300)
    result = np.zeros_like(x_axis)
    for i in range(n+1):
        l = np.ones_like(x_axis)
        for j in range(n+1):
            if i != j:
                l *= (x_axis - x[j]) / (x[i] - x[j]) 
        result += f[i] * l 
    return result

def cholesky(n):
    C = []
    pod_diag = np.zeros(n)
    diag = np.zeros(n)
    C.append(pod_diag)
    C.append(diag)

    for i in range(n):
        if i == 0:
            C[1][i] = 2
        else:
            C[0][i] = 1 / C[1][i - 1]
            C[1][i] = np.sqrt(4 - C[0][i]**2)
    return C

def splajn_kubiczny(n):
    h=2/n
    x=list(siatka(n))
    f=y(np.array(x))
    x_axis= np.linspace(-1, 1, 300)
    ksi= np.zeros_like(x)

    ############### liczymy ksi ####################################################

    CH=cholesky(n)
    wspolczynnik = 6 / (h ** 2)

    ksi[1] = (wspolczynnik * (f[0] - 2 * f[1] + f[2]) / CH[1][0])
    for i in range(2, n):
        ksi[i] = (wspolczynnik * (f[i - 1] - 2 * f[i] + f[i + 1]) - CH[0][i - 1] * ksi[i - 1]) / CH[1][i - 1]

    ksi[n - 1] = ksi[n - 1] / CH[1][n - 2]
    for i in range(n - 2, 0, -1):
        ksi[i] = (ksi[i] - CH[0][i] * ksi[i + 1]) / CH[1][i - 1]

    ################# splajny ###############################
    result = []

    for i in range(len(x_axis)):
        j = binary_search(x, x_axis[i])
        A = (x[j+1] - x_axis[i]) / (x[j+1] -x[j])
        B = (x_axis[i] - x[j]) / (x[j+1] -x[j])
        C = ((A**3 - A)*(((x[j+1] -x[j]))**2))/6
        D = ((B**3 - B)*(((x[j+1] -x[j]))**2))/6
        wynik = A*f[j] + B*f[j+1] + C*ksi[j] + D*ksi[j+1]

        result.append(wynik)
    
    return result

def wykres(n):
    x= np.linspace(-1,1,300)
    orginalna_funkcja = y(np.array(x))
    funkcja_interpolacji = interpolacja_lagrangea(n)
    funkcja_sklejana = splajn_kubiczny(n)

    plt.figure(figsize=(10, 6))

    plt.plot(x, orginalna_funkcja, color='red', linewidth=2, label='Orginalna funkcja')
    plt.plot(x, funkcja_interpolacji, color='blue', linewidth=2, label='Interpolacja Lagrange\'a', linestyle="--")
    plt.plot(x, funkcja_sklejana, color='green', linewidth=2, label='Splajny kubiczne', linestyle="--")

    plt.legend()
    plt.grid()
    plt.title(f'Porównanie interpolacji wielomianowej i splajnów kubicznych dla {n+1} węzłów')
    plt.ylim(-0.5, 2)
    plt.xlabel("x")
    plt.ylabel("y")
    #plt.savefig(f"wykres{n+1}.png")        
    plt.show()
    blad(x, n, orginalna_funkcja, funkcja_interpolacji, funkcja_sklejana)

def blad(x, n, orginalna, lagrange, splajn):

    blad_splajn = np.abs(np.array(orginalna) - np.array(splajn))
    blad_lagrange = np.abs(np.array(orginalna) - np.array(lagrange))
    wezly = np.array(list(siatka(n)))

    plt.figure(figsize=(10, 6))

    plt.plot(x, blad_lagrange, color='red', linewidth=2, label='Błąd interpolacji Lagrange\'a')
    plt.plot(x, blad_splajn, color='blue', linewidth=2, label='Błąd splajnów')
    plt.plot(wezly, [0] * (n +1), 'go', label="Węzły interpolacji")

    plt.legend()
    plt.grid()
    plt.title(f'Porównanie będu interpolacji wielomianowej i splajnów kubicznych dla {n+1} węzłów')
    plt.ylim(-0.1, 2)
    plt.xlabel("x")
    plt.ylabel("Błąd")
    #plt.savefig(f"blad{n+1}.png")        
    plt.show()

    print("Największy błąd interpolacji Lagrange\'a = ", np.max(blad_lagrange))
    print("Największy błąd splajnów = ", np.max(blad_splajn))


wykres(10)
