#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I


a) O(n). This one is deceptive and seems like O(n^3). However, it will only run until it hits it limit.


b) O(n^2). This example shows a nested for loop which means the n/input is being looped over two times every single run of the function. The runtime will become slower as the size of n increases exponentially.



c)  0(n). Recursive functions allow the input to only have to be looped through one time; keeping the runtime fast even as n increases in size



## Exercise II

### UNDERSTANDING: 
    n-story building, plenty of eggs
    
    egg breaks n-story >= f
    egg ! break n-story < f

    value of f 
    number of dropped + broken eggs is minimized

* Need to determine at which floor = f has the least broken eggs when dropped at said floor

### PLANNING:
    
    1. Let min_floor = 0, max_floor = n
    2. Find the mid point between min and max: mid_floor = n//2
    3. Throw an egg from the mid point.
        a. if egg breaks, change max_floor = mid_floor
            repeat 2 and 3
        b. if egg doesn't break, change min_floor = mid floor
            repeat 2 and 3
    4. Return current floor if the floor below or above if the egg breaks

### RUN COMPLEXITY: 
    O(Log n) Because i am using a binary search. The function is repeatedly checked until the value is found.






