def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def primes_up_to(n):
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def optimal_moves(n):
        primes = primes_up_to(n)
        moves = 0
        visited = [False] * (n + 1)

        for prime in primes:
            if not visited[prime]:
                moves += 1
                for multiple in range(prime, n + 1, prime):
                    visited[multiple] = True

        return moves

    if not nums or x < 1:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n < 1:
            ben_wins += 1
            continue

        total_moves = optimal_moves(n)

        # Maria starts the game, so if the number of moves is odd, Maria wins.
        if total_moves % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

