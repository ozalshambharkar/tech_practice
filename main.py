class firstclass:
    val1 = 0
    val2 = 0
     
    def __init__(self,a,b):
        print('this is constructor')
        self.val1 = a
        self.val2 = b

    def addvalue(self):
        print(f'addition = {self.val1 + self.val2}')


f1 = firstclass(2,3)

f1.addvalue()

print('f1.val1 = ',f1.val1)
print('f1.val2 = ',f1.val2)

f2 = firstclass(9,5)
f2.addvalue