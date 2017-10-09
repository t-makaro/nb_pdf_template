# jupyter.tplx
A more accurate representation of jupyter notebooks when converting to pdfs.

This template was designed to make converted jupyter notebooks look (almost) identical to the actual notebook. If something doesn't exist in the original notebook then it doesn't belong in the conversion.

## Installation

drop the files "jupyter.tplx" and "style_jupyter.tplx" into the folder containing the other LaTeX nbconvert templates. It should be something like: 
> */Anaconda3/Lib/site-packages/nbconvert/templates/latex

## Use
From the command line:
> jupyter nbconvert --to pdf filename.ipynb --template jupyter.tplx

I have yet to discover a way to get the 'download as pdf' option from jupyter notebook to default to this template.

## Improvements
1. \maketitle is removed (If you want a title then add a markdown cell to the top of your notebook)
2. Sections are no longer numbered automatically (notebooks don't number sections so the pdf shouldn't)
3. **BOXES!** are drawn around code cells.
4. In/Out will move to the left as the execution count increases instead of pushing code to the right.
5. $\LaTeX$ and $\Tex$ in markdown cells will no longer cause conversion to fail
6. In/Out text colours updated to match Jupyter

## Issues (in common with default template)
1. raw pyout text will not wrap text
2. code cells will not wrap text (at 86 characters the text will spill into the margin)

## Issues (unique to this template)
1. If a code cell is too long to fit on one page it will not overflow onto the next page.
