# WELCOME SCREEN
print("------------------------------------------------")
print("           GEO Investments Group")
print("------------------------------------------------")
print("1) Create a New User Account")
print("2) Login (Existing User)")
print("------------------------------------------------")
# importing random module for generating random number
import random
import os

#Get user input for the number option
user_input = input(
  "\nEnter a number option and press ENTER or type 'Q/q' to quit:")


#Account Class
class Account:

  def _init_(self, bus_name_extr):
    self.bus_name_extr = bus_name_extr


#Object of Account class to create 8-digit account number
class Accnum(Account):

  def create_accnum(self, bus_name_extr):
    return str(random.randint(10000000, 99999999)) + '-' + bus_name_extr


#Create new user
if user_input == "1":
  print("\nWelcome to GEO Investments Group!")
  #Get user input for the request parameters
  full_name = input("\nEnter the full name and press ENTER: ")
  address = input("Enter the address and press ENTER: ")
  user_dob = input("Enter the DOB and press ENTER: ")
  bus_name = input("Enter the business name and press ENTER: ")
  bus_incorp_date = input(
    "Enter the business incorporation date and press ENTER: ")
  stake_equity = input(
    "Enter the stakeholder and equity details and press ENTER: ")
  bus_acc_type = input("Enter the Type of business and press ENTER: ")
  # Create account instance to get account number
  accnumAcc = Accnum()
  acc_num = accnumAcc.create_accnum(bus_name[0:2].upper())
  user_name = input("Enter a user name and press ENTER: ")
  user_pwd = input("Enter a user password and press ENTER: ")
  user_pin = input("Enter a 4 digits PIN and press ENTER: ")

  #Create/Over-write the request parameters into the user request file based on user name
  text_file = open("user accounts " + user_name + ".txt", "w")
  text_file.write(user_name)
  text_file.write("\n" + user_pwd)
  text_file.write("\n" + user_pin)
  text_file.write("\n" + full_name)
  text_file.write("\n" + address)
  text_file.write("\n" + user_dob)
  text_file.write("\n" + bus_name)
  text_file.write("\n" + stake_equity)
  text_file.write("\n" + bus_acc_type)
  text_file.write("\n" + acc_num)
  text_file.close()
  print("\nCongratulations " + full_name +
        "! Your new user profile has been created.")

#Existing user Login
elif user_input == "2":
  login_user_name = input("\nEnter your user name and press ENTER: ").strip()
  login_pwd = input("Enter your password and press ENTER: ").strip()
  login_pin = input("Enter your 4 digit PIN and press ENTER: ").strip()
  #verify user login
  try:
    user_file = open("user accounts " + login_user_name + ".txt", "r")
    usr_name = user_file.readline().strip()
    usr_pwd = user_file.readline().strip()
    usr_pin = user_file.readline().strip()
    full_nm = user_file.readline().strip()
    usr_addr = user_file.readline().strip()
    usr_dob = user_file.readline().strip()
    usr_busnm = user_file.readline().strip()
    usr_stake_eq = user_file.readline().strip()
    usr_bus_acc_typ = user_file.readline().strip()
    usr_accnum = user_file.readline().strip()
    user_file.close()

    if usr_pwd != '' and usr_pwd != login_pwd:
      print("\nInvalid User password!")
    elif usr_pin != '' and usr_pin != login_pin:
      print("\nInvalid User PIN!")
    elif ((usr_name != '' and usr_name == login_user_name)
          and (usr_pwd != '' and usr_pwd == login_pwd)
          and (usr_pin != '' and usr_pin == login_pin)):
      print("\nWelcome " + full_nm + "!")

      #Change Settings
      print("\n------------------------------------------------")
      print("a) settings - View Profile")
      print("b) settings - Change User Name")
      print("c) settings - Change User Password")
      print("d) settings - Change User PIN")
      print("e) settings - Deactivate User Account")
      print("------------------------------------------------")
      user_input2 = input(
        "\nEnter a number option and press ENTER or type 'Q/q' to quit:")

      #View user profile
      if user_input2.upper() == "A":
        try:
          text_file2 = open("user accounts " + login_user_name + ".txt", "r")
          print("\n          Viewing Profile of " + full_nm)
          print("================================================")
          contents = open("user accounts " + login_user_name + ".txt", "r")
          usr_name_new = contents.readline().strip()
          usr_pwd_new = contents.readline().strip()
          usr_pin_new = contents.readline().strip()
          full_nm_new = contents.readline().strip()
          usr_addr_new = contents.readline().strip()
          usr_dob_new = contents.readline().strip()
          usr_busnm_new = contents.readline().strip()
          usr_stake_eq_new = contents.readline().strip()
          usr_bus_acc_typ_new = contents.readline().strip()
          usr_accnum_new = contents.readline().strip()
          contents.close()
          print("User Name: ", usr_name_new)
          print("User Password: ", usr_pwd_new)
          print("User PIN: ", usr_pin_new)
          print("Full Name: ", full_nm_new)
          print("Address: ", usr_addr_new)
          print("Business Name: ", usr_busnm_new)
          print("Stakeholder & Equity: ", usr_stake_eq_new)
          print("Business Account type: ", usr_bus_acc_typ_new)
          print("Account Number: ", usr_accnum_new)
        except FileNotFoundError:
          print("\nNo User profile exists!")

  #Change User Name
      elif user_input2.upper() == "B":
        new_usr_nm = input("\nEnter new user name and press ENTER: ")
        #Create new user profile file with the new user name
        text_file3 = open("user accounts " + new_usr_nm + ".txt", "w")
        text_file3.write(new_usr_nm)
        text_file3.write("\n" + usr_pwd)
        text_file3.write("\n" + usr_pin)
        text_file3.write("\n" + full_nm)
        text_file3.write("\n" + usr_addr)
        text_file3.write("\n" + usr_dob)
        text_file3.write("\n" + usr_busnm)
        text_file3.write("\n" + usr_stake_eq)
        text_file3.write("\n" + usr_bus_acc_typ)
        text_file3.write("\n" + usr_accnum)
        text_file3.close()
        #remove old user account as the user changed the user name
        os.remove("user accounts " + login_user_name + ".txt")

  #Change User Password
      elif user_input2.upper() == "C":
        new_usr_pwd = input("\nEnter new password and press ENTER: ")
        #Update user profile file with the new user pwd
        text_file4 = open("user accounts " + usr_name + ".txt", "w")
        text_file4.write(usr_name)
        text_file4.write("\n" + new_usr_pwd)
        text_file4.write("\n" + usr_pin)
        text_file4.write("\n" + full_nm)
        text_file4.write("\n" + usr_addr)
        text_file4.write("\n" + usr_dob)
        text_file4.write("\n" + usr_busnm)
        text_file4.write("\n" + usr_stake_eq)
        text_file4.write("\n" + usr_bus_acc_typ)
        text_file4.write("\n" + usr_accnum)
        text_file4.close()

  #Change User PIN
      elif user_input2.upper() == "D":
        new_usr_pin = input("\nEnter new 4-digit user PIN and press ENTER: ")
        #Update user profile file with the new user pwd
        text_file4 = open("user accounts " + usr_name + ".txt", "w")
        text_file4.write(usr_name)
        text_file4.write("\n" + usr_pwd)
        text_file4.write("\n" + new_usr_pin)
        text_file4.write("\n" + full_nm)
        text_file4.write("\n" + usr_addr)
        text_file4.write("\n" + usr_dob)
        text_file4.write("\n" + usr_busnm)
        text_file4.write("\n" + usr_stake_eq)
        text_file4.write("\n" + usr_bus_acc_typ)
        text_file4.write("\n" + usr_accnum)
        text_file4.close()

  #Deactivate Account
      elif user_input2.upper() == "E":
        print("\nAccount of " + full_nm +
              " deactivated and profile deleted successfully!")
        os.remove("user accounts " + usr_name + ".txt")
  #Quit settings menu
      elif user_input2.upper() == "Q":
        print("\nGood Bye!")
  #Exception
  except FileNotFoundError:
    print("\nInvalid User login!")

#Quit the program
elif user_input.upper() == "Q":
  print("\nGood Bye!")

#Invalid option entered
else:
  print("\nPlease try again with a valid option!")

#Lists of statements
statements = {'Transactions made' : '14','Total Gained' : '9900', 'Total Lost' : '4400'}

#Statements for each month
january = {'Total gained' : '500' , 'Total Lost' : '300' , 'Total transactions' : '2'}  
february = {'Total gained' : '2000' ,'Total Lost' : '200', 'Total Transactions' : '3'}
march = {'Total gained' : '400' , 'Total lost' : '500', 'Total Transactions' : '1'}
april = {'Total gained' : '1000', 'Total lost' : '450', 'Total Transactions' : '4'}
may =  {'Total gained' : '600' , 'Total lost' : '250' , 'Total Transactions' : '2'}
june = {'Total gained' : '700' , 'Total lost' : '300', 'Total Transactions' : '4'}
july = {'Total gained' : '890' , 'Total lost' : '460', 'Total Transactions' : '5'}
august = {'Total gained' : '580', 'Total lost' : '400', 'Total Transactions' : '6'}
september = {'Total gained' : '1000', 'Total lost' : '100', 'Total Transactions' : '2'}
october = {'Total gained' : '1200', 'Total lost' : '610', 'Total Transactions' : '3'} 
november = {'Total gained' : '940', 'Total lost' : '500', 'Total Transactions' : '4'}
december = {'Total gained' : '730', 'Total lost' : '280', 'Total Transactions' : '2'}
#View Statements
print("Press S to view the list of transactions made in account")
print("Press J to view January statements ")
print("Press F to view February statements ")
print("Press M to view March statements ")
print("Press A to view Aril statements ")
print("Press Y to view May statements ")
print('Press U to view June statements')
print('Press L to view July statements')
print('Press G to view August statements')
print('Press T to view September statements')
print('Press O to view October statements')
print('Press N to view November statements')
print('Press D to view December statements')

#Now letting the user view a statement
user_input = input("Enter option here: ")

if user_input == "J":
  print(january)
elif user_input == "F":
  print (february)
elif user_input == "M":
  print(march)
elif user_input == "A":
  print(april)
elif user_input == "Y":
  print(may)
elif user_input == "U":
  print(june)
elif user_input == "L":
  print(july)
elif user_input == "G":
  print(august)
elif user_input == "T":
  print(september)
elif user_input == "O":
  print(october)
elif user_input == "N":
  print(november)
elif user_input == "D":
  print(december)
elif user_input == "S":
  print(statements)
else:
  print("An error has occured due to violation of instructions")

#Now the users have the option to compare that income/outcome with another month. This is optional.
print("Press another key associated with another month if you want to compare that last selected month with another one. /n Press a non-assciated key to skip this.")
user_input = input("Enter what month to compare to: ")

if user_input == "J":
  print(january)
elif user_input == "F":
  print (february)
elif user_input == "M":
  print(march)
elif user_input == "A":
  print(april)
elif user_input == "Y":
  print(may)
elif user_input == "U":
  print(june)
elif user_input == "L":
  print(july)
elif user_input == "G":
  print(august)
elif user_input == "T":
  print(september)
elif user_input == "O":
  print(october)
elif user_input == "N":
  print(november)
elif user_input == "D":
  print(december)
elif user_input == "S":
  print(statements)
else:
  print("You have skipped this step")

#Get quarterly reports
print("Press 1 to get first quarter report")
print("Press 2 to get second quarter report")
print("Press 3 to get third quarter report")
print("Press 4 to get forth quarter report")
user_input = input("Enter option here: ")
if user_input == "1":
  print("Total gained: 2900, Total lost: 1000")
elif user_input == "2":
  print("Total gained: 2300, Total lost: 1000")
elif user_input == "3":
  print("Total gained: 2470, Total lost: 960")
elif user_input == "4":
  print("Total gained: 2870, Total lost: 1390")

#GEO Investment
print("GEO Investment fee: $10 ")
user_input = input("Please press K to pay GEO Investment fee: ")
if user_input == "K":
  print("GEO investment fee succesfully paid")
else:
  print("GEO Investment payment transaction failed")
