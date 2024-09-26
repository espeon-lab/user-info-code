#Why must variable names be lower case?

#Name 
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
middle_initial = input("Please enter your middle initial: ")

#Street
street_address = input("Whats your street address?: ")

#City, State Zip Code
city = input("What city are you in: ")
state =input("Which state are you in: ")
zip_code =input("What's your zip code: ")

#Phone number
phone_number =input("What's your phone number: ")

#Email address
email_address =input("What is your email address: ")

print (f"{first_name} {middle_initial} {last_name}")
print (f"{street_address}")
print (f"{city}, {state} {zip_code}")
print (f"{phone_number}")
print (f"{email_address}")
