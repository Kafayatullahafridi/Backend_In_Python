
def anagram(text1,text2):
    lower_text1 =text1.lower()
    lower_text2 = text2.lower()
    
    if sorted(lower_text1 )==sorted(lower_text2):
     print('true')
        

def main():
    text1  = input("Enter text to find anagram  it :")
    text2  = input("Enter text to anagram  it :")
    (anagram(text1,text2))
    
    
if __name__=="__main__":
    main()
    