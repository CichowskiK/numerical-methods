import matplotlib.pyplot as plt
import numpy as np


epsilon = 1e-12    #dokładność obliczeń
b = [i for i in range(1, 201)]   #nasz wektor wyrazów wolnych

def check(d , y, b):   #sprawdzanie wyniku
    A = np.zeros((200, 200))
    A += np.diag([d] * 200)
    A += np.diag([0.5] * (199), 1)
    A += np.diag([0.5] * (199), -1)
    A += np.diag([0.1] * (198), 2)
    A += np.diag([0.1] * (198), -2)

    x = np.linalg.solve(A, b)

    return all(abs(a - b) <= 0.00001 for a, b in zip(x, y))

def gen_Jacob (d, x):
    x_back = [0]
    while abs(np.linalg.norm(x,1) - np.linalg.norm(x_back, 1)) > epsilon:
        x_back = x.copy()
        x[0] = (b[0] - 0.5*x_back[1] - 0.1*x_back[2])/d
        x[1] = (b[1] - 0.5*x_back[0] - 0.5*x_back[2] - 0.1*x_back[3])/d
        for i in range(2,198):
            x[i] = (b[i] - 0.1*x_back[i-2] -0.5*x_back[i-1] - 0.5*x_back[i+1] - 0.1*x_back[i+2])/d
        x[198] = (b[198] - 0.1*x_back[196] -0.5*x_back[197] - 0.5*x_back[199])/d
        x[199] = (b[199] - 0.1*x_back[197] -0.5*x_back[198])/d
        yield np.linalg.norm(x,1)
    print("Wynik metody Jacobiego:", x)
    if(check(d, x, b)):
        print("wynik poprawny")
    else:
        print("wynik niepoprawny")

def gen_Gauss_Seidel (d, x):
    x_back = [1]
    while abs(np.linalg.norm(x,1) - np.linalg.norm(x_back, 1)) > epsilon:
        x_back = x.copy()
        x[0] = (b[0] - 0.5*x_back[1] - 0.1*x_back[2])/d
        x[1] = (b[1] - 0.5*x[0] - 0.5*x_back[2] - 0.1*x_back[3])/d
        for i in range(2,198):
            x[i] = (b[i] - 0.1*x[i-2] -0.5*x[i-1] - 0.5*x_back[i+1] - 0.1*x_back[i+2])/d
        x[198] = (b[198] - 0.1*x[196] -0.5*x[197] - 0.5*x_back[199])/d
        x[199] = (b[199] - 0.1*x[197] -0.5*x[198])/d
        yield np.linalg.norm(x,1)
    print("\n\n\n\nWynik metody Gaussa-Seidela", x)
    if(check(d, x, b)):
        print("wynik poprawny")
    else:
        print("wynik niepoprawny")


d=2  #wartość d

y = [1]*200   #wektor początkowy
z=y.copy()
wyniki_Jac = list(gen_Jacob(d, y))

for i in range(len(wyniki_Jac)-1):
    wyniki_Jac[i] = abs(wyniki_Jac[-1] - wyniki_Jac[i])

plt.figure(figsize=(12, 6))
plt.title("Metoda Jacobiego")
plt.plot(range(len(wyniki_Jac)-2), wyniki_Jac[:-2],
         marker='o',
         linestyle='-',
          color="b")

plt.yscale('log')
plt.xlabel('Numer iteracji')
plt.ylabel('Różnica między przybliżeniem w danej iteracji, a wynikiem dokładnym')
plt.grid(True)
plt.show()


wyniki_Gaus = list(gen_Gauss_Seidel(d, z))

for i in range(len(wyniki_Gaus)-1):
    wyniki_Gaus[i] = abs(wyniki_Gaus[-1]-wyniki_Gaus[i])

plt.figure(figsize=(12, 6))
plt.title("Metoda Gaussa-Seidela")
plt.plot(range(len(wyniki_Gaus)-2), wyniki_Gaus[:-2],
        marker='o',
        linestyle='-',
        color="b")

plt.yscale('log')
plt.xlabel('Numer iteracji')
plt.ylabel('Różnica między przybliżeniem w danej iteracji, a wynikiem dokładnym')
plt.grid(True)
plt.show()
