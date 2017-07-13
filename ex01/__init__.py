import numpy as np

# if you want to import numpy library
# here is numpy zip file http://www.numpy.org/
# if you finished download. open cmd,
# input like this, python -m pip install [numpy path]\numpy-1.13.0+mkl-cp36-cp36m-win_amd64.whl
# If you installed successfully  , "Successfully installed numpy-1.13.0+mkl".

"""
you can use double quotation mark
multi-line comments

"""

# single-line comments using pound key

# In any case, It is same meaning using or not using about semicolon .
# But, when using over two sentences, you have to write it after last sentence.

class Study:
    def __init__(self):
        print("Initialized")

    def print_sth(self):
        print('hello')
        print(1 - 2)

    def print_formatting_01(self):
        print("{1} {0}".format('one', 'two'))

    def print_formatting_02(self):
        a = 5
        b = 10
        print("a + b = %d" % (a + b))
        print("{0} {1}".format(100, 200))

    def declaration_integer(self):
        aa = 10
        bb = 20
        print(aa + bb)

    def declaration_list(self):
        listA = [1, 2, 3, 4, 5, 6]
        print("{0}".format(listA))
        print("listA length = ", len(listA))

    def declaration_dictionary_01(self):
        dicA = {'key': 100}
        print(dicA['key'])

    def declaration_dictionary_02(self):
        dicA = {'key': 100}
        dicA['auth'] = 1313
        print(dicA['auth'])

    def declaration_boolean(self):
        play = True
        print(play)

    def statement_if(self):
        play = True
        if play:
            print("play")
        else:
            print("not play")

    def statement_for(self):
        for i in[1, 2, 3]:
            print("i = " ,i ,"\n")

    def numpy_Array(self):
        x = np.array([1.0, 2.0, 3.0])
        print(x)
        print(type(x))

    def numpy_operation(self):
        x = np.array([1, 2, 3])
        y = np.array([5, 6, 7])
        print('x[] + y[] = ' , x+y)
        print('x[] - y[] = ' , x-y)
        print('x[] * y[] = ' , x*y)
        print('x[] / y[] = ' , x/y)

    def numpy_multi_dimension(self):
        a = np.array([[1, 2], [3, 4]])
        b = np.array([[7, 8], [5, 6]])
        print(a)
        print(a.shape)
        print(a+b)

    def numpy_broadcast(self):
        a = np.array([[1, 2], [3, 4]])
        b = np.array([10, 30])
        print("a*b : " , a*b)

    def numpy_access_element(self):
        a = np.array([[0, 5], [10, 20], [22, 55]])
        print(a)
        print("a[0] : " ,a[0])
        print("a[0][1] : " ,a[0][1])

    def numpy_access_element_statement_for(self):
        a = np.array([[0, 5], [10, 20], [22, 55]])
        for row in a:
            print(row)

    def numpy_access_index_element(self):
        a = np.array([[0, 5], [10, 20], [22, 55]])
        a = a.flatten()
        print("flatten a : " ,a)
        print("a[np.array([0, 1, 4]) : " , a[np.array([0, 1, 4])])

    def numpy_specific_condition(self):
        a = np.array([[0, 5], [10, 20], [22, 55]])
        a = a.flatten()
        print("a > 15" , a>15)


# you can define functions

# creates a new instance of the class and assigns this object to the local variable s.
s = Study()

"""
self variable represents the instance of the object itself.
The __init__ method is roughly what represents a constructor in Python.
You have to declare it explicitly. When you create an instance of the something class and call its methods,
it will be passed automatically, ...
When you call constructor, Python creates an object for you, and passes it as the first parameter to the __init__ method.
__init__ is the constructor for a class. The self parameter refers to the instance of the object.
It is important to use the self parameter inside an object's method if you want to persist the value with the object.

"""

# call method

# example print
s.print_sth()

# formatting
s.print_formatting_01()

# Variable declaration
s.declaration_integer()

# list
s.declaration_list()

# dictionary
s.declaration_dictionary_01()

# add new element dictionary key, value
s.declaration_dictionary_02()

# bool variable type : True , False
s.declaration_boolean()

# if statement
s.statement_if()

# for statement
s.statement_for()

# using numpy library
s.numpy_Array()

# numpy operation
s.numpy_operation()
"""
element-wise product
"""

# numpy multi-dimension
s.numpy_multi_dimension()

"""
n-dimensional
one-dimensional : vector
two-dimensional : matrix
three-dimensional : tensor
"""

# numpy broadcast
s.numpy_broadcast()

# numpy access element
s.numpy_access_element()

# numpy access element by statement for
s.numpy_access_element_statement_for()

# numpy flatten
s.numpy_access_index_element()

# numpy specific condition
s.numpy_specific_condition()
