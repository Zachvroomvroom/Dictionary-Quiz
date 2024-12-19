quiz = {'Rudolph the Red Nosed Reindeer':'Gene Autry','All I Want For Christmas':'Mariah Carey','Feliz Navidad':'Jose Feliciano','Chestnuts Roasting on an Open Fire':'Nat King Cole','Mr. Thayer':'Mr. Thayer'}

for i in quiz:
    print(i)
    answer = input("Who made that song? ")
    if answer == quiz[i]:
        print("Correct! It was",quiz[i])
    else:
        print("Wrong. The answer was",quiz[i])