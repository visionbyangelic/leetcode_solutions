class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: list[int], vFences: list[int]) -> int:
        MOD = 1000000007

        # If grid is already a square, biggest square uses full side
        if m == n:
            return ((n - 1) ** 2) % MOD

        # Store all possible vertical distances between horizontal fences
        hDiff = set()

        # Add boundary fences at position 1
        hFences.append(1)
        vFences.append(1)

        # Sort fence positions
        hFences.sort()
        vFences.sort()

        # Add boundary fences at the end of grid
        hFences.append(m)
        vFences.append(n)

        # Compute all possible heights between horizontal fences
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                hDiff.add(hFences[j] - hFences[i])

        maxSide = -1

        # Check which vertical distances also exist in horizontal distances
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                val = vFences[j] - vFences[i]
                if val in hDiff:
                    maxSide = max(maxSide, val)

        # No possible square
        if maxSide == -1:
            return -1

        # Return max square area with modulo
        return (maxSide * maxSide) % MOD