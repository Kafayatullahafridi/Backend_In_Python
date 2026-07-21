

def remove_duplicate(text):
    
    result =''
    for ch in text:
        if ch not in result:
            result+=ch
            
    return result

def main():
    text  = input("Enter text to remove duplicate  it :")
    print(remove_duplicate(text))
    
    
if __name__=="__main__":
    main()