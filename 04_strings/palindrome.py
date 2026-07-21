

def palindrome(text):
     reverse = text[::-1]
     
     if reverse ==text:
         print(f'{text} is  palindrome')
     else:
         print("Not palindrome")
         
         

def main():
    text  = input("Enter text to check wheather it is palindrome  :")
    (palindrome(text))
    
    
if __name__=="__main__":
    main()
    
    