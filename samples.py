"""Module contains two bespoke methods showcasing some simple functionality."""
from functools import reduce


def sum_primes(number):
    """Sum all the prime numbers up to and including the provided number.
    A prime number is defined as a number greater than one and having only two divisors, one and itself.
    For example, 2 is a prime number because it's only divisible by one and two.
    The provided number may not be a prime."""
    def is_prime(num):
        """checks is the provided input number is prime or otherwise"""
        for index in range(2, num):
            if num % index == 0:
                return False
        return True

    prime_list = []
    for index in range(2, number+1):  # Throws Exception if number is not integer
        if is_prime(index):
            prime_list.append(index)

    sum_of_primes = reduce(lambda x, y: x+y, prime_list)
    return sum_of_primes


def is_triangle(side_a, side_b, side_c):
    """Return a true or false for wether a triangle can be formed using the three lines.
    Whatever unit you take, the unit will be consistent for all the parameters."""
    if(side_a >= side_b) and (side_a >= side_c):
        return side_b + side_c > side_a
    elif (side_b >= side_c) and (side_b >= side_a):
        return side_a + side_c > side_b
    elif (side_c >= side_a) and (side_c >= side_b):
        return side_a + side_b > side_c
