# An Authentic LaTeX Conversion Template for Jupyter Notebooks.
A more accurate representation of jupyter notebooks when converting to pdf.
This template was designed to make converted jupyter notebooks look (almost) identical to the actual notebook. If something doesn't exist in the original notebook then it doesn't belong in the conversion.

This repository also acts as a reference for how to package nbconvert templates to be pip installable without using exporters and entry points.

## Improvements
1. \maketitle is removed (If you want a title then add a markdown cell to the top of your notebook).
2. Sections are no longer numbered automatically.
3. Syntax highlighting improvements. (Bonus if using XeLaTeX)
4. "\LaTeX" and "\TeX" are no longer converted into a logo on conversion to pdf unless they are in math mode. (replicating the functionality of these commands in notebook markdown).
3. ~~Markdown paragraphs are no longer auto-indented in the pdf.~~ **(This change was merged into nbconvert 5.5.0)**
6. ~~**BOXES!** are drawn around code cells.~~ **(This change was merged into nbconvert 5.5.0)**
7. ~~In/Out counts will move to the left as the execution count increases instead of pushing code to the right (only numbers are displayed by default to save page width).~~ **(This change was merged into nbconvert 5.5.0)**
8. ~~$\LaTeX$ and $\Tex$ in markdown cells will no longer cause conversion to fail.~~ **(This change was merged into nbconvert 5.4.0)**
9. ~~In/Out prompt colours updated to match Jupyter.~~ **(This change was merged into nbconvert 5.5.0)**
10. ~~Output text wrapping improvements.~~ **(This change was merged into nbconvert 5.5.0)**
11. ~~Code cell text wrapping.~~ **(This change was merged into nbconvert 5.5.0)**

Quick Comparison:
![comparison](example/comparison.png)
for a closer look see the example directory.

## Pygments

This repository also contains a pygments style called jupyter_python that can be used programmatically and was used in previous versions of the template. Syntax highlighting improvements are done without the style though as it was insufficient to achieve the highlighting quality I wanted, and it needed a shell escape.

## Installation
If you have multiple python interpreters installed, but sure to install on the one with nbconvert. Otherwise, the templates will be put into the wrong data folder.

```bash
pip install nb_pdf_template
```

### Updating
```bash
pip install -U nb_pdf_template
```

### Manual Install:
Drop the "latex_authentic" folder into the folder containing the other LaTeX nbconvert templates. If using anaconda, it should be something like: 
> */Anaconda3/share/jupyter/nbconvert/templates

### Uninstalling
```bash
pip uninstall nb_pdf_template
```
or if manually installed then remove the files manually.

## Use
From the command line:
```bash
jupyter nbconvert --to pdf filename.ipynb --template latex_authentic
```

You can add ```--template-file m.tex.j2``` to change the index file of the template to the one with the prompts above the cells instead of to the left of the cells.

Adding:
```python
c.LatexExporter.template_file = 'latex_authentic'
```
to the ```jupyter_nbconvert_config.py``` file will let you drop the "--template latex_authentic", and to the ```jupyter_notebook_config.py``` file will let you use "download as pdf" from within the Jupyter notebook/lab with the template.

## Build

To build the package use
```bash
hatch build
```

## Tips (Good for any template)
[Moved to the wiki](https://github.com/t-makaro/nb_pdf_template/wiki/Tips)
