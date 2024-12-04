# classic.tplx
A more accurate representation of jupyter notebooks when converting to pdfs.
This template was designed to make converted jupyter notebooks look (almost) identical to the actual notebook. If something doesn't exist in the original notebook then it doesn't belong in the conversion.

## Update for 7.0

Work is in progress for updating this for nbconvert 7.0. Minimal changes were needed to make the template itself work, so it should work with nbconvert 6.0 as well, but officially nbconvert 5 and 6 won't be supported. Once I have figured out the new template install process, I will push a release.

## Improvements
1. \maketitle is removed (If you want a title then add a markdown cell to the top of your notebook).
2. Sections are no longer numbered automatically (notebooks don't number sections so the pdf shouldn't).
8. Markdown paragraphs are no longer auto-indented in the pdf.
9. Syntax highlighting improvements. (Bonus if using XeLaTeX)
3. ~~**BOXES!** are drawn around code cells.~~ **(This change was merged into nbconvert 5.5.0)**
4. ~~In/Out counts will move to the left as the execution count increases instead of pushing code to the right (only numbers are displayed by default to save page width).~~ **(This change was merged into nbconvert 5.5.0)**
5. ~~$\LaTeX$ and $\Tex$ in markdown cells will no longer cause conversion to fail.~~ **(This change was merged into nbconvert 5.4.0)**
6. "\LaTeX" and "\TeX" are no longer converted into a logo on conversion to pdf unless they are in math mode. (This and the above point replicate the functionality of these commands in notebook markdown).
7. ~~In/Out prompt colours updated to match Jupyter.~~ **(This change was merged into nbconvert 5.5.0)**
10. ~~Output text wrapping improvements.~~ **(This change was merged into nbconvert 5.5.0)**
11. ~~Code cell text wrapping.~~ **(This change was merged into nbconvert 5.5.0)**

Quick Comparison:
![comparison](example/comparison.png)
for a closer look see the example directory.

## Installation

```
pip install nb_pdf_template
python -m nb_pdf_template.install
```

### Updating
```
pip install -U nb_pdf_template
python -m nb_pdf_template.install
```

### Manual Install:
Drop all of the "*.tplx" files into the folder containing the other LaTeX nbconvert templates. If using anaconda, it should be something like: 
> */Anaconda3/Lib/site-packages/nbconvert/templates/latex



## Use
From the command line:
```bash
jupyter nbconvert --to pdf filename.ipynb --template classic
```

Adding:
```python
c.LatexExporter.template_file = 'classic'
```
to the ```jupyter_nbconvert_config.py``` file will let you drop the "--template classic", and to the ```jupyter_notebook_config.py``` file will let you use "download as pdf" from within the Jupyter notebook.

Replace ```classic``` with your template of choice.

### Templates
This package offers the following templates:

Template | Use
---------|-------
classic.tplx **(Recommended)**| For most accurate recreation of the default Jupyter Notebook style.
classicm.tplx | m for modified. Similar to classic.tplx, but in/out prompts are above cells instead of in the margin. Bonus left margins are smaller so code cells are wider.

## Tips (Good for any template)
[Moved to the wiki](https://github.com/t-makaro/nb_pdf_template/wiki/Tips)
