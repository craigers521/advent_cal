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
- all function returns true if all evaluations are true, boolean values can be used in math (false=0, true=1)
- **list comprehension - use it** any time i am creating an empty list and for looping to append values, just use list comprehension


------- 


### Soln Ref: 
day 1:
- elegant solution with regex: https://github.com/xb4r7x/adventOfCode/blob/main/2023/1/day1.py
- elegant enumerate https://github.com/jonathanpaulson/AdventOfCode/blob/master/2023/1.py 

day 2: 
- yeah ok just watch this jonathonpaulson guy 
- https://github.com/casellimarco/raoc/blob/main/2023/q2/main.py using counters
----  

