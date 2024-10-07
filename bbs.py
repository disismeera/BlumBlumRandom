import random
from math import gcd

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generate a prime number such that p ≡ 3 (mod 4)
def generate_prime(bit_length):
    while True:
        p = random.getrandbits(bit_length)
        if is_prime(p) and p % 4 == 3:
            return p

# Blum Blum Shub random number generator
def blum_blum_shub(seed, p, q, length):
    n = p * q
    x = (seed**2) % n
    bits = []
    for _ in range(length):
        x = (x**2) % n
        bits.append(x % 2)  # extract least significant bit
    return bits

def main():
    bit_length = int(input("Enter bit length for prime numbers (e.g., 16, 32): "))
    p = generate_prime(bit_length)
    q = generate_prime(bit_length)
    
    print(f"Generated primes p: {p}, q: {q}")
    
    n = p * q
    print(f"n = p * q = {n}")
    
    seed = int(input(f"Enter a seed value (must be less than n and relatively prime to {n}): "))
    
    while gcd(seed, n) != 1:
        print("Seed is not relatively prime to n. Please enter a different seed.")
        seed = int(input(f"Enter a seed value (must be less than n and relatively prime to {n}): "))
    
    length = int(input("Enter the number of random bits to generate: "))
    
    random_bits = blum_blum_shub(seed, p, q, length)
    random_number = int(''.join(map(str, random_bits)), 2)
    
    print(f"Generated random bits: {random_bits}")
    print(f"Random number: {random_number}")

if __name__ == "__main__":
    main()
