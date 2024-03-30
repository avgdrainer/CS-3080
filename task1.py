import requests, bs4, openpyxl, random

def main():

    entries = scrape_website()
    sheet = setup_excel(entries)
    random_word = get_random_word(sheet, len(entries))
    #print("the words is " + random_word + " (will be hidden to users, just for screenshot purposes)")

    attempts = 5
    guessed_word = False
    progress = ["_" for x in range(len(random_word))]
   

    print("number of remaining attempts: %d" % (attempts))
    print(" ".join(progress))

    while attempts != 0 and guessed_word == False:

        guess = input("\033[Kenter a guess: ")

        if (validate_guess(guess)):
            attempts = update_scoreboard(guess, attempts, random_word, progress)
        else:
            print('\033[F' + '\r\033[K' + "invalid attempt. ", end = "")
        
        if "".join(progress) == random_word:
            guessed_word = True

    final_message(attempts, guessed_word)

def scrape_website():

    res = requests.get('https://www.ef.edu/english-resources/english-vocabulary/top-1000-words/')

    res.raise_for_status()

    bs4_object = bs4.BeautifulSoup(res.text, 'html.parser')
    words = bs4_object.select('div[property="content:encoded"] p')[1].getText()
    entries = words.split()

    return entries
 
def setup_excel(entries):

    wb = openpyxl.Workbook()
    sheet = wb.active

    for x in range(0, len(entries)):
        sheet['A' + str(x + 1)] = entries[x]

    wb.save(r'C:\Users\Riley\Desktop\skool\comp sci cuhh\python class (CS 3080)\task 1\words.xlsx')

    return sheet

def get_random_word(sheet, length):
    
    random_word = sheet['A' + str(random.randint(1, length))].value
    return random_word

def validate_guess(guess):

    if len(guess) != 1:
        return False
    elif (not guess.isalpha()):
        return False
    else:
        return True


def update_scoreboard(guess, attempts, random_word, progress):
    
    if guess in random_word:
        for x in range(len(random_word)):
            if random_word[x] == guess:
                progress[x] = guess
    else:
        attempts -= 1
        
    print('\033[F' + '\033[F' + '\033[F' + '\r\033[K' + "Number of remaining attempts: " + str(attempts))
    print(" ".join(progress))

    return attempts

def final_message(attempts, guessed_word):

    if (attempts == 0 or guessed_word == False):
        print("\033[KYou lost!")
    else:
        print("\033[KYou won!")

             
main()