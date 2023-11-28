import scraper_v2 as scrape
import os

os.system("cls")

search_str = [
    "Ashurbanipal",
    "Charlton_Heston",
    "Baruch_Spinoza",
    "Charles_Martel",
    "Pythagoras",
    "John_Dewey",
    "Isaac_Newton",
    "Harriet_Tubman",
    "Emperor_Yingzong_of_Song",
    "Vitruvius",
    "Abraham_Lincoln",
    "Plato",
    "Henry_Ford",
    "Ludwig_van_Beethoven",
    "Michelangelo",
    "Galileo_Galilei",
    "Nelson_Mandela",
    "Albert_Einstein",
    "Martin_Luther_King_Jr",
    "Orville_Wright",
    "Thomas_Edison",
    "Nikola_Tesla",
    "Mother_Teresa",
    "Mahatma_Gandhi",
    "Leonardo_da_Vinci",
    "Christopher_Columbus",
    "Confucius",
    "Joseph_Stalin",
    "Paul_of_Tarsus",
    "Gautama_Buddha",
    "St._Augustine",
    "Alexander_the_Great",
    "Genghis_Khan",
    "Martin_Luther",
    "Zarathustra",
]


# search_str = ["Christopher_Columbus"]

for name in search_str:
    (born, died) = scrape.run_scraper(name)

    print("search_str = {0}".format(name))
    print("born->", born.year, born.adbc, born.month, born.day)
    print("died->", died.year, died.adbc, died.month, died.day)
    print("\n")
