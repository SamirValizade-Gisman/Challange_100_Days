import random
Map=1
Number=2
print(f"Please choose you side: (Map or Number)  ") #Qəpiyin tərəfini seç
chose=input('Please write you side: ') #Qəpiyin üzünü seç
random_side=random.randint(1,2)
if random_side==Map and chose=="Map":
    print("That side is Map, and you win")
elif random_side==Number and chose=="Number":
    print("That side is Number and you win")
else:
    print("You lost!")