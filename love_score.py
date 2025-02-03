def calculate_love_score():
    # Get names as input
    name1 = input("Enter the first person's name: ").lower()
    name2 = input("Enter the second person's name: ").lower()

    
    combined_names = name1 + name2

    
    true_count = sum(combined_names.count(letter) for letter in "true")

   
    love_count = sum(combined_names.count(letter) for letter in "love")

 
    love_score = int(f"{true_count}{love_count}")

  
    print(f"Your love score is {love_score} 💖")


calculate_love_score()
