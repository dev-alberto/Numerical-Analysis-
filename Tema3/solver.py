from parser import Parser
from Sparse import Sparse

parser = Parser("sisteme/m_rar_2017_1.txt")
sistem = Sparse(parser.parse_matrix())
print(sistem)
