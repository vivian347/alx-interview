#!/usr/bin/python3
"""prime_game"""


def isWinner(x, nums):
    """Checks for winner"""
    def is_prime(num):
        """ Function to check if a number is prime """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes(n):
        """ Function to get a list of prime numbers up to n """
        primes = []
        for num in range(2, n + 1):
            if is_prime(num):
                primes.append(num)
        return primes

    def can_win(num):
        """Function to determine if a player can win the game for a given number"""
        primes = get_primes(num)
        # If the number of primes is even, the second player wins. Otherwise, the first player wins.
        return len(primes) % 2 == 0

    maria_wins = 0
    ben_wins = 0

    for num in nums:
        if can_win(num):
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
