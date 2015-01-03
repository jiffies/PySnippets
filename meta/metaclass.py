deving
class MyType(type):
    def __new__(cls,cname,supers,cdicts):
        for k,v in cdicts.items():
            print k,v
        cdicts['c']=lambda self,c: c
        return type.__new__(cls,cname,supers,cdicts)


    def __init__(self,cname,supers,cdicts):
        cdicts['d'] = lambda self,d: d
        print cname,supers,cdicts

class Model(object):
    __metaclass__ = MyType
    field_num = 0
    def a(self):
        print "aaaaa"

    @classmethod
    def b(cls):
        print cls.field_num


if __name__ == "__main__":
    m=Model()
    m.a()
    Model.b()
    print m.c(10)
    print m.d(10)
