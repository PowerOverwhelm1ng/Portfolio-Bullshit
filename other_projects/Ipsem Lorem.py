#daily disco quotes
import random
def main():

    disco_quotes = {
        "q_1": "There is nothing. Only warm, primordial blackness. Your conscience ferments in it — no larger than a single grain of malt. /n You don't have to do anything anymore. Ever. Never ever.",
        "q_2": "An inordinate amount of time passes. It is utterly void of struggle. No ex-wives are contained within it",
        "q_3": "The song of death is sweet and endless... But what is this? Somewhere in the sore, bloated *man-meat* around you — a sensation!",
        "q_4": "The limbed and headed machine of pain and undignified suffering is firing up again. It wants to walk the desert. Hurting. Longing. Dancing to disco music. -Ancient Reptilian Brain",
        "q_5": "That we continue to persist at all is a testament to our faith in one another.",
        "q_6": "We don’t have anything to talk about anymore. Every combination of words has been played out. The atoms don’t form us anymore: us, our love, our unborn daughters…— the ex-something",
        "q_7": "This is real darkness. It's not death, or war, or child molestation. Real darkness has love for a face. The first death is in the heart, Harry.-The Ex Something",
        "q_8": "You: I swore I wouldn't let you go. You *told* me — you asked me to be this way." "/n Dolores Dei: That was someone else. I betrayed her, overwrote her, and am happier for it."
    }

    def get_disco_quotes():
        quote_key = random.choice(list(disco_quotes.keys()))
        return disco_quotes[quote_key]
    
    if __name__ == "__main__":
        random_quote = get_disco_quotes()
        print(random_quote)

