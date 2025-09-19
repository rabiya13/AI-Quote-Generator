import random

# -------------------------------
# 1. Dataset: Unique Quotes
# -------------------------------
quotes = [
    "Dreams are blueprints of the reality you are yet to build.",
    "Every small step is a silent victory toward greatness.",
    "Stars cannot shine without embracing the dark sky.",
    "Learning is not a race; it is the art of constant becoming.",
    "Your mind is a garden—plant curiosity and harvest wisdom.",
    "The strongest bridges are built from failures turned lessons.",
    "Time whispers truth to those patient enough to listen.",
    "Greatness is found not in noise, but in consistent effort.",
    "Courage begins where comfort ends.",
    "Ideas are seeds; action is the sunlight that makes them grow."
]

# Synonym dictionary for NLP tweaks
synonyms = {
    "dreams": ["visions", "aspirations", "imaginings"],
    "reality": ["world", "life", "existence"],
    "learning": ["growth", "knowledge", "discovery"],
    "courage": ["bravery", "valor", "fearlessness"],
    "wisdom": ["insight", "understanding", "enlightenment"],
    "failure": ["setback", "struggle", "obstacle"],
    "greatness": ["excellence", "mastery", "glory"],
    "ideas": ["thoughts", "concepts", "inspirations"]
}

# -------------------------------
# 2. Function: Apply NLP tweaks
# -------------------------------
def tweak_quote(quote):
    words = quote.lower().split()
    new_words = []
    for word in words:
        clean_word = word.strip(".,!?;")
        if clean_word in synonyms:
            # Replace with random synonym
            new_word = random.choice(synonyms[clean_word])
            new_words.append(new_word)
        else:
            new_words.append(word)
    tweaked = " ".join(new_words).capitalize()
    return tweaked

# -------------------------------
# 3. Generate AI Quote
# -------------------------------
def generate_quote():
    original = random.choice(quotes)
    tweaked = tweak_quote(original)
    print("\n✨ AI Quote Generator ✨\n")
    print("Original:", original)
    print("AI Tweaked:", tweaked)

# -------------------------------
# 4. Run Program
# -------------------------------
if __name__ == "__main__":
    generate_quote()
