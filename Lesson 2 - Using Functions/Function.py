def say(phrase):
    print(phrase)
    
say("Python")

#############################################################

def yello(phrase):
    print(phrase.upper() + "!") #Where upper makes the characters to be uppercased
    
yello("Yepp")


#############################################################

def hey(phrase = "Gooden Morden"): #We can define a default value for the variables the function has
    print(phrase, '!')
    
hey()    
hey("Hello")