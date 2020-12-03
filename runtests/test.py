import yaml
import io
from gkdtikz.tree import root, GkdInterface

n = yaml.load("""
a:
- a
- b
""", Loader=yaml.SafeLoader)
root(lambda x: print(x, end=''), n)

class S:
    globals = {}
GkdInterface.load(S, lambda x: print(x, end=''))