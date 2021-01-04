user_choice=input("HEADS OR TAILS? Type 'H' for HEADS or 'T' for TAILS :").upper()      # taking input irrespective of case

import random
python_choice=random.choice(['H','T'])

if user_choice==python_choice:
    print("You won the Toss")
elif user_choice!=python_choice:
    print("You loss the Toss")