import numpy as np

A1 = np.array([
    [5.8267103432, 1.0419816676, 0.4517861296, -0.2246976350, 0.7150286064],
    [1.0419816676, 5.8150823499, -0.8642832971, 0.6610711416, -0.3874139415],
    [0.4517861296, -0.8642832971, 1.5136472691, -0.8512078774, 0.6771688230],
    [-0.2246976350, 0.6610711416, -0.8512078774, 5.3014166511, 0.5228116055],
    [0.7150286064, -0.3874139415, 0.6771688230, 0.5228116055, 3.5431433879]])

A2 = np.array([
    [5.4763986379, 1.6846933459, 0.3136661779, -1.0597154562, 0.0083249547],
    [1.6846933459, 4.6359087874, -0.6108766748, 2.1930659258, 0.9091647433],
    [0.3136661779, -0.6108766748, 1.4591897081, -1.1804364456, 0.3985316185],
    [-1.0597154562, 2.1930659258, -1.1804364456, 3.3110327980, -1.1617171573],
    [0.0083249547, 0.9091647433, 0.3985316185, -1.1617171573, 2.1174700695]])

b = np.array([-2.8634904630, -4.8216733374, -4.2958468309, -0.0877703331, -2.0223464006]).reshape(-1, 1)

y1 = np.linalg.solve(A1, b)
y2 = np.linalg.solve(A2, b)


delta_b = np.random.randn(5)                 #genereujemy wektor
delta_b = delta_b / np.linalg.norm(delta_b) * 1e-6   #sprowadzamy go do odpowiedniej normy
delta_b = delta_b.reshape(-1,1)              #odwracamy go 

y1Zaburzone = np.linalg.solve(A1, b+delta_b)
y2Zaburzone = np.linalg.solve(A2, b+delta_b)

uwarunkowanieA1 = np.linalg.cond(A1)
uwarunkowanieA2 = np.linalg.cond(A2)

print("Macierz A1:\n", A1, "\nMacierz A2:\n", A2, "\nWektor b:\n", b, "\nWektor delta_b\n", delta_b)

print("\n______________________________________________________________\n")

print("Wyniki:\nDla A1:\n",y1, "\nDla A2:\n", y2)

print("\n______________________________________________________________\n")

print("Wyniki dla zaburzonego wektora wyrazów wolnych:\nDla A1:\n",y1Zaburzone, "\nDla A2:\n", y2Zaburzone)

print("\n______________________________________________________________\n")

print("Uwarunkowanie A1:",uwarunkowanieA1, "\nUwarunkowanie A2:",uwarunkowanieA2)