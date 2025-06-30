import sys


def hanoi(n, source='A', target='C', auxiliary='B', moves=None):
    """Return a list of moves to solve the Tower of Hanoi puzzle."""
    if n <= 0:
        raise ValueError("n must be greater than 0")
    if moves is None:
        moves = []
    if n == 1:
        moves.append((source, target))
    else:
        hanoi(n - 1, source, auxiliary, target, moves)
        moves.append((source, target))
        hanoi(n - 1, auxiliary, target, source, moves)
    return moves


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    if not argv:
        print("Usage: python hanoi.py <n>")
        return 1
    try:
        n = int(argv[0])
        moves = hanoi(n)
        for i, move in enumerate(moves, 1):
            print(f"Move {i}: {move[0]} -> {move[1]}")
    except ValueError as e:
        print(f"Error: {e}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
