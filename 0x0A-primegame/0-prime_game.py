#!/usr/bin/python3
"""Prime Game - Maria and Ben's number-based game"""

def isWinner(rounds, numbers):
    """
    Determines the overall winner after a series of rounds.

    Args:
        rounds (int): Number of rounds to be played.
        numbers (list): List of integers representing the upper limit for each round.

    Returns:
        str or None: "Maria" if Maria wins, "Ben" if Ben wins, or None if it's a tie.
    """
    if rounds <= 0 or not numbers:
        return None
    if rounds != len(numbers):
        return None

    ben_score = 0
    maria_score = 0

    max_num = max(numbers)
    sieve = [True] * (max_num + 1)
    sieve[0], sieve[1] = False, False  # 0 and 1 are not prime

    for i in range(2, int(max_num**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = False

    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if sieve[i] else 0)

    for n in numbers:
        if prime_count[n] % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    if maria_score > ben_score:
        return "Maria"
    elif ben_score > maria_score:
        return "Ben"
    else:
        return None

