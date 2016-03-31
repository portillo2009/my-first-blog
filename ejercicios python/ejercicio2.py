# !/user/bin/pyton
# -*-codigo:utf -8-*-
# Paso  nombres
nombres = [
	["Erudice Granados", "sandragranados@gimail.com"]
	["Pablo Duarte", "pablocyne@yahoo.com"]
	["Juan Lago", "juan123@gimail.com"]
	["Margarita Carderon", "caudmaga2708@gimail.com"]
	["Erica Morales", "eymor@yahoo.com"]
	]
# paso 2 print nombres
nombres.sort()

for nom in nombres:
	print (nom)

# paso 3 lista con solo el nombre
print ()
print("Cantidad de Letras")
print()

for dato in nombres:
	caracteres = len(dato[0])-1
	print(dato[0] + " " + str(caracteres))

# paso 4 Dominios
print()
print("Dominios")
print ()

for nom in nombres:
	donminio = nom [1].split("@")[1]
	print dominios	
