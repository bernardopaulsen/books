import os

os.system('kernprof -l 2_4_lineprofiler.py')
os.system('python -m line_profiler 2_4_lineprofiler.py.lprof')
