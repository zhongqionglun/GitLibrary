#!---UTF.8---


"""
def function to test with as statement
"""


def function1():
    with open('readme.txt', 'w') as fp:
        fp.write("this is a 'read me' file")
    # fp = open('readme.txt', 'w')
    # fp.write("now we open the file to write again!")
    with open('readme.txt', 'r') as fp:
        print(fp.read())
if __name__ == "__main__":
    function1()
