# string formating was done like this is python before python 3.6
string="Hey my name is {0} and I am from {1}"
name="Priyojit"
country="India"
print(string.format(name,country))

# now you can use f-string
print(f"Hey my name is {name} and I am from {country}")

# for showing float values to exact 2 decimal places
price=49.099999999
print(f"the price is only {price:.2f} dollars")

# to retian the raw f-string use double curly braces
print(f"Hey my name is {{name}} and I am from {{country}}")