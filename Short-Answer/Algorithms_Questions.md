# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0                  #: O(1) ==> constant
    while (a < n * n * n): #: O(1) ==> constant just comparing and does not impact the growth of n
      a = a + n * n        #: O(n) ==> This is what increases the the output

```


```python
b)  sum = 0             # O(1) ===> constant
    for i in range(n):  # O(n) ===> looping through the input
      j = 1             # O(1) ===> constant
      while j < n:      # O(log n) ===> slightly slower
        j *= 2          # O(1) ===> constant --> j= j*2
        sum += 1        # O(1) ===> constant

# n * log n

```

``` python
c)  def bunnyEars(bunnies):
      if bunnies == 0:                  #O(1)  ===> constant
        return 0                        #O(1)  ===> constant

      return 2 + bunnyEars(bunnies-1)   # 2 + O(n)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.
