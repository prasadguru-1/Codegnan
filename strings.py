Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
#len()
a="codegnan"
len(a)
8
b="python course"
len(b)
13
c=" "
len(c)
1
d="guru prsad"
len(d)
10
#count()
a="guru prasd"
a.(a)
SyntaxError: invalid syntax
a.(g)
SyntaxError: invalid syntax
a."twinkle"
SyntaxError: invalid syntax

a=("twinkle")
a.count("k")
1
a.count("l")
1
a.count(" ")
0
#find a string
a="python"
a.find("h")
3
a.find("n")
5
b="hello"
b.find("l")
2
#escape sequences
#\n->new line
#\t->tab space
a="name\nmailid\tmobileno"
print(a)
name
mailid	mobileno
b="name:guruprasad\nmailid:prasadguru@.com\tmobileno
SyntaxError: unterminated string literal (detected at line 1)
prinnt(b)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    prinnt(b)
NameError: name 'prinnt' is not defined. Did you mean: 'print'?
b="name:guruprasad\nmailid:prasadguru@.com\tmobileno:9398595097
SyntaxError: unterminated string literal (detected at line 1)
>>> b="name:guruprasad\nmailid:prasadguru@.com\tmobileno:9398595097"
>>> print(b)
name:guruprasad
mailid:prasadguru@.com	mobileno:9398595097
>>> #replace()
>>> a="wait until you succeseed"
>>> a.replace("wait","work")
'work until you succeseed'
>>> b="guruprsad from chittoor"
>>> a.replace("from","a")
'wait until you succeseed'
>>> #upper()
>>> a="code"
>>> a.upper()
'CODE'
>>> b="guruprasad"
>>> a.upper()
'CODE'
>>> b.upper()
'GURUPRASAD'
>>> c="prasadguru"
>>> c.lower()
'prasadguru'
>>> d="guruprasad"
>>> d.capitalize()
'Guruprasad'
>>> e="python"
>>> e.capitalize()
'Python'
>>> a="hello'
SyntaxError: unterminated string literal (detected at line 1)
>>> a="hello"
>>> a.isupper()
False
>>> a.lower()
'hello'
>>> #strip()
>>> #lstrip(),rstrip()
>>> a="     guru"
>>> a.strip()
'guru'
>>> b="   prasad     "
>>> a.rstrip()
'     guru'
>>> #split()
>>> a="python java c c++"
>>> a.split()
['python', 'java', 'c', 'c++']
>>> b="guru from to chittoor"
>>> b.split()
['guru', 'from', 'to', 'chittoor']
