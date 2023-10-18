import re
import datetime
from dict_rules import get_exit_message, rules  


# function for chatbot repsonse
def chatbot_response(user_input):
    user_input = user_input.lower()

    for pattern, response in rules.items():
        if re.search(pattern, user_input):
            if callable(response):
                return response()
            else:
                return response
    return "I didn't get that, Could you please rephrase that?"

# get the date and time for naming the chat log file
current_datetime = datetime.datetime.now()
date_time_str = current_datetime.strftime("%y%m%d%H%M")
# name the file with date and time
chat_log_filename = f"{date_time_str}.txt"

with open(chat_log_filename, 'w') as chat_log:
    print('\n   Welcome to Library\nI am chatbot, you can ask me query about books.\n')
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            exit_message = get_exit_message()
            print()
            print("Chatbot:", exit_message)
            break
        response = chatbot_response(user_input)
        if callable(response):  # Check if the response is a function
            print("Chatbot:", response())
            print()
        else:
            print("Chatbot: " + response)
            print()
        chat_log.write(f"You: {user_input}\n")
        chat_log.write(f"Chatbot: {response}\n")

