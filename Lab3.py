import time
from collections import deque

# Стек на основе массива
class StackArray:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

# Стек на основе связанного списка
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        item = self.top.value
        self.top = self.top.next
        return item

    def is_empty(self):
        return self.top is None

# Стек на основе дека
class StackDeque:
    def __init__(self):
        self.stack = deque()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

# Алгоритм поиска пути
def search(n, m, matrix, route, direction, stack):
    row, col = route[-1]
    drow, dcol = direction
    new_pos = (row + drow, col + dcol)

    if (0 <= new_pos[0] < n) and (0 <= new_pos[1] < m) and matrix[new_pos[0]][new_pos[1]] == 0:
        route.append(new_pos)
        matrix[new_pos[0]][new_pos[1]] = 1
        if new_pos[0] == n - 1:
            return True
        priority_dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for d in priority_dirs:
            if search(n, m, matrix, route, d, stack):
                return True
        matrix[new_pos[0]][new_pos[1]] = 0
        route.pop()
    return False

def find_route(n, m, matrix, start, stack_type):
    if stack_type == 'array':
        stack = StackArray()
    elif stack_type == 'linked_list':
        stack = StackLinkedList()
    elif stack_type == 'deque':
        stack = StackDeque()

    route = [(0, start)]
    stack.push((0, start))
    if not search(n, m, matrix, route, (1, 0), stack):
        return None
    return route


def solve_maze(matrix, stack_type):
    n, m = len(matrix), len(matrix[0])

    # Проверка на полностью нулевой лабиринт
    if all(cell == 0 for row in matrix for cell in row):
        return "YES", matrix

    possible = True
    original_matrix = [row[:] for row in matrix]  # Создание копии матрицы для восстановления
    for col in range(m):
        if matrix[0][col] == 0:
            if not find_route(n, m, matrix, col, stack_type):
                possible = False
                break
    return "YES" if possible else "NO", matrix

# Функция для измерения времени выполнения
def measure_time(func, *args):
    start_time = time.perf_counter()
    result, matrix = func(*args)
    end_time = time.perf_counter()
    return end_time - start_time, result, matrix

# Функция для вывода матрицы
def print_matrix(matrix):
    for row in matrix:
        print(' '.join(str(cell) for cell in row))
    print()

# Пример использования
matrix_example = [
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
]

# Замер времени для стека на массиве
time_array, result_array, matrix_result_array = measure_time(solve_maze, matrix_example, 'array')
print(f"Array Stack: {time_array:.10f} seconds, Result: {result_array}")
print("Resulting Matrix:")
print_matrix(matrix_result_array)

matrix_example = [
    [0, 0, 0, 0, 0],
]

# Замер времени для стека на связанном списке
time_linked_list, result_linked_list, matrix_result_linked_list = measure_time(solve_maze, matrix_example, 'linked_list')
print(f"Linked List Stack: {time_linked_list:.10f} seconds, Result: {result_linked_list}")
print("Resulting Matrix:")
print_matrix(matrix_result_linked_list)

# Восстановление исходной матрицы для следующих тестов
matrix_example = [
    [1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 1]
]

# Замер времени для стека на деке
time_deque, result_deque, matrix_result_deque = measure_time(solve_maze, matrix_example, 'deque')
print(f"Deque Stack: {time_deque:.10f} seconds, Result: {result_deque}")
print("Resulting Matrix:")
print_matrix(matrix_result_deque)