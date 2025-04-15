import math
import matplotlib.pyplot as plt
import time
import copy

def LU(n, matrix):
    matrix = copy.deepcopy(matrix)
    i =0
    while i < n:
        if i==0:
            matrix[3][i] = matrix

        elif i == n-1: 
            matrix [1][i] = matrix[1][i] - matrix[3][i]*matrix[0][i-1]
            matrix [2][i] = matrix[2][i] - matrix[3][i]*matrix[1][i-1]
            matrix [3][i] = matrix[3][i] / matrix[2][i-1]
        elif i == n-2:
            matrix [2][i] = matrix[2][i] - matrix[3][i]*matrix[1][i-1]
            matrix [3][i] = matrix[3][i] / matrix[2][i-1]
        else :
            matrix [1][i] = matrix[1][i] - matrix[3][i]*matrix[0][i-1]
            matrix [2][i] = matrix[2][i] - matrix[3][i]*matrix[1][i-1]
            matrix [3][i] = matrix[3][i] / matrix[2][i-1]

        i+=1

    determinant = math.prod(matrix[2])

    x=list(range(1,n+1))

    for i in range(1, n):
        x[i] = x[i] - matrix[3][i] * x[i - 1]

    x[n - 1] = x[n - 1] / matrix[2][n - 1]
    x[n - 2] = (x[n - 2] - matrix[1][n - 2] * x[n - 1]) / matrix[2][n - 2]

    for i in range(n - 3, -1, -1):
        x[i] = (x[i] - matrix[0][i] * x[i + 2] - matrix[1][i] * x[i + 1]) / matrix[2][i]
        
    return x, determinant
    

N=300
#konstrujmy jedna duza macierz i bedziemy korzystac tylko z jej wybranych czesci
matrix = []
matrix.append([0.15 / (i * i * i) for i in range(1, N - 1)] + [0] + [0])  #drugi gorny
matrix.append([0.2 / i for i in range(1, N)] + [0])  #pierwszy gorny
matrix.append([1.01] * N) #diagonala
matrix.append([0] + [0.3] * (N - 1))  #dolny

wynik, wyznacznik = LU(N, matrix)

print (wyznacznik)
print (wynik)

times = []

for i in range(5,N+1):

    start_time = time.time()
    LU(i,matrix)
    end_time = time.time()

    final_time = end_time-start_time
    times.append(final_time)


plt.figure(figsize=(12, 6))

plt.plot(range(5,N+1), times,
         marker='o',
         linestyle='-',
          color="b")

plt.xlabel('Rozmiar danych')
plt.ylabel('Czas wykonania (sekundy)')
plt.grid(True)
plt.show()