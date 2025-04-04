import random
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("introduzca el tamaño de su contraseña aqui por favor:"))
contraseña = ""
for i in range(longitud):
    contraseña += random.choice(caracteres)
print("Tu increible y mejorada contraseña es:", contraseña)


