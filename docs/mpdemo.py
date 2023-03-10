import multiprocessing as mp


def square(i):
    return i * i


l = [1, 3, 2, 5, 4, 3, 2]

if __name__ == '__main__':
    with mp.Pool(4) as pool:
        squares = pool.map(square, l)
    print(squares)