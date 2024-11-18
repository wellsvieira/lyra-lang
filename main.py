import sys
from GT import *

if len(sys.argv) > 1:
  with open(sys.argv[1],'r') as file:
    inp = file.read()
    parser.parse(inp)
else:
  for line in sys.stdin:
    parser.success = True
    parser.labels = 0
    parser.address = 0
    stack = Stack()
    parser.parse(line)