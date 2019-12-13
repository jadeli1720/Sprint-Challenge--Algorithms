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

5. can we use .find() ---> returns the lowest index of the sub string if it is found in the given string. If it is not found then it returns -1

    *str.find(sub[, start[, end]] )
    *sub - It's the substring to be searched in the str string.
    *start and end (optional) - substring is searched within str[start:end] -->slice

'''
def count_th(word):
    print("Word length",len(word)) # wreath length ==> 6
    # If the length of word is 0 or less than 2 retrun 0
    if len(word) == 0 or len(word) < 2:
        return 0

    count = 0
    find_word = word.find("th") 
    print("Find word",find_word)
    
    #if find word is 
    if find_word != -1:
        # print(True)
        # add to the count
        count += 1
        print("Count", count)

        # Use recursion to check the string for other th's


print("Calling function",count_th("wreath"))
# print("Calling function",count_th("thhtthht"))