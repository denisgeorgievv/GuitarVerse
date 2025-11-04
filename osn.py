import random
from komponenti.akordi_info import akordi_info, akordi, popularnost, trudnost, trudnost_prichini, progresii

def menu():
    while True:
        print("\nGUITARVERSE")
        print("-----------")
        print("1. get info about a chord of your choice")
        print("2. you give us the notes, we give you the chord")
        print("3. search chord progressions by the mood you're going for")
        print("4. how popular is your chord?")
        print("5. how difficult is your chord?")
        print("6. guess the chord!")
        print("7. guess the note!")
        print("0. exit")

        izbor = input("\nenter a number: ").strip()

        if izbor == "1":
            akord_info_menu()
        elif izbor == "2":
            nameri_akord_menu()
        elif izbor == "3":
            progresii_menu()
        elif izbor == "4":
            popularnost_menu()
        elif izbor == "5":
            trudnost_menu()
        elif izbor == "6":
            poznai_akorda_menu()
        elif izbor == "7":
            poznai_notata_menu()
        elif izbor == "0":
            print("\nsee you soon!")
            break
        else:
            print("\nsorry, there's no such function.")

def akord_info_menu():
    while True:
        akord = input("\nenter your chord: ").strip().lower()
        ime, noti = akordi_info(akord)

        if ime:
            print(f"\nyour chord: {ime}")
            print("notes:", ", ".join(noti))
        else:
            print("\nsorry, there's no such chord.")

        print("\nwould you like to:\n1. try another chord\n2. return to main menu")
        izbor2 = input("\nenter 1 or 2: ").strip()
        if izbor2 == "1":
            continue
        else:
            break

def nameri_akord_menu():
    while True:
        noti_input = input("\nenter your notes separated by spaces: ").upper().split()

        found = False
        for akord, (ime, noti) in akordi.items():
            if sorted(noti_input) == sorted(noti):
                print(f"\nthis is {ime} ({', '.join(noti)})")
                found = True
        if not found:
            print("\nsorry, there's no such chord with those notes.")

        print("\nwould you like to:\n1. try another set of notes\n2. return to main menu")
        izbor2 = input("\nenter 1 or 2: ").strip()
        if izbor2 == "1":
            continue
        else:
            break

def progresii_menu():
    while True:
        print("\nchoose a mood from the list below:\n- bright\n- sad\n- suspensful\n- dreamy\n- romantic\n- raw & aggressive\n- dramatic")
        mood = input("\nenter a mood: ").strip().lower()

        if mood in progresii:
            print(f"\nchord progressions for a {mood}-sounding song:")
            for progresiq in progresii[mood]:
                print(" - ".join(progresiq))
        else:
            print("\nsorry, there's no such chord progressions for that mood.")

        print("\nwould you like to:\n1. try another mood\n2. return to main menu")
        izbor2 = input("\nenter 1 or 2: ").strip()
        if izbor2 == "1":
            continue
        else:
            break

def popularnost_menu():
    while True:
        akord = input("\nenter your chord: ").strip().lower()
        if akord in popularnost:
            print(f"\n{akordi[akord][0]} is used in approximately {popularnost[akord]} of guitar songs (estimate).")
        else:
            print("\nsorry, there's no such data for that chord.")

        print("\nwould you like to:\n1. try another chord\n2. return to main menu")
        izbor2 = input("\nenter 1 or 2: ").strip()
        if izbor2 == "1":
            continue
        else:
            break

def trudnost_menu():
    while True:
        akord = input("\nenter your chord: ").strip().lower()
        if akord in trudnost:
            print(f"\n{akordi[akord][0]}'s difficulty is {trudnost[akord]}.")
            print(f"reason: {trudnost_prichini[akord]}")
        else:
            print("\nsorry, there's no such data for that chord.")

        print("\nwould you like to:\n1. try another chord\n2. return to main menu")
        izbor2 = input("\nenter 1 or 2: ").strip()
        if izbor2 == "1":
            continue
        else:
            break

def poznai_akorda_menu():
    tochki = 0
    print("\ntype A, B or C to guess. type 'exit' to stop.")

    while True:
        pravilen = random.choice(list(akordi.items()))
        greshen1 = random.choice(list(akordi.items()))
        greshen2 = random.choice(list(akordi.items()))

        opcii = [pravilen, greshen1, greshen2]
        random.shuffle(opcii)

        noti = pravilen[1][1][:]
        random.shuffle(noti)
        print("\nnotes:", ", ".join(noti))

        print("A.", opcii[0][1][0])
        print("B.", opcii[1][1][0])
        print("C.", opcii[2][1][0])

        otgovor = input("\nyour choice: ").strip().upper()

        if otgovor == "EXIT":
            print(f"\nfinal score: {tochki}")
            break

        if otgovor in ["A", "B", "C"]:
            izbor = opcii[["A", "B", "C"].index(otgovor)]
            if izbor == pravilen:
                tochki += 1
                print(f"\nthat's correct! your socre is {tochki}")
            else:
                print(f"that's wrong, it's actually {pravilen[1][0]}. your final score is {tochki}\n")
                print("would you like to:\n1. try again\n2. return to main menu")
                izbor2 = input("\nenter 1 or 2: ").strip()
                if izbor2 == "1":
                    tochki = 0
                    continue
                else:
                    break
        else:
            print("type only A, B, C or 'exit'.\n")

def poznai_notata_menu():
    struni = ["E", "B", "G", "D", "A", "E"]
    tochki = 0
    print("type the correct note, type 'exit' to stop.")

    while True:
        struna_index = random.randint(0, 5)
        pragche = random.randint(0, 12)

        otvorena_nota = struni[struna_index]
        vsichki_noti = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        startirasht_index = vsichki_noti.index(otvorena_nota)
        nota_index = (startirasht_index + pragche) % 12
        pravilna_nota = vsichki_noti[nota_index]

        print(f"\nstring: {6 - struna_index}, fret: {pragche}")
        otgovor = input("your answer: ").strip().upper()

        if otgovor == "EXIT":
            print(f"\nfinal score: {tochki}")
            break

        if otgovor == pravilna_nota:
            tochki += 1
            print(f"that's correct! your score is {tochki}")
        else:
            print(f"that's wrong, it's actually {pravilna_nota}. your final score is {tochki}\n")
            print("would you like to:\n1. try again\n2. return to main menu")
            izbor2 = input("\nenter 1 or 2: ").strip()
            if izbor2 == "1":
                tochki = 0
                continue
            else:
                break

if __name__ == "__main__":
    menu()