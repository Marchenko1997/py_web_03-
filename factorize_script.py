import time
from multiprocessing import Pool, cpu_count

def factorize_sync(*numbers):
    result = []
    for number in numbers:
        divisors = []
        for i in range(1, number + 1):
            if number % i == 0:
                divisors.append(i)
        result.append(divisors)
    return result

def factorize_number(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

def factorize_parallel(*numbers):
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(factorize_number, numbers)
    return results

if __name__ == '__main__':
    numbers = (128, 255, 99999, 10651060)

    start_time = time.time()
    a, b, c, d = factorize_sync(*numbers)
    end_time = time.time()
    print("Sync version time:", end_time - start_time)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    print("Sync version test passed!")

    start_time = time.time()
    a, b, c, d = factorize_parallel(*numbers)
    end_time = time.time()
    print("Parallel version time:", end_time - start_time)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    print("Parallel version test passed!")