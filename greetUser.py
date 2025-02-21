import datetime  # Importing the datetime module to work with date and time

def greet(name):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Getting the current date and time
    print(f"Hello, {name}!")  # Greeting the user
    print(f"Welcome to the world of coding. The current date and time is: {current_time}")  # Displaying the current date and time
    print("Here are some motivational quotes to inspire you:")  # Informing the user about the motivational quotes
    quotes = [
        "Code is like humor. When you have to explain it, it’s bad.",
        "Experience is the name everyone gives to their mistakes.",
        "In order to be irreplaceable, one must always be different.",
        "Java is to JavaScript what car is to Carpet.",
        "Knowledge is power."
    ]
    for quote in quotes:  # Looping through the list of quotes
        print(f"- {quote}")  # Printing each quote

def add_quote(quotes, new_quote):
    quotes.append(new_quote)  # Adding a new quote to the list
    return quotes  # Returning the updated list of quotes
quotes = [
    "Code is like humor. When you have to explain it, it’s bad.",
    "Experience is the name everyone gives to their mistakes.",
    "In order to be irreplaceable, one must always be different.",
    "Java is to JavaScript what car is to Carpet.",
    "Knowledge is power."
]

# Adding a new quote
add_quote(quotes, "The only way to do great work is to love what you do.")  # Adding a new motivational quote to the list

greet("GitHub Copilot")  # Calling the greet function with the name "GitHub Copilot"