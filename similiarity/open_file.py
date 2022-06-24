import sys

def read_file(filename):
    try:
        with open(filename, 'r', errors='ignore') as f:
            data = f.read()
        return data
    except IOError:
        print("Cannot open file: ", filename)
        sys.exit()