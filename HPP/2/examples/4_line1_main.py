import os

os.system('kernprof -l 4_line1.py')
os.system('ipython -m line_profiler 4_line1.py.lprof')