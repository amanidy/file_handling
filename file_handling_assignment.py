try:

 with open ("my_file.txt", "w") as file:
    file.write("Welcome to McDorcis services.\n")
    file.write("The answer to life's ultimate question is 42 .\n")
    file.write( "The total sum of 2 and 3 is " + str(2+3) + ".\n")


 with open("my_file.txt", "a") as file:
    file.write("McDorcis services are opened 24/7.\n")
    file.write("We offer web development services at affordable price.\n")
    file.write("Visit our site for more info.\n")



 with open("my_file.txt", "r") as file:
    contents = file.read()

 print(contents)

except FileNotFoundError:
   print("The file you are looking for does not exist")
except PermissionError:
   print("You do not have the required permission to access this file")
except Exception as e:
   print(f"An unexpected error occurred :{e}")
   
