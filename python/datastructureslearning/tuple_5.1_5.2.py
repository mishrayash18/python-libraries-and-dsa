# t = (1,2,3,4)
# print(t)
# print(type(t))
"immutable"

# t1=(1)
# print(type(t1))

"to create a tuple with single element, we need to put a coma"
"after the element otherwise it is declared as variable"

# t2 = (2,)
# print(type(t2))






"tuple is not fully immutable"
# t = (1,2,3,[4,5])   
# t[3][0] = 5
# print(t[3])




"packing, unpacking"
"packing"
# value = 1,2,3,4,5,6
# print(value)


"unpacking"
# a,b,c,d,e,f = value
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)


# a,b,c, *rest= value
# print(rest)