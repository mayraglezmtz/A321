import numpy as np

rows = 36  #(0-35)
cols = 7 # (A-G (Incluyendo el pasillo))

businessClass = 8
economyClass = 28
totalSections = businessClass + economyClass

missingSeats = {
    0: ['B', 'E', 'F', 'G'],
    1: ['B', 'F'],
    2: ['B', 'F'],
    3: ['B', 'F'],
    4: ['B', 'F'],
    5: ['B', 'F'],
    6: ['B', 'F'],
    8: ['G'],
    9: ['A', 'B', 'C', 'E'],
    22: ['A', 'G'],
    23: ['E']
}

def create_availability_matrix(rows, cols):
    # Crear una matriz llena de unos (asientos disponibles)
    matrix = np.ones((rows, cols), dtype=int)
    
    # Marcar los asientos faltantes como 0
    for row, missing_cols in missingSeats.items():
        for col_letter in missing_cols:
            col_index = ord(col_letter) - ord('A')
            if 0 <= row < rows and 0 <= col_index < cols:
                matrix[row][col_index] = 0
    
    return matrix

def create_adjacency_matrix(rows, cols):
    # Calcular el número total de nodos (asientos)
    total_seats = rows * cols
    
    # Crear una matriz de adyacencias vacía
    adj_matrix = np.zeros((total_seats, total_seats), dtype=int)
    
    # Llenar la matriz de adyacencias
    for i in range(total_seats):
        row_i = i // cols
        col_i = i % cols
        
        # Verificar si el asiento actual existe
        if is_valid_seat(row_i, col_i):
            # Revisar los asientos adyacentes (arriba, abajo, izquierda, derecha)
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            
            for d_row, d_col in directions:
                new_row = row_i + d_row
                new_col = col_i + d_col
                
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if is_valid_seat(new_row, new_col):
                        # Calcular los índices en la matriz de adyacencias
                        current_index = i
                        neighbor_index = new_row * cols + new_col
                        
                        # Establecer la conexión en ambas direcciones
                        adj_matrix[current_index][neighbor_index] = 1
                        adj_matrix[neighbor_index][current_index] = 1
    
    return adj_matrix

def is_valid_seat(row, col):
    # Convertir índice de columna a letra
    col_letter = chr(ord('A') + col)
    
    # Verificar si el asiento está en la lista de asientos faltantes
    if row in missingSeats and col_letter in missingSeats[row]:
        return False
    return True

# Crear las matrices
availability_matrix = create_availability_matrix(rows, cols)
adjacency_matrix = create_adjacency_matrix(rows, cols)

print("Matriz de disponibilidad de asientos:")
print(availability_matrix)
print("\nMatriz de adyacencias:")
print(adjacency_matrix)
print("\nDimensiones de la matriz de adyacencias:", adjacency_matrix.shape)



