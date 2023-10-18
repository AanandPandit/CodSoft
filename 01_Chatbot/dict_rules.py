import random

# ----------------------------dictionary-------------------------------------------------
# greeting response
greeting = [
    "Hello! Welcome to our chatbot. How can I assist you today?",
    "Hi! How can I assist you today?",
    "Hi, is there anything I can assist you with?",
    "Hey, what can I do for you?",
    "Hi, it's great to see you!",
    "Hey, how can I make your day better?"
]
def get_greeting():
    return random.choice(greeting)


# jokes repsonse
jokes = [
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Parallel lines have so much in common. It's a shame they'll never meet.",
    "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them.",
    "Why don't scientists trust atoms? Because they make up everything!",
    "How do you organize a space party? You 'planet'!",
    "What did one wall say to the other wall? I'll meet you at the corner!",
    "I used to play piano by ear, but now I use my hands.",
    "Why did the bicycle fall over? Because it was two-tired!",
    "Why don't oysters donate to charity? Because they are shellfish!",
    "What do you call a fish with no eyes? Fsh!"
]
def get_random_joke():
    return random.choice(jokes)


# exiting response
exiting_message = [
    "Goodbye! Have a great day!",
    "If you need further assistance in the future, don't hesitate to reach out. Have a wonderful day!",
    "I hope our conversation was helpful. If you have more to discuss, just come back anytime.",
    "Goodbye, and remember, I'm here whenever you need assistance or just want to chat."
]
def get_exit_message():
    return random.choice(exiting_message)

# book list
book_list = ("To Kill a Mockingbird by Harper Lee",
                 "1984 by George Orwell",
                 "The Great Gatsby by F. Scott Fitzgerald",
                 "Pride and Prejudice by Jane Austen",
                 "The Catcher in the Rye by J.D. Salinger",
                 "The Lord of the Rings by J.R.R. Tolkien",
                 "The Hobbit by J.R.R. Tolkien",
                 "Harry Potter and the Sorcerer's Stone by J.K. Rowling",
                 "The Da Vinci Code by Dan Brown",
                 "The Hunger Games by Suzanne Collins"
)
def get_book_list():
    return "\n".join(book_list)


# -----------------------------------main_rules-----------------------------------------------------
# dictionary
rules = {
    # introduction of Chatbot.
    r"(hi|hello|hey|greeting|hlo)": get_greeting,
    r"(how are you|how's it going|how's life)": "I'm just a computer program, so I don't have feelings, but I'm here and ready to help you with any questions or tasks you have. How can I assist you today?",
    r"(what is your name|who are you)": "I'm a chatbot designed to help you with information and tasks.",
    r"(bye|goodbye|see you later)": get_exit_message,
    r"(how is your day|your day)": "my day is good.",
    r"(max day|maximum day I can borrow book|for how many day I can borrow book|when to retrun book)":"You can take books maximum of two weeks and then it will be labelled Rs. 1 per day",
    r"(can i extend time)":"No you can't do that, you have to retake it.",
    r"(do you have online library)":"Yes you can check in our website or you can scan the QR and it will take you to website.",
    r"(thank|thanks|thank you)":"Its my pleasure to help, Visit again.",
    r"(where i find book|where is book)":"You can check book at second floor of the library.",

    # Jokes telling
    r"(tell me a joke|joke|jokes|funny facts)": get_random_joke,

    # list of book
    r"(list of books|books available|available books|what are the availabe books)": get_book_list,

    
}
