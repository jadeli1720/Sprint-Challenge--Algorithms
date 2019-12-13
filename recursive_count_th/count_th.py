'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.

Understanding:
1. inputs: 1 word = sting
2. total count th occurs
3. Case Matters --> th count will only matter if the input includes lowercase. If it is "TH" then we don't add to count
4. use recursion - no loops
    recursion is a loop
5. needs to include if input is none count = 0

Plan:

1. Need to find all lowercase th
2. check combination of 2 letters along the length of the string
    isolate every 2 letters in string
3. for every 2 letter combination that has "th" add to count (but can use for loop)
    count_th +1???


'''
def count_th(word):
    print(len(word)) # wreath length ==> 6
    
    print(word[0:2]) # isolates 2 letters


count_th("wreath")