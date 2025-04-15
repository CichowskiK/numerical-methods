import numpy as np

def generate_tridiagonal_matrix(n, d, sub_diag1=0.5, sub_diag2=0.1):
    main_diag = np.full(n, d) 
    sub_diag1_vals = np.full(n - 1, sub_diag1)  
    sub_diag2_vals = np.full(n - 2, sub_diag2)  
    matrix = np.diag(main_diag) + \
             np.diag(sub_diag1_vals, k=1) + np.diag(sub_diag1_vals, k=-1) + \
             np.diag(sub_diag2_vals, k=2) + np.diag(sub_diag2_vals, k=-2)
    return matrix


def is_positive_definite(matrix):
    eigenvalues = np.linalg.eigvalsh(matrix) 
    return np.all(eigenvalues > 0), np.min(eigenvalues)


n = 200  
d_values = np.linspace(0.5, 1.0, 100) 

results = []
for d in d_values:
    matrix = generate_tridiagonal_matrix(n, d)
    is_pd, min_eigenvalue = is_positive_definite(matrix)
    results.append((d, is_pd, min_eigenvalue))

min_positive_d = next((d for d, is_pd, _ in results if is_pd), None)
results, min_positive_d

print(min_positive_d)
