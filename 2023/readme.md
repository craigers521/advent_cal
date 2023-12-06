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
----  

