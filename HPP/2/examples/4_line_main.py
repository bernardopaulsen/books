import os

os.system('kernprof -l 4_line.py')
os.system('ipython -m line_profiler 4_line.py.lprof')