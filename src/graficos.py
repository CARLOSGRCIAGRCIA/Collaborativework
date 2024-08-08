import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def graficar_vector(vector):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.quiver(0, 0, 0, vector[0], vector[1], vector[2], color='b')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Gráfico del vector')
    plt.show()

def graficar_matriz(matriz):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(matriz[:, 0], matriz[:, 1], matriz[:, 2], c='r', marker='o')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Gráfico de la matriz')
    plt.show()
