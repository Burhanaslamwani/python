import re
string = """Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, and a syntax that allows programmers to express concepts in fewer lines of code,[25][26] notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales.[27]

Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.[28]

Python interpreters are available for many operating systems. CPython, the reference implementation of Python, is open source software[29] and has a community-based development model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation."""
new_str = re.sub(r'is',"IS",string)
#print(new_str)
for m in re.finditer("is",string):
    print("is on index", m.start(),m.end())

 
