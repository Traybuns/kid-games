"""
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "A piece of code that does the same thing over and over again.",
    "Method": "A function that is part of a class.",
    "Module": "A file containing Python code that you can import into your project.",
    "Class": "A custom defined data type that can be used to create objects.",
    "Feature": "An additional component of a program."
}



programming_dictionary["Loop"] = "A piece of code that does the same thing over and over again."
#empty_dictionary = {}
#programming_dictionary = empty_dictionary
programming_dictionary["Bug"] = "An insect, an annoying insect"
print(programming_dictionary["Bug"])
#print(programming_dictionary)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

    student_scores = {
        'Harry': 88,
        'Ron': 78,
        'Hermione': 95,
        'Draco': 75,
        'Neville': 60
    }

    # Creating a new dictionary for student grades
    student_grades = {}

    # Assigning grades based on scores
    student_grades["Harry"] = "Exceeds Expectation"
    student_grades["Ron"] = "Acceptable"
    student_grades["Hermione"] = "Outstanding"
    student_grades["Draco"] = "Acceptable"
    student_grades["Neville"] = "Fail"

    print(student_grades)


capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Spain": "Madrid"
}

#travel_log = {
   # "France": ["Paris", "Lille", "Dijon"],
  #  "Germany": ["Berlin", "Hamburg", "Stuttgart"]
#}

#print(travel_log["France"][1])

nested_list =["A", "B", ["C", "D"]]
print(nested_list[2][1])

travel_log = {
    "France":{
        "num_times_visited": 3,
        "cities_visited": ["Paris, Lille, Dijon"]
    },
    "Germany": {
        "num_times_visited": 2,
                "cities_visited": ["Berlin", "Hamburg", "Stuttgart"]
},
}

print(travel_log["Germany"]["cities_visited"][2])

"""

# Dictionary to store bids
bids = {}


def find_highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        if bids[bidder] > highest_bid:
            highest_bid = bids[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of N{highest_bid}")


continue_bidding = True

while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: N"))
    bids[name] = price

    Should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if Should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)

    print("\n" * 100)  

