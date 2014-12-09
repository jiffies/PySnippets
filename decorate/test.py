import tempfile
import sys

temp=tempfile.TemporaryFile()
a=sys.stdout
sys.stdout = temp

print "abcdddd"
temp.write("33333")
temp.seek(0)
sys.stdout=a

print "read",temp.read()
temp.close()
