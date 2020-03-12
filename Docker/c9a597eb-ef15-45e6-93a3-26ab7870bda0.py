import sys
from unittest.mock import MagicMock

lst = sys.argv[1:]
input = MagicMock(side_effect=lst)

n1 = int(input())
n2 = int(input())

print(n1 + n2)