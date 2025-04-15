import math
import matplotlib.pyplot as plt
import time
import numpy as np

def check(n , y, b):
    A = np.ones((n, n))
    A += np.diag([4] * n)
    A += np.diag([2] * (n - 1), 1)

    x = np.linalg.solve(A, b)

    return all(abs(a - b) <= 0.00001 for a, b in zip(x, y))  #porównujemy je z pewną tolerancją biorąc pod uwage to że może iiny błąd zaokrąglenia przez liczenie różnymi metodami

def sherman(n):
    M = []
    M.append([4]*n)
    M.append([2]*(n-1) + [0])
    b = [2]*n
    y=[]

    start =time.time()

    z = [0]*n
    q = [0]*n
    z[n-1] = b[n-1] / M[0][n-1]
    q[n-1] = 1 / M[0][n-1]

    for i in range(n - 2, -1, -1):
        z[i] = (b[n-2] - M[1][i] * z[i+1]) / M[0][i]
        q[i] = (1 - M[1][i] * q[i+1]) / M[0][i]

    suma = sum(z)/(1+sum(q))
        

    for i in range(n):
        y.append(z[i] - suma*q[i])
    
    finalTime =time.time() - start

    #if (check(n, y, b)):          #algorytm sprawdzający
    #    print("wynik poprawny")
    #else:
    #    print("wynik nie poprawny")

    print(y)
    return finalTime
    

sherman(120)


#rysowanie wykresu, trzeba pamiętać że nie możemy wtedy uruchamiac algorytmu sprawdzającego bo wtedy złożonośc tego algorytmu O(N^3) zostanie zsumowana z naszym O(N)
n = 120
times = []

for i in range(5,n+1):

    times.append(sherman(i))



plt.figure(figsize=(12, 6))

plt.plot(range(5,n+1), times,
         marker='o',
         linestyle='-',
          color="b")

plt.xlabel('Rozmiar danych')
plt.ylabel('Czas wykonania (sekundy)')
plt.grid(True)
plt.show()


