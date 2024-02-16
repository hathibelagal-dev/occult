import sys

stack = []

output_format = None

def _dfs(item, depth = 0):
    stack.append(item[0])
    if output_format == "ast":
        print(" " * depth * 2, end = "")
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

def items(ast, translate_to):
    global stack
    global output_format
    output_format = translate_to
    if ast[0] != "OCCULT_PROGRAM":
        print("Programma invalidum ☠️ ")
        sys.exit(1)
    for item in ast[1]:
        _dfs(item, 0)
        _process()
        stack = []
