### q5notes 
amount=int(input("enter the amount:"))
denominations=[2000,500,200,100,50,20,10]
print("minimum number of notes")
for note in denominations:
    if amount>= note:
        count=amount//note
        print(f' {note}*{count}')


