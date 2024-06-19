#Import re for regular expressions.
import re

#Make a function to validate phone numbers.
def validate_phone_number(phone_number):
#Regular expression for US phone number in various formats.
    pattern = re.compile(r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')
#If the pattern matches the phone number return true, otherwise false.
    return bool(pattern.match(phone_number))

#Create a function to validate the social security numbers.(SSN)
def validate_ssn(ssn):
#Regular expression for ssn is 123-24-2444
    pattern = re.compile(r'^\d{3}-\d{2}-\d{4}$')
#If pattern matches ssn then return true otherwise false.
    return bool(pattern.match(ssn))

#Create a function to validate the zip codes.
def validate_zip_code(zip_code):
#Regular expression for US zip codes.
    pattern = re.compile(r'^\d{5}(-\d{4})?$')
#If the pattern matches the zip code then return true if not then false.
    return bool(pattern.match(zip_code))

#Create a main function to get input from the user and to display the results.
def main():
    #Get user input for phone number, SSN, and zip code.
    phone_number = input('Enter your phone number: ')
    ssn = input('Enter your social security number: ')
    zip_code = input('Enter your zip code: ')

    #Validate the phone number results.
    if validate_phone_number(phone_number):
        print('The phone number is valid.')
    else:
        print('The phone number is invalid. ')

    #Validate the social security number.
    if validate_ssn(ssn):
        print('The social security number is valid. ')
    else:
        print('The social security number is invalid. ')

    #Validate the zip code and show result.
    if validate_zip_code(zip_code):
        print('The zip code is valid. ')
    else:
        print('The zip code is invalid. ')

#Call the main function to run the program.
if __name__ == '__main__':
    main()