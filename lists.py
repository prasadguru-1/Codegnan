Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#tuple
a="data science"
a[::]
'data science'
a[::1]
'data science'
a[::2]
'dt cec'
b="cloud computing"
a[::]
'data science'
b[::]
'cloud computing'
b[::4]
'cdmi'
a[::3]
'dacn'
b[::6]
'cci'
b[::6]
'cci'
b[3:6]
'ud '
b=[:9]
SyntaxError: invalid syntax
b[7:]
'omputing'
c="machine learning"
c[::]
'machine learning'
c[1:10:3]
'ai '
c[2:14:4]
'cea'
c[3:15:5]
'hli'
c[1:12:2]
'ahn er'
#negative
a="python"
a[-1:6:-2]
''
a=[-1:-6:-2]
SyntaxError: invalid syntax
a[-2:-9:-1]
'ohtyp'
#lista
a=[3,5.6,"python",8+9j,True,false]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a=[3,5.6,"python",8+9j,True,false]
NameError: name 'false' is not defined. Did you mean: 'False'?
a=[3,5.6,"python",8+9j,True,False]
print(a)
[3, 5.6, 'python', (8+9j), True, False]
type(a)
<class 'list'>
type(b)
<class 'str'>
c=[8.9]
type(c)
<class 'list'>
#methods
a=["python","java","c"]
a.append("ml")
a
['python', 'java', 'c', 'ml']
a.append(["c++","ml"])
a
['python', 'java', 'c', 'ml', ['c++', 'ml']]
a=["apple","banana",]
a.exend(["mango","grapes"])
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a.exend(["mango","grapes"])
AttributeError: 'list' object has no attribute 'exend'. Did you mean: 'extend'?
a.extend(["mango","grapes"])
a
['apple', 'banana', 'mango', 'grapes']
a[black',"white","red"]
  
SyntaxError: unterminated string literal (detected at line 1)
a=["black","white","red"]
  
a.insert(1,"pink")
  
a
  
['black', 'pink', 'white', 'red']
#index
  
a=["ml","ai","ds"]
  
a.index("ds')
        
SyntaxError: unterminated string literal (detected at line 1)
a.index("ds")
        
2
a.copy()
        
['ml', 'ai', 'ds']
b=a.copy()
        
b
        
['ml', 'ai', 'ds']
b
        
['ml', 'ai', 'ds']
a=["yellow","green","red"]
        
a.sort()
        
a
        
['green', 'red', 'yellow']
b=[1,2,4,6,7,12,11,18,]
        
b.sort()
        
b
        
[1, 2, 4, 6, 7, 11, 12, 18]
>>> a=["vij","hyd","vzg"]
...         
>>> a
...         
['vij', 'hyd', 'vzg']
>>> a.reverse()
...         
>>> a
...         
['vzg', 'hyd', 'vij']
>>> a=["python",java","c"]
...    
SyntaxError: unterminated string literal (detected at line 1)
>>> a=["python",java","c"]
...    
SyntaxError: unterminated string literal (detected at line 1)
>>> a=["python","java","c"]
...    
>>> a.pop()
...    
'c'
>>> a
...    
['python', 'java']
>>> a.pop(1)
...    
'java'
>>> a=["hi","hello","how"]
...    
>>> len(a)
...    
3
>>> b="hello"
...    
>>> len(b)
...    
5
>>> a=["python","java"]
...    
>>> a.clear()
...    
>>> a
...    
[]
>>> b=[]
...    
>>> b.append("guru")
...    
>>> b
...    
['guru']
