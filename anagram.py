#an anagram of a string is another string that contains same char, only the order of characters are different
def anagram(s1,s2):
    
    if sorted(s1)==sorted(s2):
        print("yes")
    else:
       print("no")
s1=str(input(""))
s2=str(input(""))
anagram(s1,s2)
