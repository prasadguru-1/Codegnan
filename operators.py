Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# bitwise
>>> a=3
>>> b=4
>>> a&b
0
>>> a=2
>>> b=5
>>> a&b
0
>>> a=5
>>> b=7
>>> a&b
5
>>> bin(3)
'0b11'
>>> bit(4)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    bit(4)
NameError: name 'bit' is not defined. Did you mean: 'bin'?
>>> bin(4)
'0b100'
>>> bin(2)
'0b10'
>>> bin(5)
'0b101'
>>> a=6
>>> b=8
>>> a&b
0
>>> a=7
>>> b=9
>>> a&b
1
>>> a=7
>>> b=9
>>> a|b
15
>>> a=9
>>> ~a
-10
>>> a=3
>>> b=9
>>> a^b
10
>>> #leftshita=3
>>> a=6
>>> a<<3
48
>>> #rightshift
>>> a=4
>>> a>>2
1
