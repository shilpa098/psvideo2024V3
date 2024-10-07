import re
#followed by a 4 letter word
str = 'an example word:deaf!!'
match = re.search(r'word:\w\w\w\w', str)
# If-statement after search() tests if it succeeded
if match:
  print ('found', match.group()) ## 'found word:cat'
else:
  print ('did not find')

# . - A period. Matches any single character except newline character.
print(re.search(r'Co.k.e', 'Cookie').group())

# + - Checks for one or more characters to its left.
re.search(r'Co+kie', 'Cooookie').group()

# Checks for any occurrence of a or o or both in the given sequence
re.search(r'Ca*o*kie', 'Caokie').group()

email_address = "Please contact us at: support@test.com, xyz@test.com"

# 'addresses' is a list that stores all the possible match
addresses = re.findall(r'[\w\.-]+@[\w\.-]+', email_address)
for address in addresses:
  print(address)

str = "Customer number: 232454, Date: February 12, 2011"
items = re.findall("[0-9]+.*: .*", str)

print(items)

str = "The destination is Paris!"
mo = re.search(r"destination.*(London|Paris|Zurich|"
               r"Strasbourg)", str)
if mo: print(mo.group())

regex = r"[A-z]{1,2}[0-9R][0-9A-Z]?[0-9][ABD-HJLNP-UW-Z]{2}"
address = "BBC News Centre, London, W12 7RJ"
compiled_re = re.compile(regex)
res = compiled_re.search(address)
print(res)

metamorphoses = "OF bodies chang'd to various forms, I sing: Ye Gods, from whom these miracles did spring, Inspire my numbers with coelestial heat;"

print(re.split("\W+", metamorphoses))

print("Changing the month....")
str = " Task to complete ELK Stack by 23 july 2018."
# res = re.sub("[0-9]{4}","2020", str)
res = re.sub("(june|july|august|september)", "December", str)
print(res)

# to find 3 letter word
str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
if match:
  print('found', match.group())  ## 'found word:cat'
else:
  print('did not find')

str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', str)
if match:
  print(match.group())  ## 'b@google'

import re

example_codes = ["SW1A 0AA",  # House of Commons
                 "SW1A 1AA",  # Buckingham Palace
                 "SW1A 2AA",  # Downing Street
                 "BX3 2BB",  # Barclays Bank
                 "DH98 1BT",  # British Telecom
                 "N1 9GU",  # Guardian Newspaper
                 "E98 1TT",  # The Times
                 "TIM E22",  # a fake postcode
                 "A B1 A22",  # not a valid postcode
                 "EC2N 2DB",  # Deutsche Bank
                 "SE9 2UG",  # University of Greenwhich
                 "N1 0UY",  # Islington, London
                 "EC1V 8DS",  # Clerkenwell, London
                 "WC1X 9DT",  # WC1X 9DT
                 "B42 1LG",  # Birmingham
                 "B28 9AD",  # Birmingham
                 "W12 7RJ",  # London, BBC News Centre
                 "BBC 007"  # a fake postcode
                 ]

pc_re = r"[A-z]{1,2}[0-9R][0-9A-Z]? [0-9][ABD-HJLNP-UW-Z]{2}"

for postcode in example_codes:
  r = re.search(pc_re, postcode)
  if r:
    print(postcode + " matched!")
  else:
    print(postcode + " is not a valid postcode!")

s = "Sun Oct 14 13:47:03 CEST 2012"

expr = r"\b(?P<hours>\d\d):(?P<minutes>\d\d):" \
       r"(?P<seconds>\d\d)\b"
x = re.search(expr, s)
print(x.group('hours'))
print(x.group('minutes'))


re_pattern=r"[A-Z]{5,25}"

userName=input("Enter Name")

result=re.search(re_pattern,userName)
if(result):
    print("Match Found")
else:
    print("Match not found")


re_pattern = r"(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{4,})"
password = input("Enter Password")
result = re.search(re_pattern, password)
if (result):
  print("Match Found")
else:
  print("Match not found")