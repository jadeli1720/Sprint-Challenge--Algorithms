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

1. Account for if the input is empty or less than 2.
    if it is return 0 else do the following:
2. Need to find all lowercase th
3. check combination of 2 letters along the length of the string
    isolate every 2 letters in string
4. for every 2 letter combination that has "th" add to count (but can use for loop)
    count_th +1???

5. can we use .find() ?
Syntax:
    str.find(sub[, start[, end]] )

Parameters:
    The find() method takes maximum of three parameters:
        *sub - It's the substring to be searched in the str string.
        *start and end (optional) - substring is searched within str[start:end] --> slice
        
Return Value:
    The find() method returns an INTEGER value.
        *If substring exists inside the string, it returns the index of first occurence of the substring.
        *If substring doesn't exist inside the string, it returns -1. 

'''
def count_th(word):
    
    # If the length of word is 0 or less than 2 retrun 0
    if len(word) == 0 or len(word) < 2:
        return 0
    
    #Initialize count to 0. Will add the number of time "th" is found
    count = 0
    # Initialize find_word using .find() to locate "th" in string. 
    find_word = word.find("th") 
    # print("Find word",find_word)
    
    #if result of find_word is not -1
    if find_word != -1:
        # add to the count ---> += allows to iterate?
        count += 1
        # print("Count", count)

        # Use recursion to check the string for other th's
        #count = incrementing through string in groups of 2 to find "th" and adding it to  count
        count += count_th(word[int(find_word) + 2:])
        # print("recursion", count)

    # return the total number of times "th" was found through the string
    return count

# print("Calling function",count_th("wreath"))
print("Calling function",count_th("thhtthht"))