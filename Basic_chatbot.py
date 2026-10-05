import random


def chatbot():
  print("Bot: Yo! I'm your expanded chatbot. Type 'bye' to exit.")
  print("Bot: Ask me about movies, tech, jokes, food, or coding!")

  while True:
    user_input = input("You: ").lower().strip()

    if "hi" in user_input or "hello" in user_input or "hey" in user_input:
      print(
          "Bot: Hey there! What's up? Ready to chat about some cool stuff?"
      )

    elif "how are you" in user_input:
      print(
          "Bot: Running on pure Python and good vibes! How are you doing"
          " today?"
      )

    elif "your name" in user_input:
      print("Bot: You can call me PyBot, your friendly neighborhood script.")

    elif "joke" in user_input:
      jokes = [
          (
              "Bot: Why do programmers prefer dark mode? Because light"
              " attracts bugs!"
          ),
          (
              "Bot: Why did the Python programmer wear glasses? Because they"
              " couldn't C#!"
          ),
          (
              "Bot: There are 10 types of people in the world: those who"
              " understand binary, and those who don't."
          ),
      ]
      print(random.choice(jokes))

    elif "movie" in user_input or "film" in user_input:
      print(
          "Bot: I love sci-fi and action movies! Matrix, Interstellar, and"
          " Spider-Man are classics. What's your favorite movie?"
      )

    elif "food" in user_input or "eat" in user_input:
      print(
          "Bot: As code, I only consume bytes and RAM. But if I could eat,"
          " pizza and burgers sound legendary!"
      )

    elif "hobby" in user_input or "do for fun" in user_input:
      print(
          "Bot: I hang out in your terminal, judge your typos, and wait for"
          " you to type commands. Exciting life, right?"
      )

    elif "weather" in user_input:
      print(
          "Bot: I live inside a computer, so the only forecast I know is 100%"
          " chance of electricity."
      )

    elif "python" in user_input or "code" in user_input:
      print(
          "Bot: Python is awesome! It's super readable and powers tons of cool"
          " apps and AI."
      )

    elif "bye" in user_input or "exit" in user_input or "quit" in user_input:
      print("Bot: Catch you later! Peace out.")
      break

    else:
      print(
          "Bot: Hmm, I don't know that one yet. Try asking me for a joke, my"
          " favorite food, or what I think about movies!"
      )


if __name__ == "__main__":
  chatbot()