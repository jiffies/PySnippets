a = range(10)
for index,value in enumerate(a,start=4):
    print index,value

d = dict(zip("abc",[1,2,3]))
print d
for k,v in dict.iteritems(d):
    print k,v

def my_range(number):
    i = 0
    while i<number:
        yield i
        i+=1

if __name__ == "__main__":
    print my_range(17)
    print iter(my_range(17))
    print iter(my_range(17)).next()
    #for i in my_range(17):
        #print i
