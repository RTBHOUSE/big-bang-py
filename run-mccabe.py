"""
Check recursively McCabe complexity of Python files.

Usage:
> python run-mccabe.py **max_complexity**

This script is slightly changed version of @dmerejkowsky gist:
https://gist.github.com/dmerejkowsky/8aa70f5f6b7f04165f8e041ee9e3b177
"""

import ast
import re
import sys
import textwrap
from pathlib import Path

import mccabe

LINESEPS = ['\r\n', '\r', '\n']
U_LINESEPS = LINESEPS + ['\u0085', '\u2028', '\u2029']
U_NEWLINE = re.compile('|'.join(U_LINESEPS))


def main():
    max_complexity = int(sys.argv[1])
    print("Looking for code with complexity above", max_complexity)
    for py_file in yield_py_files():
        process(py_file, max_complexity)


def yield_py_files():
    py_files = Path(".").glob('**/*.py')
    for py_file in py_files:
        if not is_hidden_file(py_file):
            yield py_file


def is_hidden_file(file_path):
    return any(x.startswith(".") for x in file_path.parts)


def process(py_file, max_complexity):
    with open(py_file) as file:
        code = U_NEWLINE.sub(repl='\n', string=file.read())
    tree = compile(code, py_file, "exec", ast.PyCF_ONLY_AST)
    visitor = mccabe.PathGraphingAstVisitor()
    visitor.preorder(tree, visitor)
    for graph in visitor.graphs.values():
        if graph.complexity() > max_complexity:
            text = textwrap.dedent('{}:{}:{} {} {}')
            text = text.format(
                py_file, graph.lineno, graph.column, graph.entity, graph.complexity()
            )
            print(text)


if __name__ == "__main__":
    main()
