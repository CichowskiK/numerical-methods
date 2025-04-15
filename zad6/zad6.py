import numpy as np
import matplotlib.pyplot as plt

M = np.array([
    [9, 2, 0, 0],
    [2, 4, 1, 0],
    [0, 1, 3, 1],
    [0, 0, 1, 2]
])

epsilon = 1e-12

y = [0.25] * 4

####################################################################################
#___________________________________PODPUNKT A______________________________________

def gen_Pot(y, A):
    back_y = np.zeros_like(y)
    while np.linalg.norm(y - back_y, 1) > epsilon:
        back_y = y.copy()
        z= np.dot(A, y)
        y = z / np.linalg.norm(z, 1)
        yield np.linalg.norm(z, 1)
    print("wektor własny do największej wartości własnej to:", y / np.linalg.norm(y))

wyniki_Pot= list(gen_Pot(y, M))

print("największa wartość własna to:", wyniki_Pot[-1])

for i in range(len(wyniki_Pot)):
    wyniki_Pot[i] = abs(wyniki_Pot[-1] - wyniki_Pot[i])

####################################################################################
#___________________________________PODPUNKT B______________________________________
'''  ALGORYTM QR PRZEZ OBROTY GIVENSA- ŚREDNIO DZIAŁA
def givens_rotation(a, b):

    if b == 0:
        c, s = 1, 0
    else:
        r = np.hypot(a, b)
        c = a / r
        s = -b / r
    return c, s

def qr_tridiagonal_givens(A):

    n = A.shape[0]
    Q = np.eye(n)  
    R = A.copy()

    for i in range(n - 1):
        c, s = givens_rotation(R[i, i], R[i + 1, i])

        G = np.eye(n)
        G[i, i], G[i, i + 1] = c, s
        G[i + 1, i], G[i + 1, i + 1] = -s, c

        R = G @ R  
        Q = Q @ G.T  

    return Q, R

def gen_algorytm_QR(A):
    i=0
    while not is_upper_triangular(A):
        Q, R = qr_tridiagonal_givens(A)
        A = R @ Q
        print(A)
        yield A
        i = i +1
        if i >100:
            break
'''

def is_upper_triangular(matrix):

    rows, cols = matrix.shape
    if rows != cols:
        return False 
    
    for i in range(1, rows):
        for j in range(i):
            if abs(matrix[i, j]) >= 1e-8:
                return False  
    return True

def gen_QR(A):
    while not is_upper_triangular(A):
        Q, R= np.linalg.qr(A)
        A = R @ Q
        yield A

wyniki_qr = list(gen_QR(M))

print(wyniki_qr[-1])

print("wszystkie wartości własne:", wyniki_qr[-1][0][0], wyniki_qr[-1][1][1], wyniki_qr[-1][2][2], wyniki_qr[-1][3][3])

diag_1 = []
diag_2 = []
diag_3 = []
diag_4 = []

wartosci, wektory = np.linalg.eig(M)

for i in range(len(wyniki_qr)):
    diag_1.append(abs(wyniki_qr[i][0][0] - wartosci[0]))
    diag_2.append(abs(wyniki_qr[i][1][1] - wartosci[1]))
    diag_3.append(abs(wyniki_qr[i][2][2] - wartosci[2]))
    diag_4.append(abs(wyniki_qr[i][3][3] - wartosci[3]))

####################################################################################
#__________________________SPRAWDZENIE Z BIBLLIOTEKĄ NUMPY__________________________

wartosci, wektory = np.linalg.eig(M)

print("Wartości własne obliczone za pomocą funkcji bibliotecznych wynosi: ", wartosci)
print("odpowiadające im wektory własne to: \n", wektory.T)

####################################################################################
#_____________________________________WYKRESY_______________________________________

plt.figure(figsize=(12, 6))
plt.title("Metoda Potęgowa")
plt.plot(range(len(wyniki_Pot)), wyniki_Pot,
         marker='o',
         linestyle='-',
          color="b")


plt.yscale('log')
plt.xlabel('Numer iteracji')
plt.ylabel('Różnica między przybliżeniem w danej iteracji, a wynikiem dokładnym')
plt.grid(True)
plt.show()

x = range(len(diag_1))  
values = [diag_1, diag_2, diag_3, diag_4]
labels = ["Diag 1", "Diag 2", "Diag 3", "Diag 4"]


plt.figure(figsize=(12, 6))
for data, label in zip(values, labels):
    plt.plot(x, data, marker='o', label=label)

plt.yscale('log')
plt.title("Różnice między przybliżonymi wartościami własnymi a wartościami dokładnymi")
plt.xlabel("Iteracja")
plt.ylabel("Różnica")
plt.legend()
plt.grid(True)
plt.show()



