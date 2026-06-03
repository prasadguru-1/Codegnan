Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #datatypes
>>> a=5
>>> type(a)
<class 'int'>
>>> b=6.7
>>> type(b)
<class 'float'>
>>> c="code"
>>> type(c)
<class 'str'>
>>> d="python"
>>> type(d)
<class 'str'>
>>> e='''course'''
>>> type(e)
<class 'str'>
>>> f=4+9j
>>> type(f)
<class 'complex'>
>>> g=4j+3
>>> type(g)
<class 'complex'>
>>> x=6j
>>> type(x)
<class 'complex'>
>>> z=true
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    z=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> z=True
>>> type(z)
<class 'bool'>
>>> y=False
>>> tyep(y)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    tyep(y)
NameError: name 'tyep' is not defined
>>> a=9
>>> b=10
>>> a+b
19
>>> #datatype conversions
>>> #int(8)
>>> int(8)
8
>>> int("hi")
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    int("hi")
ValueError: invalid literal for int() with base 10: 'hi'
#str
str(8)
'8'
str(7.8)
'7.8'
str("guru")
'guru'
str(5+9j)
'(5+9j)'
str(True)
'True'
str(False)
'False'
#complex
complex(5+9j)
(5+9j)
complex(True)
(1+0j)
complex(False)
0j
#bool
bool(8)
True
bool(5.7)
True
bool("html")
True
bool(5+7j)
True
