import sys


class test:
    def __enter__(self):
        print ("enter")
        return 66

    def __exit__(self, exc_type, exc_val, exc_tb):
        print ("exit")
        return True


def testWith1():
    with test() as t:
        print "t is not the result of test(),it is _enter_ returned"
        print ("t is 1,yes,it is {0}".format(t))
        raise NameError("Hi there")
        sys.exit()
        print "Never here"
# testWith1()


def TestWith2():
    with open("myfile.txt") as f:
        for line in f:
            print (line)
    f.readline()  # f is already clean up here, here will meet ValueError exception

# TestWith2()


class controlled_execution(object):
    def __init__(self, filename):
        self.filename = filename
        self.f = None

    def __enter__(self):
        try:
            f = open(self.filename, 'r')
            content = f.read()
            return content
        except IOError  as e:
            print (e)

    def __exit__(self, type, value, traceback):
        if self.f:
            print ('type:%s, value:%s, traceback:%s' % (str(type), str(value), str(traceback)))
            self.f.close()


def TestWithAndException():
    with controlled_execution("myfile.txt") as thing:
        if thing:
            print(thing)
TestWithAndException()
