names = ["dato", "GIORGI", "mari", "IRAKLI", "Nino", "n"]

# Using list comprehension
print([n[0].upper() + n[1:].lower() for n in names if len(n) > 1])

# Using map and filter :^)
print(list(
		map(lambda n: n[0].upper() + n[1:].lower(), 
			filter(lambda n: len(n) > 1, names)))
)