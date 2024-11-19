name=input("What's your name?")


def choose_practicum():
   practicum=input("Choose practicum.")
   if practicum =="costumes":
      return "costumes"
   elif practicum =="scenery":
      return "scenery"
   elif practicum =="lighting":
      return "lighting"
   elif practicum =="sound":
      return "sound"
   else:
      return "error"

user_choice = choose_practicum() # this variable equals the return value of the function
        
while user_choice == "error":
   print("error. invalid input.") # error message
   user_choice=choose_practicum()
else:
   choice=f'"Congratulations, {name}, you are signed up for {user_choice}!"'
   print(choice)



      
      
        



