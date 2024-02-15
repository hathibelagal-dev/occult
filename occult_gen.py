import sys

stack = []

def _dfs(item, depth = 0):
    print(" " * depth * 2, end = "")
    stack.append(item[0])
    print(item[0])
    for i in range(1, len(item)):
        if type(item[i]) is tuple:
            _dfs(item[i], depth + 1)
        else:
            stack.append(item[i])

def _process():
    if not stack:
        return
    while stack:
        item = stack.pop()        

def items(ast):
    global stack
    if ast[0] != "OCCULT_PROGRAM":
        print("Programma invalidum ☠️ ")
        sys.exit(1)
    for item in ast[1]:
        _dfs(item, 0)
        _process()
        stack = []
