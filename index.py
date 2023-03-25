print("In the Program, I will explore my capacities with Functions in Python and my English")

#I'm declaring my variables and requesting that a user press the datas
nome = input("Press your Name.. ")
idade = int (input("Press your Age.. "))
profession = input("Press your Profession..")
country = input("Press your country..")
city = input("Press your city..")
work = input("Press your work..")
lenguage = input("Press your lenguages..")

#Initial walk
print("..")
print("Talk with Dev..")
print("..")

#First function for the user name
print("Hello my friend! What's your name? ")
def meu_Nome(nome):
    print("Hi my name is", nome)

#call the name Function
meu_Nome(nome)
print("..")

#second function for the age of user with validation age, minor or older
print("Hello ",nome," How old you are? ")
def verifica_Idade(idade):
    if (idade <= 17):
        print("I'm ",idade, "years old!")
        print("You are a minor! LOL")
    else: 
        print("I'm ",idade, "years old!")
        print("Yeahh! You are older!")

#to call the function age
verifica_Idade(idade)
print("..")

#function for the profession
print("What's your profession? ")
def minha_Profissao(profession):
    print("I'm a ", profession)
    print("You are a ", profession, "?")
    print("Woww, It's so cool! I'm a",profession,"too!")

#to call a profission function
minha_Profissao(profession)
print("..")

#function for the country user
print("Where country are you from?")
def meu_pais(country):
    print("I'm from ", country)
    print("Are you from ",country,"?")
    print("How, It's very nice!")

#to call the country function
meu_pais(country)
print("..")

#function for city
print("Where do you live?")
def minha_Cidade(city):
    print("I live in ", city)
    print(city,"looks like good! ")

#Call the city function
minha_Cidade(city)
print("..")

print("..")
print("My name is Charlie, I'm nineteen too and I live in Washington, D.C.")
print("..")
#function for the work
print("Where do you Work?")
def meu_Trabalho(work):
    print("I work at", work)
    print("Wow! Wow! Wait a minute.. Do you work at", work, "??")
    print("Yess LIMAO")
    print("Dawn broo! It's very very amazing!")

#call work function
meu_Trabalho(work)
print("..")

#function for the lenguages work
print("Whats programming lenguages do you work?")
def minhas_Linguagens(lenguage):
    print("I work with ",lenguage)
    print("Wow ", lenguage, " is very cool. I like this!")

#Call lenguage function
minhas_Linguagens(lenguage)
