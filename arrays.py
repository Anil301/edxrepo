names=['Anil','Ananya','Shashi','Ravikanth']
message1=f"Good Evening {names[-2].title()}"
message2=f"Good Evening {names[-1].title()}"
message3=f"Good Evening {names[0].title()}"
message4=f"Good Evening {names[1].title()}"
print(names)
names[2]='Sushma'
print(names)
names.append('Shashi')
print(names)
names.insert(2,'Shashi')
print(names)
del names[3]
print(names)