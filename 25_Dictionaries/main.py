capitals = {
            "USA": "Washington, D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"
            }

# print(dir(capitals));
# print(help(capitals));
# print(capitals.get("USA"));
# print(capitals.get("Japan"));
# print(capitals.get("India"));

# if capitals.get("Japan"):
#     print("That Capital Exist")
# else:
#     print("That Capital Does Not Exist")

# if capitals.get("Russia"):
#     print("That Capital Exist")
# else:
#     print("That Capital Does Not Exist")
    
# capitals.update({"Germany": "Berlin"});
# capitals.update({"USA": "Detroit"});
# capitals.pop("China");
# capitals.popitem();
# capitals.clear();

# keys = capitals.keys()

# print(capitals)

# print(keys)
# for key in keys:
#     print(key)

# values = capitals.values()

# print(values)

# for value in values:
#     print(value)
    
items = capitals.items()

# print(items)

# for item in items:
#     print(item)
for key, value in items:
    print(f"{key} : {value}")