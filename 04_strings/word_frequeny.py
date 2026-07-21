

def  word_frequency(text):
    counted_chars = ''
    
    for ch in text:
        if ch not in counted_chars:
            frequency = text.count(ch)
            print(f"{ch}:{frequency}")
            counted_chars+=ch
            


def main():
    text = input('Enter the text :')
    word_frequency(text)
    
if __name__=="__main__":
    main()
    