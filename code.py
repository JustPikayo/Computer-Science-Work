'''
Build a program that asks for a PIN code and uses a while loop to allow only three attempts to enter it correctly.
Set a correct PIN (e.g., 4321) in the code.

Ask the user to enter the PIN.

Use a while loop to keep asking until the correct PIN is entered or 3 attempts have been made.

After 3 failed attempts, print "Too many failed attempts. Locked out."

If the user enters the correct PIN, print
'''

correct_pin = "4321"
attempts = 0
max_attempts = 3

while attempts < max_attempts:  
    entered_pin = input("Please enter your PIN: ")
    if entered_pin == correct_pin:
        print("Access granted.")
        break  
    else:
        print("Incorrect PIN. Please try again.")
        attempts += 1  

if attempts == max_attempts:
    print("Too many failed attempts. Locked out.")
