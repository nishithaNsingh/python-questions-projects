def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_primes(numbers):
    return filter(is_prime, numbers)

if __name__ == "__main__":
    num = input("Enter a list of numbers separated by spaces: ")
    numbers = list(map(int, num.split()))

    prime_numbers = list(filter_primes(numbers))

    print("Input Numbers:", numbers)
    print("Prime Numbers:", prime_numbers)
