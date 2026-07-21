

def reverse(text):
    
    reverse = text[::-1]
    return reverse
def main():
    text  = input("Enter text to reverse  it :")
    print(reverse(text))
    
    
if __name__=="__main__":
    main()