import os
os.system('pygmentize -f tex -S default > pygments.sty')
os.system('pweave -f texpygments main.texw')
os.system('pdflatex -shell-escape main.tex')
