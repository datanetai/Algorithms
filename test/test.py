import math

def main():
    print("Hello, world!")
    n = 0
    while n < 100:
        if is_prime(n):
            print(n)
        n += 1

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    main()
