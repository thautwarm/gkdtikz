import gkdtex.developer_utilities as dev
import yaml

def yaml_to_latex(print, x):
    def print2(x, print=print):
        print('  ')
        print(x)
    if isinstance(x, dict):
        assert len(x) == 1
        [(k, v)] = x.items()
        print(f"node {{{k}}}\n")
        yaml_to_latex(print, v)
    elif isinstance(x, list):
        for each in x:
            print('child{\n')
            yaml_to_latex(print2, each)
            print('}\n')
    else:
        print(f"node {{{x}}}")
        print('\n')

def root(tex_print, x):
    if isinstance(x, dict):
        tex_print("\\begin{tikzpicture}[\n")
        tex_print("  sibling distance=10em,\n")
        tex_print("   every node/.style = {shape=rectangle, draw, align=center}\n")
        tex_print("]\n")
        tex_print('\\')
        yaml_to_latex(tex_print, x)
        tex_print(';\n')
        tex_print("\\end{tikzpicture}")
        return
    if isinstance(x, list):
        assert len(x) == 1
        return root(tex_print, x[0])
    raise TypeError(x)


def simple_tree(src: dev.Group, *, self: dev.Interpreter, tex_print, expand=""):
    from gkdtex.builtins import PY_NAMESPACE
    expand_opts = eval('{' + expand + '}', self.state[PY_NAMESPACE])
    if expand_opts and isinstance(expand_opts, dict) and expand_opts.get('before'):
        src = dev.eval_to_string(self, src.obj)
    else:
        src = dev.get_raw_from_span_params(self.src, src.offs)

    result = yaml.load(src, yaml.SafeLoader)
    if expand_opts and isinstance(expand_opts, dict) and expand_opts.get('after'):
        raise NotImplementedError
    else:
        root(tex_print, result)

class GkdInterface:
    @staticmethod
    def load(self, tex_print):
        tex_print("\\usetikzlibrary{matrix}\n")
        self.globals['gkd@simpletree'] = simple_tree
