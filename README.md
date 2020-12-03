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
\documentclass{article}
\usepackage{tikz} % use LaTex package 
\usepackage{amsfonts}
\usepackage{amssymb}

\begin{document}

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
\end{document}
```

![simpletree](simpletree.PNG)
