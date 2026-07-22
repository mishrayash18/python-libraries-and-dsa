s = {"abc", "xyz", "pqrs", "efg"}
# print(s)
"they dont maintain any order"
"duplicate items are ignored"


empty_dict = {} 
"this creates an empty dictionary"

empty_set = set() 
"this creates an empty set"





"built in methods of sets"
"Add"

s.add(4)
# print(s)



"remove"

s.remove("abc")
# print(s)



"discard"

s.discard("sbc")
"safer than remove as it does nothing if"
"the element is not present in the set"
# print(s)



"pop"

s.pop()
"removes an element randomly from the set"
# print(s)



"clear"

s.clear()
"wipes out the entire set"