"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Dajana Kočková
email: d.kockova@gmail.com
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

registered_users = {
    "bob" : "123",
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123"
}
separator = "-"*40
user_name = input("Enter your username:")
password = input("Enter your password:")

if user_name in registered_users: 

    if registered_users[user_name] == password:
        print(separator)
        print(f"Welcome to the app, {user_name.capitalize()}", "We have 3 texts to be analyzed.", sep="\n")
        print(separator) 
        entered_number = (input("Enter a number btw. 1 and 3 to select:"))

        if not entered_number.isnumeric():
            print("You need to write a number from 1 to 3!")

        elif int(entered_number) in range(1,4):
            print(separator)
            chosen_text = TEXTS[int(entered_number)-1]
            print("There are", len(chosen_text.split()), "words in the selected text.")

            number_of_titles = int()
            for title in chosen_text.split():
                 if title.istitle():
                      number_of_titles += 1
            print("There are", number_of_titles, "titlecase words.")

            number_of_uppers = int()
            for uppers in chosen_text.split():
                 if uppers.isupper():
                    number_of_uppers += 1
            print("There are", number_of_uppers, "uppercase words.")

            number_of_lowers = int()
            for lowers in chosen_text.split():
                 if lowers.islower():
                    number_of_lowers += 1
            print("There are", number_of_lowers, "lowercase words.")

            count_of_numbers = int()
            numbers_list = list()
            for numbers in chosen_text.split():
                if numbers.isdigit():
                    count_of_numbers += 1
                    numbers_list.append(int(numbers))
            print("There are", count_of_numbers, "numeric strings.")
            print("The sum of all the numbers", sum(numbers_list))

            print(separator)
            print("LEN", " OCCURRENCES ", "NR.", sep="|")
            print(separator)

            length_of_words = list()

            for word in chosen_text.split():
                word = word.replace(".","").replace(",","")
                length_of_words.append(len(word))

            for number_of_letters in set(length_of_words):
                occurrences = length_of_words.count(number_of_letters)
                print(f"{number_of_letters}|{"*"*occurrences} |{occurrences}")

        else:
            print("You need to write a number from 1 to 3!")
       
    else:
        print("Ooops! Wrong password, terminating the program..")

else:
    print("username:", user_name)
    print("password:", password)
    print("unregistered user, terminating the program..")



    
