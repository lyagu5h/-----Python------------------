from threading import Thread;

def calculate_squares():
    for i in range(1, 11):
        print(f"{i}^2 = {i ** 2}")

def calculate_cubes():
    for i in range(1, 11):
        print(f"{i}^3 = {i ** 3}")

if __name__ == '__main__':
    square_thread = Thread(target=calculate_squares)
    cube_thread = Thread(target=calculate_cubes)

    square_thread.start()
    cube_thread.start()

    square_thread.join()
    cube_thread.join()