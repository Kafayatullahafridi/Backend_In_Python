

def vowels(text):
    
 text = text.lower()
 vowels = "aeiou"
 count = 0
 for ch in text:
    if ch in vowels:
        count+=1
 return count

def main():
    text  = input("Enter text to find vowels in it :")
    print(vowels(text))
    
    
if __name__=="__main__":
    main()