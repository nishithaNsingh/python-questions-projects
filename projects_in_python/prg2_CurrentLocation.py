import phonenumbers
from phonenumbers import timezone,geocoder,carrier
number = input("Enter your number with +__: ")
phone = phonenumbers.parse(number)

time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone,"en")
reg = geocoder.description_for_number(phone,"en")
print("Your phone is in", reg)
print("Your current time zone is", time)
print("Your carrier name is", car)

