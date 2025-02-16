import re
def checkers():
    # Main function to handle password input and validation loop.
    while True:
        password=input("Please enter the password (or type 'exit' to quit):-")
        if password.lower() == "exit":
            print("Thank you ! For Signing in")
            break
        result=checker_password(password)
        print(result)

def checker_password(password):
    '''
      Criteria (in order of priority):
    1. Minimum length of 8 characters
    2. At least one digit
    3. At least one uppercase letter
    4. At least one lowercase letter
    5. At least one special character from specified set
    '''
    if len(password)<8:
        return "Low: password must be at least 8 characters long."
    elif not any(char.isdigit() for char in password):
        return "Low: password must include at least one number."
    elif not any(char.isupper() for char in password):
        return "Average: password must include at least one uppercase letter."
    elif not any(char.islower() for char in password):
        return "Low: password must include at least one  lowercase letter."
    elif not re.search(r"[!, @, $, %, ^, &, *, +, #,<,>]",password):
        return "Average: Add special characters [!, @, $, %, ^, &, *, +, #,<,>] to make your password."
    else:
        return "Strong: You password is secure"

if __name__=="__main__":
    checkers()
 