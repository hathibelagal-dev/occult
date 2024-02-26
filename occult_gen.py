import sys
import json

stack = []

_output_format = None
_output_file = None

_of = None

def _gen_json(tup):
    if isinstance(tup, tuple):
        if len(tup) == 2 and isinstance(tup[0], str):
            return {tup[0]: _gen_json(tup[1])}
        else:
            return [_gen_json(item) for item in tup]
    else:
        return tup

def _dfs(item, depth = 0):
    stack.append(item[0])
    _of.write(" " * depth * 2)
    _of.write(item[0])
    _of.write("\n")
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

def items(ast, translate_to, output_file):
    global stack
    global _output_format
    global _output_file
    global _of
    _output_file = output_file
    _of = open(_output_file, 'w')
    _output_format = translate_to
    if ast[0] != "OCCULT_PROGRAM":
        print("Programma invalidum ☠️ ")
        sys.exit(1)
    if _output_format == 'ast':
        for item in ast[1]:
            _dfs(item, 0)
            _process()
            stack = []
    elif _output_format == 'json':
        json_data = _gen_json(ast)
        _of.write(json.dumps(json_data, indent = 2))
    _of.close()
