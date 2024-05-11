from random import choice

from src.pokeneas.pokenea import Pokenea


pokeneas = [
    Pokenea(
        1,
        "Meowgician",
        "3 feet tall on Tuesdays, 1 inch tall on Wednesdays",
        "Can summon catnip storms at will",
        "https://storage.googleapis.com/pockeneas-images/Meowgician.jpeg",
        "In the litter box of life, always bury your past."
    ),
    Pokenea(
        2,
        "Fluffzilla",
        "Variable, depending on the level of static electricity in the air",
        "Can turn anything into a pillow with a touch",
        "https://storage.googleapis.com/pockeneas-images/Fluffzilla.jpeg",
        "Life's too short to be serious, unless you're a giraffe."
    ),
    Pokenea(
        3,
        "Gigglesnort",
        "6 inches when standing, 10 feet when bouncing",
        "Can make opponents laugh uncontrollably with a silly dance",
        "https://storage.googleapis.com/pockeneas-images/Gigglesnort.jpeg",
        "If laughter is the best medicine, then I'm the pharmacy of joy!"
    ),
    Pokenea(
        4,
        "Spaghettopus",
        "2 feet tall when dry, 20 feet tall when wet",
        "Can turn into any pasta dish at will",
        "https://storage.googleapis.com/pockeneas-images/Spaghettopus.jpeg",
        "Life is a noodle, slurp it up before it slurps you."
    ),
    Pokenea(
        5,
        "Sir Crispy",
        "3 feet tall in the morning, 1 foot tall at night",
        "Can summon maple syrup rain showers",
        "https://storage.googleapis.com/pockeneas-images/Sir%20Crispy.jpeg",
        "To butter or not to butter, that is the breakfast."
    ),
    Pokenea(
        6,
        "Techno-tail",
        "1 foot tall, but appears as 10 feet tall in digital environments",
        "Can hack into any electronic device with a flick of its tail",
        "https://storage.googleapis.com/pockeneas-images/Techno-tail.jpeg",
        "In the binary of life, always remember to byte back."
    ),
    Pokenea(
        7,
        "Yawnicorn",
        "5 feet tall when awake, 50 feet tall when asleep",
        "Can create dream bubbles that make others fall asleep instantly",
        "https://storage.googleapis.com/pockeneas-images/Yawnicorn.jpeg",
        "Dream big, nap bigger.",
    ),
    Pokenea(
        8,
        "Pranksterpus",
        "2 feet tall on Mondays, 6 inches tall on Fridays",
        "Can swap personalities with anyone it touches",
        "https://storage.googleapis.com/pockeneas-images/Pranksterpus.jpeg",
        "Life's a joke, might as well be the punchline."
    )
]

def get_random_pokenea() -> Pokenea:
    return choice(pokeneas)