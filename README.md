## gkdtikz

### Installation

```
pip install gkdtikz gkdtex
gkdtex src.tex
latexmk -pdf src.out.tex 
```

### gkdtiz

Writing simple trees via basic Yaml syntax.

```tex
\usepackage{tikz} % use LaTex package 

\gkd@usepackage{gkdtikz.tree} % use GkdTeX package

\gkd@simpletree{
root:
  - node 1:
    - $\mathbb{L}\mathrm{eaf} \; 1$
  - leaf 2 $\lambda$
  - node 2 $\gamma$:
    - $math$
    - normal:
      - \textbf{bold}
      - \textit{italic}
      - \textrm{roman}
}
```

![simpletree](simpletree.PNG)