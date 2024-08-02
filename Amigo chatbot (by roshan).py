#its a simple bot that can answer your questions.
#first we use import function
import random#for convo
import re#for  arithmetic calculations
import turtle#for drawing 
import pyjokes#for jokes
joke = pyjokes.get_joke()
#si = p * r * t #simple interest
turtle.speed(10)  #speed for turtle pen
#its a group for eg a=1,2,3
responses = {
#conversation
    "hi": "Hello!",
    "how are you?": "i am good, thank you.",
    "what's your name?": "i am Amigo.",
    "bye": "Goodbye!",

    "default": "Sorry, i don't understand that. Please search your query on Goggle or any other platforms. Thank you.",#default message

    "who created you": "i am created by Roshan Adhikari.",
    "what is your age": " i was created on 12 july 2024.",
    "where do you live" :"i am a bot, i live in beautiful clouds,but my creator is from bhowali.",
    "tell me about your creator": "Here are the following details-\n1-He is a boy\n2-He is in class 11(PCM)\n3-He like playing games\n4-He studies in Devito School Bhowali.",
    "what is nega": "nega is you.",
    "yo":"english or spanish",
    "english": "who ever moves first is dumb",
    "spanish": "el que se mueve primero es dumb",
    "tell a joke": "why was 10 scared?\nbcoz he was in between 9 and 11",
    "who is father of maths": "Archimedes is widely regarded as one of the greatest mathematicians in history,\nearning him the title of the Father of Mathematics.\nBorn in Syracuse, Sicily, in 287 BC, Archimedes was a polymath who made significant contributions to a wide range of fields,\nincluding mathematics, physics, engineering, and astronomy.",
    "who invented zero": "zero was invented by a Indian mathematicician named Arya bhatta.",
    "joke":"joke above ",
    "who are you": " i am Amigo your favourite ai chatbot",
    "si":'above is your simple interest',
    "a": "above is your amount",



#trigonometric ratios
    "sin0":"0",
    "sin30":"1/2",
    "sin45":"1/2^1/2",
    "sin60":"3^1/2 /2",
    "sin90":"1",

    
    "cos0":"1",
    "cos30":"3^1/2 /2",
    "cos45":"1/2^1/2",
    "cos60":"1/2",
    "cos90":"0",

    
    "tan0":"0",
    "tan30":"1/3^1/2",
    "tan45":"1",
    "tan60":"3^1/2",
    "tan90":"not defined",


#conversation 
    "what do you like":"i like to answer the questions you ask",
    "weather":"check on google buddy",
    "how is your day": "My day is going well! I'm always learning new things.",
    "what are you doing": "I'm here to chat and help you with anything you need. What would you like to talk about?",
   
    "who invented computer":"Charles Babbage (born December 26, 1791, London, England—died October 18, 1871, London) was an English mathematician and inventor who is credited with having conceived the first automatic digital computer.",
    "do you watch anime":"yes i love to watch anime. Few anime i would like to recommend you are\n1-Vinland Saga\n2-naruto\n3-jjk\netc",
    "tell me the names of some popular games":"--->some popular games are as follows\n1-football\n2-cricket\n3-basketball\n--->some of the popular online games are\n1-bgmi(Battle Grounds Mobile India)\n2-ff(Free fire)\n3-minecraft\n4-valorant\n5-fortnite\netc ",




}
#Capitals
Capitals = {
#states
"Andhra Pradesh" : { "Capital" :"Amaravati", "Year_of_establishment":"2014"},
"Arunachal Pradesh" : "Itanagar",


#Countries
"India" : {"Capital":"New Delhi", "Year_of_establishment": "1947"},

}
#it is also a group for elements and their atmoic number and symbol
elements = {
    "hydrogen": {"atomic_number": 1, "symbol": "H"},
    "helium": {"atomic_number": 2, "symbol": "He"},
    "lithium": {"atomic_number": 3, "symbol": "Li"},
    "beryllium": {"atomic_number": 4, "symbol": "Be"},
    "boron": {"atomic_number": 5, "symbol": "B"},
    "carbon": {"atomic_number": 6, "symbol": "C"},
    "nitrogen": {"atomic_number": 7, "symbol": "N"},
    "oxygen": {"atomic_number": 8, "symbol": "O"},
    "fluorine": {"atomic_number": 9, "symbol": "F"},
    "neon": {"atomic_number": 10, "symbol": "Ne"},
    "sodium": {"atomic_number": 11, "symbol": "Na"},
    "magnesium": {"atomic_number": 12, "symbol": "Mg"},
    "aluminum": {"atomic_number": 13, "symbol": "Al"},
    "silicon": {"atomic_number": 14, "symbol": "Si"},
    "phosphorus": {"atomic_number": 15, "symbol": "P"},
    "sulfur": {"atomic_number": 16, "symbol": "S"},
    "chlorine": {"atomic_number": 17, "symbol": "Cl"},
    "argon": {"atomic_number": 18, "symbol": "Ar"},
    "potassium": {"atomic_number": 19, "symbol": "K"},
    "calcium": {"atomic_number": 20, "symbol": "Ca"},
    "scandium": {"atomic_number":21, "symbol":"Sc"},
    
}


#turtle
#turtle is used here for drawing shapes
def draw_square(size):
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)


def draw_triangle(size):
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)


def draw_circle(radius):
    turtle.circle(radius)
    
def draw_shape(shape, size):
    turtle.clear()
    if shape == "square":
        draw_square(size)
    elif shape == "triangle":
        draw_triangle(size)
    elif shape == "circle":
        draw_circle(size)
    else:
        turtle.write("i cant draw this shape", align="center", font=("Arial", 12, "normal"))#this is error bcoz only the shapes in bot memory will be drawn

#Important for main working of Amigo
def get_response(message):

   
    
    if message in responses:#this will check if msg is in present in group
        return responses[message]#this will give output to que which is in his memory
    
    
    elif re.match(r'^[\d+\-*/. ()]+$', message):  #these are arithmetic expressions
        #here the operations will be done
        try:
            result = eval(message)#eval means evaluate for eg like eval(2*2) it will give 4 bcoz it evaluates any arithmetic expresssion
            return f"The result is: {result}"
        except Exception as e:
            print(e)#this is for exception which this bot cannot do
            return "Sorry, I am weak in calculations."#this will be output after exception
    
    
    elif message in elements:#this will check that the elements u entered is in this bots memory or not
        #if it is in presnt in group then following will work
        element_info = elements[message]
        atomic_number = element_info["atomic_number"]
        symbol = element_info["symbol"]
        return f"{message.capitalize()} (Symbol: {symbol}, Atomic Number: {atomic_number})"#this is ouput for elements
    
    
    
    
    elif message in Capitals:#this will check for states and capitals
        state_info = Capitals[message]
        Capital = state_info["Capital"]
        Year_of_establishment = state_info["Year_of_establishment"]
        return f"{message.capitalize()} (Capital: {Capital}, Year_of_establishment: {Year_of_establishment})"#this is for states

    #this is for turtle
    #this will check if the draw cmd is right or wrong
    elif message.startswith("draw"):
        parts = message.split()
        if len(parts) == 3:
            shape = parts[1]
            size = int(parts[2])
            draw_shape(shape, size)
            return f"Drawing {shape} with size {size}."#this is ouput which is given during drawing is processed
        else:
            return "wrong draw command. Use 'draw shape size' (e.g., draw square 100). If not type bye.)"#this is error caused when u enter wrong cmd
    else:
        return responses["default"]#if these things are not are in bot memory then it will send  a default msg

#greet
print("Welcome to the chat ! Type 'bye' to exit.")
print("You can ask me to do the following things.")
print("1-Normal conversation\n2-Arithmetic calculations\n3-Draw shapes\n4-Elements and their atomic number and symbol\n5-Capitals of states and countries")
while True:#while loop so it asks everytime
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Amigo: Goodbye!")
        break
#for jokesssssss
    elif user_input.lower() == 'joke':
        print(joke)
# forsimple interest
    elif user_input.lower()=='si':
        p = int(input("principal:"))
        r = int(input("rate:"))
        t = int(input("time:"))
        si = int(p) * int(r) * int(t) / 100 
        print("simple interest:",si)
#for amount
    elif user_input.lower()=='a':
        p = int(input("principal:"))
        r = int(input("rate:"))
        t = int(input("time:"))
        a = p * (1+r/100)**t
        print("amount:",a)


    
    response = get_response(user_input)#this will see the input then ans the que from his memory
    print("Amigo:", response)#this is output which will be given everytime
turtle.done()#stopping turtle

