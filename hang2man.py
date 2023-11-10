
graphic = [
        """
            +-------+
            |
            |
            | 
            |
            |
         ==============
        """
            ,
        """
            +-------+
            |       |
            |       0
            | 
            |
            |
         ==============
        """
            ,
        """
            +-------+
            |       |
            |       0
            |       |
            |
            |
         ==============
        """
            ,
        """
            +-------+
            |       |
            |       0
            |      -|
            |
            |
         ==============
        """
            ,
        """
            +-------+
            |       |
            |       0
            |      -|-
            |
            |
         ==============
        """
            ,
        """
            +-------+
            |       |
            |       0
            |      -|-
            |      /
            |
         ==============
        """
            ,
        """
            +-------+
            |       |
            |       0
            |      -|-
            |      / \
            |
         ==============
        """]
import random
word_list = ["Apple", "Banana", "Cherry", "Date", "Eggplant", "Figs", "Grape", "Honeydew", "Iguana", "Jackal", "Kiwi", "Lemon", "Mango", "Nectarine", "Orange", "Papaya", "Quince", "Raspberry", "Strawberry", "Tomato", "Umbrella", "Violet", "Watermelon", "Xylophone", "Yogurt", "Zebra", "Ant", "Bear", "Cat", "Dog", "Elephant", "Fox", "Giraffe", "Horse", "Iguana", "Jaguar", "Kangaroo", "Lion", "Monkey", "Nightingale", "Octopus", "Penguin", "Quokka", "Raccoon", "Squirrel", "Tiger", "Umbrella", "Vulture", "Walrus", "X-ray", "Yak", "Zebra", "Astronomy", "Biology", "Chemistry", "Drama", "Economics", "French", "Geography" "Amethyst", "Beehive", "Cucumber", "Dolphin", "Eagle", "Flamingo", "Gazelle", "Hyena", "Ibis", "Jellyfish", "Koala", "Lemur", "Mantis", "Nightingale", "Ocelot", "Puma", "Quail", "Rhinoceros", "Salamander", "Tapir", "Uakari", "Vervet", "Wombat", "X-ray", "Yeti", "Zucchini", "Alchemy", "Botany", "Cryptocurrency", "Dramatic", "Esoteric", "Futuristic", "Gourmet", "Harmonious", "Intricate", "Juxtapose", "Kaleidoscopic", "Luminous", "Mysterious", "Nurturing", "Oblivion", "Philosophy", "Quintessential", "Rhapsodic", "Serendipity", "Transformation", "Unicorn", "Vivid", "Whimsical", "Xenophile", "Yesteryear", "Zeppelin", "Ambiguous", "Benevolent", "Cacophony", "Dandelion", "Effervescent", "Felicity", "Gossamer", "Hypnotic", "Incandescent", "Juxtaposition", "Kaleidoscope", "Labyrinth", "Melancholy", "Nostalgia", "Obliterate", "Peregrine", "Quotidian", "Reticent", "Surreptitious", "Talisman", "Ubiquitous", "Vexatious", "Whispering", "Xenophobes", "Yesteryears", "Zephyr"]
#randomly choose a word from the above list assign it a variable of chosen word
random_number = random.randint(0, len(word_list) - 1)
word_chosen = word_list[random_number].lower()
word_chosen = list(word_chosen)
#generate as many blanks as the number of letters in the word chosen
length = 0
blanks = []
for length in range(len(word_chosen)):
    blanks += "-"
    length += 1
width = 0
word2chosen = len(word_chosen)
while width < len(word_chosen):
# used to achieve repetition
    if blanks == word_chosen:
        print("YOU LIVE")
        break
    else:
        print(graphic[width])
    guess = input(f"Guess the letters of the word you have {word2chosen} CHANCES TO LIVE\n")
    word2chosen -= 1
    for l in range(len(word_chosen)) :
        letter = word_chosen[l]
        if guess == letter:
            blanks[l] = letter    
        else:
            pass
    width += 1
    print(blanks)
blanks = str(blanks)
word_chosen = str(word_chosen)
if blanks == word_chosen:
    print(f"{blanks}")
    print("you win")
else:
    print("YOU DIE")
    print()
    
