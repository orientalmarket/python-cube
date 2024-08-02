import numpy as np
import sys

cube_width = 20.0
width = 160
height = 44
horizontal_offset = 1 * cube_width
distance_from_cam = 100
K1 = 40
increment_speed = 0.6
angle_x = angle_y = angle_z = 0


def calculate_x(i, j, k):
    return (
        j * np.sin(angle_x) * np.sin(angle_y) * np.cos(angle_z)
        - k * np.cos(angle_x) * np.sin(angle_y) * np.cos(angle_z)
        + j * np.cos(angle_x) * np.sin(angle_z)
        + k * np.sin(angle_x) * np.sin(angle_z)
        + i * np.cos(angle_y) * np.cos(angle_z)
    )


def calculate_y(i, j, k):
    return (
        j * np.cos(angle_x) * np.cos(angle_z)
        + k * np.sin(angle_x) * np.cos(angle_z)
        - j * np.sin(angle_x) * np.sin(angle_y) * np.sin(angle_z)
        + k * np.cos(angle_x) * np.sin(angle_y) * np.sin(angle_z)
        - i * np.cos(angle_y) * np.sin(angle_z)
    )


def calculate_z(i, j, k):
    return (
        k * np.cos(angle_x) * np.cos(angle_y)
        - j * np.sin(angle_x) * np.cos(angle_y)
        + i * np.sin(angle_y)
    )


def calculate_surface(cube_x, cube_y, cube_z, char):
    x = calculate_x(cube_x, cube_y, cube_z)
    y = calculate_y(cube_x, cube_y, cube_z)
    z = calculate_z(cube_x, cube_y, cube_z) + distance_from_cam
    ooz = 1 / z
    x_prime = int(width / 2 + horizontal_offset + K1 * ooz * x * 2)
    y_prime = int(height / 2 + K1 * ooz * y)
    index = x_prime + y_prime * width
    if index >= 0 and index < width * height:
        if ooz > z_buffer[index]:
            z_buffer[index] = ooz
            char_buffer[index] = char


print(f"\x1b[2J")
while True:
    char_buffer = np.full(width * height, ".")
    z_buffer = np.zeros(width * height * 4)
    cube_x = -cube_width
    while cube_x < cube_width:
        cube_y = -cube_width
        while cube_y < cube_width:
            calculate_surface(cube_x, cube_y, -cube_width, "@")
            calculate_surface(cube_width, cube_y, cube_x, "$")
            calculate_surface(-cube_width, cube_y, -cube_x, "~")
            calculate_surface(-cube_x, cube_y, cube_width, "#")
            calculate_surface(cube_x, -cube_width, -cube_y, ";")
            calculate_surface(cube_x, cube_width, cube_y, "+")
            cube_y += increment_speed
        cube_x += increment_speed
    print(f"\x1b[H")
    for k in range(width * height):
        if k % width:
            sys.stdout.write(char_buffer[k])
            sys.stdout.flush()
        else:
            sys.stdout.write("\n")
            sys.stdout.flush()

    angle_x += 0.05
    angle_y += 0.05
    angle_z += 0.01
