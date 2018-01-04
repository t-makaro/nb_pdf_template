# jupyter.tplx
A more accurate representation of jupyter notebooks when converting to pdfs.

This template was designed to make converted jupyter notebooks look (almost) identical to the actual notebook. If something doesn't exist in the original notebook then it doesn't belong in the conversion.

## Improvements
1. \maketitle is removed (If you want a title then add a markdown cell to the top of your notebook)
2. Sections are no longer numbered automatically (notebooks don't number sections so the pdf shouldn't)
3. **BOXES!** are drawn around code cells.
4. In/Out will move to the left as the execution count increases instead of pushing code to the right.
5. $\LaTeX$ and $\Tex$ in markdown cells will no longer cause conversion to fail
6. In/Out text colours updated to match Jupyter
7. Markdown paragraphs are no longer auto-indented in the pdf

## Installation

### Manually:
drop the files "jupyter.tplx" and "style_jupyter.tplx" into the folder containing the other LaTeX nbconvert templates. If using anaconda, it should be something like: 
> */Anaconda3/Lib/site-packages/nbconvert/templates/latex

### Automatically:
Warning this was only been tested on windows.
```
pip install nb_pdf_template
python -m nb_pdf_template.install.py
```

## Use
From the command line:
> jupyter nbconvert --to pdf filename.ipynb --template jupyter.tplx

Adding:
```
c.LatexExporter.template_file = 'jupyter.tplx'
```
to the ```jupyter_nbconvert_config.py``` file will let you drop the "--template jupyter.tplx", and to the ```jupyter_notebook_config.py``` file will let you use "download as pdf" from within the Jupyter notebook.

## Issues (in common with default template)
1. raw pyout text will not wrap text
2. code cells will not wrap text (at 86 characters the text will spill into the margin)

## Issues (unique to this template)
1. If a code cell is too long to fit on one page it will not overflow onto the next page.

## Tips (Good for any template)
1. Want to remove page numbers? Add "\pagenumbering{gobble}" to a raw cell at the top of the notebook.
2. Want to set page numbers to start at a specific number? Add "\setcounter{page}{number_here}" to a raw cell at the top of the notebook.
3. Want to re-add the maketitle? Add:
```
\author{name}
\title{title}
\date{date}
\maketitle
```
to a raw cell at the top of the notebook to customize the maketitle.
