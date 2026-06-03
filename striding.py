Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #starding
>>> a="data science"
>>> a[::]
'data science'
>>> a[::1]
'data science'
>>> a=[::2]
SyntaxError: invalid syntax
>>> a[::2]
'dt cec'
>>> a="cloud computing"
>>> a[::4]
'cdmi'
>>> 
>>> a[::3]
'cucpi'
>>> a[::6]
'cci'
>>> a[3:6]
'ud '
>>> a[:9]
'cloud com'
>>> a[:7]
'cloud c'
>>> a[7:]
'omputing'
>>> a=[2:14:4]
SyntaxError: invalid syntax
>>> a[2:14:4]
'ocu'
>>> a[3:15:5]
'umn'
>>> a[1:12:2]
'lu opt'
>>> a=mechaning learning
SyntaxError: invalid syntax
>>> D
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    D
NameError: name 'D' is not defined
>>> a="python course"a
SyntaxError: invalid syntax
>>> a="pytjhon course"
>>> #negative
>>> a="python course"
>>> a[-1:-11:-4]
'eoo'
>>> a[-3:-13:-5]
'rn'
