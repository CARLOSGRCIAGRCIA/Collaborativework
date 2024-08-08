import numpy as np

def leer_vector(x, y, z):
    return np.array([float(x), float(y), float(z)])

def leer_matriz(a11, a12, a13, a21, a22, a23, a31, a32, a33):
    return np.array([[float(a11), float(a12), float(a13)], 
                     [float(a21), float(a22), float(a23)], 
                     [float(a31), float(a32), float(a33)]])

def sumar_vectores(vector1, vector2):
    return vector1 + vector2

def restar_vectores(vector1, vector2):
    return vector1 - vector2

def producto_punto(vector1, vector2):
    return np.dot(vector1, vector2)

def magnitud(vector):
    return np.linalg.norm(vector)

def proyeccion(vector1, vector2):
    return np.dot(vector1, vector2) / np.linalg.norm(vector2) ** 2 * vector2

def producto_matriz_vector(matriz, vector):
    return np.dot(matriz, vector)

def producto_matrices(matriz1, matriz2):
    return np.dot(matriz1, matriz2)
