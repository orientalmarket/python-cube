import numpy as np
import logging
import sys

logging.basicConfig(
    filename="log.txt",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logging.debug("DEBUGGING")


def main():
    cube_width = 10.0
    width = 160
    height = 44
    horizontal_offset = 1 * cube_width
    distance_from_cam = 100
    K1 = 40
    increment_speed = 0.5
    global x
    global y
    global z
    angle_x = angle_y = angle_z = 0

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
            else:
                sys.stdout.write("\n")

        attributes = vars()
        for var in attributes:
            logging.info(f"{var}: {attributes[var]}")

        angle_x += 0.05
        angle_y += 0.05
        angle_z += 0.01


if __name__ == "__main__":
    main()
