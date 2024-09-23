"""
Name: Dictionary.py
Author: Gavin Hashemi
Date: 2024-09-23 1:50 p.m.
Description:

 Dictionary is key/value.
 Duplicated is not allowed.
 The key is case-sensitive which means , when we want to extract the value of it, it cannot be case different.
 For extraction, the key must be existed; otherwise, it will fail
 We can use [] to extract the value , or use get() method to extract the value. However, get() does not fail the application if the key does not exist. it returns 'None'.
 get() method for non exist value, it can have 'default value'
"""


customer = {
    "name": "Gavin Gargamel",
    "age" : 5000,
    "is_verified": True
}

print(customer["name"])

customer["name"] = "George Wild"
print(customer["name"])

#add new key value
customer["birthday"] = "Jan 1, 3000 BC"
print(customer["birthday"])


print(customer.get("age"))
print(customer.get("not_exist_value"))
print(customer.get("not_exist_value", "default value exist")) # default value with get()