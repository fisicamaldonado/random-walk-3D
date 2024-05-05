import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def random_walk_3D(steps):
    x, y, z = 0, 0, 0
    positions = [(x, y, z)]

    for _ in range(steps):
        direction = random.randint(1, 6)  # Simulamos el lanzamiento de un dado de 6 caras
        if direction == 1:
            x += 1  # Movimiento hacia la derecha
        elif direction == 2:
            x -= 1  # Movimiento hacia la izquierda
        elif direction == 3:
            y += 1  # Movimiento hacia arriba
        elif direction == 4:
            y -= 1  # Movimiento hacia abajo
        elif direction == 5:
            z += 1  # Movimiento hacia arriba en el eje z
        else:
            z -= 1  # Movimiento hacia abajo en el eje z
        positions.append((x, y, z))
    
    return positions

def plot_random_walk_3D(positions, steps):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x_values = [pos[0] for pos in positions]
    y_values = [pos[1] for pos in positions]
    z_values = [pos[2] for pos in positions]

    ax.plot(x_values, y_values, z_values, marker='o', color='b')  # Todos los puntos menos el primero son azules
    ax.scatter(*positions[0], color='r', marker='o', s=100)  # El primer punto es rojo y más grande
    ax.scatter(*positions[-1], color='g', marker='o', s=100)  # El último punto es verde y más grande

    # Vector de desplazamiento desde el origen hasta el punto final
    displacement = np.array(positions[-1]) - np.array(positions[0])
    ax.quiver(*positions[0], *displacement, color='k')

    ax.set_title(f'Random Walk Simulation 3D ({steps} steps)')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

# Definimos la cantidad de pasos en el "random walk" 3D
num_steps = 1000

# Simulamos el "random walk" 3D
walk_positions_3D = random_walk_3D(num_steps)

# Graficamos el resultado
plot_random_walk_3D(walk_positions_3D, num_steps)
