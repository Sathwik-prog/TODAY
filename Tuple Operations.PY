# create a tuple with different data types
tuplex = ("tuple", False, 3.2, 1)
print(tuplex)

# create a tuple
tuple = (4, 6, 2, 8, 3, 1)
print(tuplex)
#tuples are immutable, so you cannot add new elements
#using merge of tuples with + operator you can add a element and it will create a new tuple
tuplex = tuplex + (9,)
print(tuplex)

#Counts the number of occurences of item 50 from a tuple
tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))

#create a tuple
tuplex = (2, 4, 3, 5, 6, 7, 8, 6, 1)
#used tuple[start:stop] the start index is inclusive and the stop index_slice = tuplex[3:5]
#is exclusive
_slice = tuplex[3:5]
print(_slice)
#if the start index is'nt defined, is taken from the beg inning of the tuple
#if the start index is'nt defined, is taken from the beg inning of the tuple
_slice = tuplex[:6]
print(_slice)