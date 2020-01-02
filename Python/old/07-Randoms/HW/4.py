# Gadzlevs userList-is redaqtirebis sashualebas
# Lets you edit entries in userList

DATA_NAME = "saxeli"
DATA_AGE = "asaki"
DATA_NATIONALITY = "warmoshoba"


userList = [{DATA_NAME : "dato", DATA_AGE: 25, DATA_NATIONALITY: "Georgia"}, 
			{DATA_NAME: "gio", DATA_AGE: 45, DATA_NATIONALITY: "Georgia"}]

while (True):
	print(userList)
	index = input("Sheiyvanet romeli user-is redaqtireba gsurt (nebismieri simbolo rom gatishot): ")
	
	if (not index.isnumeric() ):
		break

	index = int(index)
	if (index < len(userList)):
		newName = input("Sheiyvanet axali {} {}-stvis: "
			.format(DATA_NAME, userList[index][DATA_NAME]))
		newAge = input("Sheiyvanet axali {}: ".format(DATA_AGE))
		newNat = input("Sheiyvanet axali {}: ".format(DATA_NATIONALITY))
		userList[index] = {DATA_NAME: newName, DATA_AGE: newAge, DATA_NATIONALITY: newNat}
	else:
		print("Araswori indeqsia")
