import phonenumbers 
from phonenumbers import geocoder

phone_number1 = phonenumbers.parse(input("Enter the phone number: "))
print(geocoder.description_for_number(phone_number1, 'en'))