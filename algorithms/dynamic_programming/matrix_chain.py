from rich import print as rprint
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)


def matrix_chain(d):
    """d is a list of n + 1 numbers such that the size of kth matrix is d[k]-by-d[k+1]
    return an n-by-n table such that N[i][j] represents the minimum number of multiplcations
    needed to compute the product of Ai through Aj, inclusive
    """
    n = len(d) - 1
    N = [[0] * n for i in range(n)]
    for b in range(1, n):  # number of products in subchain
        for i in range(n - b):  # start of subchain
            j = i + b  # end of subchain
            N[i][j] = min(
                N[i][k] + N[k + 1][j] + d[i] * d[k + 1] * d[j + 1] for k in range(i, j)
            )
    pp.pprint(N)


matrix_chain([1, 2, 3, 4, 5])
