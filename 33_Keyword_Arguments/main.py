def hello(greeting, title, first_name, last_name):
    print(f"{greeting} {title}{first_name} {last_name}")
    
# hello("Hello", "Mr.", "Ashwani", "Kumar")
# hello("Mr.", "Hello", "Kumar", "Ashwani")
# hello(greeting="Hello", title="Mr.", first_name="Ashwani", last_name="Kumar")
# hello(title="Mr.", greeting="Hello", first_name="Ashwani", last_name="Kumar")

def getPhone(country, area, first, last):
    return f"Phone Number: +{country}-{area}-{first}-{last}"

phoneNum = getPhone(country=91, area=42, first=377, last=492)

print(phoneNum)