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
- gotta brush up on that regex, `r'somestring'` is a raw string allowing you to escape characters and still use regex special chars. aka an actual backslash vs a \d or an actual parenthesis vs a capture group

day 4:
- complex number grid i cant quit you.  One of my favorite benefits of parsing a grid into a dictionary with keys as complex numbers, you need to track length and width of the array.  If its a key in your dictionary its within the grid, if its not its not. And checking if adjacency is within the grid boils down to simple addition/subtraction of complex number.  added benefit for part 2, inverse complex number inverts both the real and imag parts.  so complex(1,-1) becomes complex(-1,1) etc. 

day 5: 
- really gross approach to finding bad/good sorted pages but it worked.  Part 2 i stole someones bubble sort algorithm. 

day 6: index mod len(list) trick for cycling through list elements

day 7: i'll never really understand recursion

day 8: for part2 i could allow duplicates in the list (or rather inverse pairs) and then just vector out from each number individually but it was such a small dataset i went fast and dirty