#https://www.youtube.com/watch?v=VEfEzl9mgt0&ab_channel=NerdCademy

import secrets  #genera números aleatorios seguros
import string #operaciones comunes de strings
import random




lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
special = string.punctuation
allChars = lower + upper + digits + special
password = ""




pwLen = int(input("Longitud mínima: "))
minUpper = int(input("¿Cuántas mayúsculas quieres? "))
minLower = int(input("¿Cuántas minúsculas quieres? "))
minDigits = int(input("¿Cuántos números? "))
minSpec = int(input("¿Cuántos carácteres especiales?: "))




#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
for i in range(minUpper):
    password += "".join(random.choice(secrets.choice(upper))) #random.choice retorna un elemento aleatorio de una secuencia seq no vacía


for i in range(minLower):
    password += "".join(random.choice(secrets.choice(lower)))


for i in range(minDigits):
    password += "".join(random.choice(secrets.choice(digits)))


for i in range(minSpec):
    password += "".join(random.choice(secrets.choice(special)))

#we take the remainig of the password length and choose randonly characters
remaining = pwLen - minLower - minUpper - minDigits - minSpec


for i in range(remaining):
    password += "".join(random.choice(secrets.choice(allChars)))


password = list(password)
random.shuffle(password) #Mezcla la secuencia
print("".join(password)) #The join() method takes all items in an iterable and joins them into one string
