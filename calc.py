def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
   formated_f_name = f_name.title()
   formated_l_name = l_name.title()
   return f":Result {formated_f_name} {formated_l_name}"

print(format_name("Traybuns", "Gobum"))



def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True 
            else:
                return False  
        else:
            return True  #
    else:
        return False  


print(is_leap(2400))
print(is_leap(1989))  
print(is_leap(2000))  
print(is_leap(2100))  
