## 2024
Lets go! 

----  
### Lessons Learned: 
day 1: 
- forgot about python Collections module with handy defaultdict and Counter dictionary subclasses.  Counter is useful here, just go ahead and count everything in right list and then you can just reference left list to see if it exists and if it does return the count

day 2: 
- sorted() function can be used in comparison operators
- map can be used rather than list comprehension to convert datatypes `list(map(int, line.split()))`

day 3:
- gotta brush up on that regex

day 4:
- complex number grid i cant quit you.  One of my favorite benefits of parsing a grid into a dictionary with keys as complex numbers, you need to track length and width of the array.  If its a key in your dictionary its within the grid, if its not its not. And checking if adjacency is within the grid boils down to simple addition/subtraction of complex number.  added benefit for part 2, inverse complex number inverts both the real and imag parts.  so complex(1,-1) becomes complex(-1,1) etc. 