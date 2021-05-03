from sys import stdin

a, b, c = [int(x) for x in stdin.readline().rstrip().split()]

print("Takahashi" if a - b - (-1) * c > 0 else "Aoki")
