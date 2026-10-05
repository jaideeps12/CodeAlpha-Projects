import random

words = [# Animals
    "aardvark", "albatross", "alligator", "alpaca", "anaconda", "antelope", "ape", "armadillo", 
    "baboon", "badger", "barracuda", "bat", "bear", "beaver", "bee", "bison", "boar", "buffalo", 
    "butterfly", "camel", "capybara", "caribou", "cassowary", "cat", "caterpillar", "cattle", 
    "chamois", "cheetah", "chicken", "chimpanzee", "chinchilla", "chough", "clam", "cobra", 
    "cockroach", "cod", "cormorant", "coyote", "crab", "crane", "crocodile", "crow", "curlew", 
    "deer", "dinosaur", "dog", "dogfish", "dolphin", "donkey", "dormouse", "dotterel", "dove", 
    "dragonfly", "duck", "dugong", "dunlin", "eagle", "echidna", "eel", "eland", "elephant", 
    "elk", "emu", "falcon", "ferret", "finch", "fish", "flamingo", "fly", "fox", "frog", "gaur", 
    "gazelle", "gerbil", "giraffe", "gnat", "gnu", "goat", "goldfinch", "goldfish", "goose", 
    "gorilla", "goshawk", "grasshopper", "grouse", "guanaco", "gull", "hamster", "hare", "hawk", 
    "hedgehog", "heron", "herring", "hippopotamus", "hornet", "horse", "hound", "hummingbird", 
    "hyena", "ibex", "iguana", "impala", "jackal", "jaguar", "jay", "jellyfish", "kangaroo", 
    "kingfisher", "koala", "kookabura", "kouprey", "kudu", "lapwing", "lark", "lemur", "leopard", 
    "lion", "llama", "lobster", "locust", "loris", "louse", "lyrebird", "magpie", "mallard", 
    "manatee", "mandrill", "mantis", "marten", "meerkat", "mink", "mole", "mongoose", "monkey", 
    "moose", "mosquito", "mouse", "mule", "narwhal", "newt", "nightingale", "octopus", "okapi", 
    "opossum", "ostrich", "otter", "owl", "oyster", "panther", "parrot", "partridge", "peafowl", 
    "pelican", "penguin", "pheasant", "pig", "pigeon", "pony", "porcupine", "porpoise", "quail", 
    "quelea", "quetzal", "rabbit", "raccoon", "rail", "ram", "rat", "raven", "reddeer", "redpanda", 
    "reindeer", "rhinoceros", "rook", "salamander", "salmon", "sandpiper", "sardine", "scorpion", 
    "seahorse", "seal", "shark", "sheep", "shrew", "skunk", "snail", "snake", "sparrow", "spider", 
    "spoonbill", "squid", "squirrel", "starling", "stingray", "stinkbug", "stork", "swallow", 
    "swan", "tapir", "tarsier", "termite", "tiger", "toad", "trout", "turkey", "turtle", "viper", 
    "vulture", "wallaby", "walrus", "wasp", "weasel", "whale", "wildcat", "wolf", "wolverine", 
    "wombat", "woodcock", "woodpecker", "worm", "wren", "yak", "zebra",
    
    # Technology & Computers
    "algorithm", "bandwidth", "binary", "browser", "byte", "cache", "chip", "cloud", 
    "compiler", "cookie", "cyber", "database", "debug", "desktop", "digital", "disk", 
    "domain", "download", "driver", "email", "encryption", "ethernet", "firewall", "firmware", 
    "flash", "folder", "gateway", "gigabyte", "graphics", "hardware", "hash", 
    "host", "html", "hyperlink", "interface", "internet", "intranet", "java", "javascript", 
    "kernel", "keyboard", "keyword", "laptop", "linux", "login", "malware", "matrix", 
    "memory", "microchip", "modem", "monitor", "motherboard", "mouse", "multimedia", 
    "netbook", "network", "node", "notebook", "offline", "online", "open", "operating", 
    "packet", "password", "patch", "phishing", "pixel", "platform", "plugin", "podcast", 
    "port", "portal", "print", "processor", "protocol", "python", "query", "queue", 
    "ram", "recovery", "redirect", "redundancy", "router", "runtime", "scanner", "script", 
    "security", "server", "silicon", "smartphone", "software", "spam", "speaker", "spreadsheet", 
    "spyware", "storage", "streaming", "switch", "syntax", "tablet", "terminal", 
    "thread", "token", "trojan", "unix", "update", "upload", "url", "user", "utility", 
    "vector", "version", "video", "virtual", "virus", "webcam", "website", "widget", 
    "wiki", "windows", "wireless", "workflow", "workstation", "worm", "xml", "zip",
    
    # Geography & Countries
    "afghanistan", "albania", "algeria", "andorra", "angola", "antigua", "argentina", "armenia", 
    "australia", "austria", "azerbaijan", "bahamas", "bahrain", "bangladesh", "barbados", "belarus", 
    "belgium", "belize", "benin", "bhutan", "bolivia", "bosnia", "botswana", "brazil", "brunei", 
    "bulgaria", "burkina", "burundi", "cambodia", "cameroon", "canada", "chad", "chile", 
    "china", "colombia", "comoros", "congo", "croatia", "cuba", "cyprus", "denmark", "djibouti", 
    "dominica", "ecuador", "egypt", "eritrea", "estonia", "eswatini", "ethiopia", "fiji", 
    "finland", "france", "gabon", "gambia", "georgia", "germany", "ghana", "greece", "grenada", 
    "guatemala", "guinea", "guyana", "haiti", "honduras", "hungary", "iceland", "india", 
    "indonesia", "iran", "iraq", "ireland", "israel", "italy", "jamaica", "japan", "jordan", 
    "kazakhstan", "kenya", "kiribati", "kosovo", "kuwait", "kyrgyzstan", "laos", "latvia", 
    "lebanon", "lesotho", "liberia", "libya", "liechtenstein", "lithuania", "luxembourg", 
    "madagascar", "malawi", "malaysia", "maldives", "mali", "malta", "mauritania", "mauritius", 
    "mexico", "micronesia", "moldova", "monaco", "mongolia", "montenegro", "morocco", "mozambique", 
    "myanmar", "namibia", "nauru", "nepal", "netherlands", "nicaragua", "niger", 
    "nigeria", "norway", "oman", "pakistan", "palau", "panama", "paraguay", "peru", 
    "philippines", "poland", "portugal", "qatar", "romania", "russia", "rwanda", "samoa", 
    "senegal", "serbia", "seychelles", "singapore", "slovakia", "slovenia", "somalia", 
    "spain", "sudan", "suriname", "sweden", "switzerland", "syria", "taiwan", "tajikistan", 
    "tanzania", "thailand", "togo", "tonga", "tunisia", "turkey", "turkmenistan", "tuvalu", 
    "uganda", "ukraine", "uruguay", "uzbekistan", "vanuatu", "vatican", "venezuela", "vietnam", 
    "yemen", "zambia", "zimbabwe"]

word = random.choice(words)
guessed = []
wrong_guesses = 0
max_attempts = 6

hangman = [
    """
     -----
     |   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]

print("Welcome to Hangman!")
print("Hint: The word is a fruit.")

while wrong_guesses < max_attempts:

    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print(hangman[wrong_guesses])
    print("Word:", display)

    if "_" not in display:
        print("Congratulations! You won!")
        print("The fruit was:", word)
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    if guess in guessed:
        print("You already guessed that letter.")
        continue

    guessed.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

else:
    print(hangman[wrong_guesses])
    print("Game Over!")
    print("The fruit was:", word)