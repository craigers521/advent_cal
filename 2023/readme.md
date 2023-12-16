## 2023 
Lets go! 

----  
### Lessons Learned: 
day 1: 
- newer regex module "regex" backwards compatible with re but adds functionality like finding overlapping substrings with findall  

day 2: 
- `string.split()` you can do direct variable assignment rather than output a list
- provide a second position argument to `dict.get(keynamevar, default)` to return a default value if key doesnt exist
- also can use a defaultdict from collections: `from collections import default dict`, which helps you deal with missing keys or assign default values to dict
- more useful collections: counter - count unique elements, can be compared
- `all()` function returns true if all evaluations are true, boolean values can be used in math (false=0, true=1)
- **list comprehension - use it** any time i am creating an empty list and for looping to append values, just use list comprehension

day 3:
- back to the complex numbers to model x,y grid, tricks include nested enumerate for easy x,y coords and mapping of complex class to single letter name for easy referencing  

day 4: 
- rather than compare one list to values in a number list with a for loop, make each a set and intersection (`&`) the sets
- optimization: dont make copies and compare all copies, if you know that its going to be the same result, just add that result for x copies

day 5:
- generally broke me on part 2... some tricks tho
- unpacking multiple inputs into a single var: `thing, *stuff = input.split('wtvr')`
- use map to call something on everything in a list, handy for converting lists datatypes `list(map(int, thing.split()))`
- class method `__repr__` for friendly troubleshooting of class objects with nice data  

day 6: 
- map, filter and reduce just for one-liners and getting fancy with lambdas: https://stackabuse.com/map-filter-and-reduce-in-python-with-examples/
- the "right" approach is to use the quadratic formula, brute force works tho
- `eval()` vs `int()` for string to integer converstion:  https://mhrprogramming.medium.com/issues-in-converting-strings-using-eval-and-int-functions-in-python-programming-3d2e3a6ac573 ( TL;DR is eval works on all kinds of things like floats, expressions, hex, etc but int works on strings with leading zeros)

day 7: 
- follow an assertion up with an f-string for easy troubleshooting without a bunch of prints:  `assert (test[1] > test[0]), f'{test}'`
- collections Counter builds a dict with counts instead of you having to do it with defaultdict and loop
- use ord to flip string char to ascii value and then ord to flip it back for easy comparisons of non-integer string values or double-digit values `hand.replace('K',chr(ord('9')+4))`

day 8: 
- the trick here is about syncing up multiple cycles, rather than continually cycling and checking if everyone is in sync, cycle each once then find the least common multiple of all them.  Python doesnt have a nice way to take lcm of a list of ints so have to write your own

day 10: 
- pt 1 pretty straighforward using our grid techniques, just exit the pipe legal direction for the pipe you are in but dont go to a pipe you have already been to, until you get back to S
- pt 2 the trick is imagine your pipe as a polygon, a few tricks to find if point is in polygon:  
    - raycast any direction, odd number of intersections is in polygon. This is tricky for what i call "edge riding" but if you imagine the pipe zoom in you only cross sections that exit vertically up if casting through "top portion" of square (see pipespace.txt)
    - use matplotlib.Path and shapely to cheat
    - take area of polygon using shoelace formula

day 11:
- grid approach but interesting technique was to calculate my position shift by evaluating if current position was less than one of the shifting row/col.  Because that evals as a Boolen i can sum up the trues to gift the shift amount, this can be multiplied then for larger factor shifts
- set math again easy for not verifiy in if value in list
- for complex points distance using only up,down,left,right is calculated using "manhattan distance" aka diff in x + diff in y

day 12:
- git gud at recursion... 
- fun technique is to set set a cache dictionary, use function input as unique key and store result for quick lookups later... or just use lru_cache from functools

day 13: 
- adding `[::-1]` reverses a list, but you can also do that on a sliced list like `mylist[:r][::-1]`
- zip an unpacked list of lists to transpose it (aka rotate 90) like `list(zip(*mylst))`

day 14: 
- i could have made this a lot easier by just rotating the grid and then i would always "roll" the same direction
- another handy trick i saw was to split strings on '#', sort them, then rejoin on '#', this "rolls" by moving all rocks to the left

day 15:
- i didnt implement this but another handy module from collections is the "OrderedDict"... its a dict that maintains key order for insertion/deletion but still lets you update in values without changing position

day 16:
- set operations on a set produces a new set... so you need to do things like `set |= otherset` or just `set.update(otherset)`, if you just `set | otherset` the resultant new set goes into the ether
------- 


### Soln Ref: 
day 1:
- elegant solution with regex: https://github.com/xb4r7x/adventOfCode/blob/main/2023/1/day1.py
- elegant enumerate https://github.com/jonathanpaulson/AdventOfCode/blob/master/2023/1.py 

day 2: 
- yeah ok just watch this jonathonpaulson guy 
- https://github.com/casellimarco/raoc/blob/main/2023/q2/main.py using counters  

day 3:
- using complex number grid https://www.youtube.com/watch?v=xmfHyglUV1Q

day 5: johnny p again and been liking [this guy](https://www.youtube.com/watch?v=b8ka6eZ4Vbk&t=11s)

day 6:
- quad formula walkthru: https://github.com/mebeim/aoc/blob/master/2023/README.md#day-6---wait-for-it 

day 12: recursion
 - https://www.youtube.com/watch?v=g3Ms5e7Jdqo
 - https://www.youtube.com/watch?v=n-6-J1O1tIU
----  

