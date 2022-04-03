num1=int(input('enter first number:'))
num2=int(input('enter second number:'))
op=input('enter operator:')

if(op== '+'):
    print('The addition is :',num1+num2)
elif op=='-':
    print('The substraction is :',num1-num2)
elif op=='/':
    print('The division is :',abs(num1/num2))  
elif op=='*':
    print('The multiplication is :',num1*num2)
else:
    print('wrong operator.')          