print("What type of cover does the book have? ")
book_cover = input()

if book_cover == "soft":
    print("Is the book perfect_bound?")
    perfect_bound = input()
    if perfect_bound == "yes":
        print("Soft cover, perfect_bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")

elif book_cover == "hard":
    print("Books with hard covers can be more expensive")

else:
    print("book_cover is not popular")