
** HOW TO RUN QUICKSORT **
PYTHON:
- from bash call: python test-harness.py
- displayed will be preferred file/s to operate on, input integer corresponding to preference
- code should then run, output results to log-file.dat

C++ Stretch Goal:
- if you wish to recompile: g++ -o name_for_out quick sort.cpp
- then call: ./name_for_out file_path size
	- file_path = path of file to sort
	- size = size of static array, eg. For ints-100k.dat size = 100000
- Segmentation fault will occur with ints-10m.dat


Tests longer than 15s:
- ints-10m.dat ~ 42.8s
- floats-10m.dat ~ 42.7