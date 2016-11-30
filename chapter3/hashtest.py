import hashlib
import sys

filename = sys.argv[0]
read_file = file(filename)
the_hash = hashlib.md5()
for line in read_file.readlines():
    the_hash.update(line)
print the_hash.hexdigest()
