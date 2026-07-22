
"""strings are immutable so that they
can easily be shared between different parts
 of a program without the risk of them being 
 changed accidentally by some part of the program.
 this ensures the integriyty of the data structure
 across the platform."""



s = "hello"
# print(s[0])
'''this is allowed as we're trying to access
the element'''

# s[0] = "H"
# print(s)
'''not allowed as we're trying to modify an immutable object''' 



s = s.replace("h", "H")
print(s)
"creates a new string with first letter H and assigns it "
"back to s"