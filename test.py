name="praveen kumar ragoju"

print(len(name))
print(name.split())
print(name.upper())
print(name.casefold())
print(name.center(5))

first_name="praveen"
middle_name="kumar"
last_name="ragoju"

full_name=first_name + middle_name + last_name
print(full_name.upper())

inital_text="I will try"
new_text=inital_text.replace("try","do it")
print(new_text)

text = "   praveen kumar ragoju   "
print(text)
stripped_text = text.strip()
print("Stripped text:", stripped_text)


import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")