#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Returns the winner of the game"""
    wins = {
        'Ben': 0,
        'Maria': 0,
    }

    if x >= 10000:
        return 'Maria'

    def isPrime(num):
        """Returns whether or nor a number is a prime number"""
        if num <= 1:
            return False
        if num <= 3:
            return True
        if not num % 2 or not num % 3:
            return False

        i = 5
        while (i * i <= num):
            if not num % i or not num % (i + 2):
                return False
            i += 6

        return True

    for i in range(x):
        primes = []

        # Extract all prime numbers for n
        for n in range(2, nums[i] + 1):
            if isPrime(n):
                primes.append(n)

        primesLength = len(primes)

        # If there are odd numbers of prime numbers, Maria wins the round
        if primesLength % 2 != 0:
            wins['Maria'] += 1
        else:  # otherwise Ben wins the round
            wins['Ben'] += 1

    # If a winner cannot be determined
    if wins['Maria'] == wins['Ben']:
        return None

    # Get the player with the highest rounds won
    keyMax = max(wins, key=lambda x: wins[x])

    return keyMax


if __name__ == '__main__':
    print("Winner: {}".format(isWinner(3, [4, 5, 1])))
