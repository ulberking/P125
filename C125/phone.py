from phonenumbers import geocoder
import phonenumbers
from phonenumbers import carrier

serviceprovider = phonenumbers.parse('+15147651749')
print(carrier.name_for_number(serviceprovider,'en'))

chnum=phonenumbers.parse('+15147651749','CH')
print(geocoder.description_for_number(chnum,'en'))