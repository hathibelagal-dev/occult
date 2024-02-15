import sys

def _dfs(item, depth = 0):
    print(" " * depth * 2, end = "")
    print(item[0])
    for i in range(1, len(item)):
        if type(item[i]) is tuple:
            _dfs(item[i], depth + 1)

def items(ast):
    if ast[0] != "PROGRAM":
        print("Programma invalidum ☠️ ")
        sys.exit(1)
    for item in ast[1]:
        _dfs(item, 0)
