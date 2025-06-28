# Import necessary modules
import nltk
from nltk.chat.util import Chat, reflections

# Define conversation patterns (regex + responses)
chat_pairs = [
    [r"hi|hello|hey",
     ["Hello! How can I assist you today?",  
      "Hey there! How can I help you today?"]],

    [r"how are you\??",
     ["I'm just code, but I'm functioning perfectly! How about you?",  
      "I'm just a bot, but I feel great! How about you?"]],

    [r"(what is|what's) your name\??",
     ["You can call me ChatBot.I'm your Python-powered assistant!", 
      "I'm AssistBot — here to chat and help."]],

    [r"(what can you do|help)\??",
     ["I can answer basic questions, define programming terms, and tell jokes. Try asking me something!",
      "I can answer simple questions, explain Python topics, and even tell a few jokes! Ask me anything."]],

    [r"(who made you|who created you)\??",
     ["I was created by a programmer using Python and NLTK."]],

    [r"tell me something cool",
     ["You can use Python to build apps, analyze data, or automate boring tasks.",
      "Here's something cool: Python is named after Monty Python, not the snake!"]],

    [r"tell me a joke",
     ["What do you call a snake that works on a computer? A Python developer!"]],

    [r"any funny fact about coding",
     ["A programmer’s favorite debugging tool? Staring at the screen until the bug runs away."]],

    [r"tell me a programming fact",
     ["Python was named after the comedy group Monty Python, not the snake."]],
    
    [r"what is python\??",
     ["Python is a popular, high-level programming language known for being Simple but Great."]],

    [r"why should I learn python\??",
     ["Because it’s beginner-friendly, powerful, and used in AI, web, automation, and more!"]],

    [r"what is recursion\??",
     ["Recursion is when a function calls itself... wait, didn’t I just say that?"]],

    [r"how do i learn python\??",
     ["Start with small projects, practice daily, and never fear errors — they’re just stepping stones."]],

    [r"what is a chatbot\??",
     ["A chatbot is a program that simulates human conversation using rules or AI. Like me!"]],

    [r"what is (natural language processing|NLP)\??",
     ["NLP is a field of AI that allows computers to understand, interpret, and respond to human language."]],

    [r"Thats great",
     ["Thanks! for the compliment!"]],

    # Exiting the conversation
    [r"(bye|exit|quit)",
     ["Goodbye! It was nice answering your queries."]],

    # Fallback for unknown input
    [r"(.*)",
     ["I'm not sure how to respond to that. Could you try rephrasing?",
      "That's interesting... but I might need more context to answer."]]
    ]

# Function to start the chatbot interaction
def start_chat():

    # Display welcome message
    print("\n" + "="*55)
    print("Welcome to ChatBot")
    print("I'm here to answer your questions and doubts.")
    print("Type 'bye' or 'exit' to end the conversation.")
    print("="*55 + "\n")
    # Create a Chat instance with the defined pairs and reflections
    chatbot = Chat(chat_pairs, reflections)
    chatbot.converse()  # Start conversation loop

# Run the chatbot
if __name__ == "__main__":
    start_chat()
