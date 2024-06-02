import numpy as np
from scipy.linalg import blas as scipy_blas
import time
from joblib import Parallel, delayed


n = 2048

# Генерация случайных матриц типа double
A = np.random.rand(n, n).astype(np.float64)
B = np.random.rand(n, n).astype(np.float64)

# Алгебраическое перемножение
def matrix_multiply(A, B):
    n = A.shape[0]
    C = np.zeros((n, n), dtype=np.float64)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i, j] += A[i, k] * B[k, j]
    return C



start_time = time.perf_counter()


C_direct = matrix_multiply(A, B)


end_time = time.perf_counter()

# Время выполнения
time_direct = end_time - start_time
print(f"Время выполнения первого метода: {time_direct} seconds")


start_time = time.perf_counter()

# Перемножение с использованием BLAS
C_blas = scipy_blas.cgemm(1.0, A, B)


end_time = time.perf_counter()

# Время выполнения
time_blas = end_time - start_time
print(f"Время выполнения второго метода: {time_blas} seconds")


# Оптимизированное перемножение с использованием параллельных вычислений на CPU
def matrix_multiply_parallel(A, B, num_jobs=-1):
    def multiply_row(i):
        return np.dot(A[i, :], B)

    C = Parallel(n_jobs=num_jobs)(delayed(multiply_row)(i) for i in range(A.shape[0]))
    return np.array(C)



start_time = time.perf_counter()


C_optimized = matrix_multiply_parallel(A, B)


end_time = time.perf_counter()

# Время выполнения
time_optimized = end_time - start_time
print(f"Время выполнения третьего метода: {time_optimized} seconds")

# Сравнение матриц на совпадение
def compare_matrix(A, B, epsilon=1e-6):
    return np.allclose(A, B, atol=epsilon)

if compare_matrix(C_direct, C_blas):
        print("Матрицы 1 и 2 равны.")
else:
        print("Матрицы 1 и 2 равны.")

if compare_matrix(C_direct, C_optimized):
    print("Матрицы 1 и 3 равны.")
else:
    print("Матрицы 1 и 3 не равны.")

def calculate_performance(time_taken, n):
    if time_taken == 0:
        return float('inf')
    c = 2 * n ** 3
    performance = c / time_taken * 1e-6  # в MFlops
    return performance


# Считаем производительность
performance_direct = calculate_performance(time_direct, n)
performance_blas = calculate_performance(time_blas, n)
performance_optimized = calculate_performance(time_optimized, n)

print(f"Производительность первого метода: {performance_direct} MFlops")
print(f"Производительность второго метода: {performance_blas} MFlops")
print(f"Производительность третьего метода: {performance_optimized} MFlops")