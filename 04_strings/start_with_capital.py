


def capital_start(text):
    
    for ch in text:
        if ch == text[0]:
          text[0] =  ch.upper()
        elif ch == ' ':
            text[ch+1] =ch.upper()
            
    return text

text = "john don"
capital_start(text)
            
    
            