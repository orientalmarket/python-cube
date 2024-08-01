import pygame
import numpy as np
import logging

logging.basicConfig(
    filename="log.txt",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logging.debug("DEBUGGING")


angle_x = angle_y = angle_z = 0
angle_x = 0.05
angle_y = 0.05
angle_z = 0.01

rotation_x = np.array(
    [
        [1, 0, 0],
        [0, np.cos(angle_x), -np.sin(angle_x)],
        [0, np.sin(angle_x), np.cos(angle_x)],
    ]
)

rotation_y = np.array(
    [
        [np.cos(angle_y), 0, np.sin(angle_y)],
        [0, 1, 0],
        [-np.sin(angle_y), 0, np.cos(angle_y)],
    ]
)

rotation_z = np.array(
    [
        [np.cos(angle_z), -np.sin(angle_z), 0],
        [np.sin(angle_z), np.cos(angle_z), 0],
        [0, 0, 1],
    ]
)


def calculate_x(i, j, k):
    vector = np.array([i, j, k])
    vector_rot_x = np.matmul(vector, rotation_x)
    vector_rot_y = np.matmul(vector_rot_x, rotation_y)
    vector_rot_z = np.matmul(vector_rot_y, rotation_z)
    logging.info(vector_rot_z[2])
    return vector_rot_z[0]


def calculate_y(i, j, k):
    vector = np.array([i, j, k])
    vector_rot_x = np.matmul(vector, rotation_x)
    vector_rot_y = np.matmul(vector_rot_x, rotation_y)
    vector_rot_z = np.matmul(vector_rot_y, rotation_z)
    return vector_rot_z[1]


def calculate_z(i, j, k):
    vector = np.array([i, j, k])
    vector_rot_x = np.matmul(vector, rotation_x)
    vector_rot_y = np.matmul(vector_rot_x, rotation_y)
    vector_rot_z = np.matmul(vector_rot_y, rotation_z)
    return vector_rot_z[2]


def main():
    calculate_x(-1, -1, 1)


if __name__ == "__main__":
    main()
