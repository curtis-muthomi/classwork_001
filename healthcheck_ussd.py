print("WELCOME TO HEALTHCHECK USSD SERVICE")
print("_____________________________________")
print("SYMPTOM OPTIONS:")
print("1. fever,headache and fatigue")
print("2. cough,sore throat and chestpain")
print("3. stomach pain,diarrhea and nausea")
print("4.joint pain,skin rash and red eyes")

symptomchoice=(input("SELECT YOUR SYMPTOMS (1-4)"))

if symptomchoice=="3":
    print("\n possible diseases:")
    print("foodpoisoning")
    print("gastroenteritis")
    print("cholera")

elif symptomchoice=="4":
    print("\n possible diseases:")
    print("dengue fever")
    print("chikungunya")
    print("allergic reaction")

elif symptomchoice=="1":
    print("\n possible diseases:")
    print("malaria")
    print("typhoid")
    print("influenza")

elif symptomchoice=="2":
    print("\n possible disease:")
    print("common cold")
    print("COVID-19")
    print("pneumonia")

else:
    print("INVALID INPUT!")