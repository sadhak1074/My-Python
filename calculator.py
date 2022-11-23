N=int(input("Enter your first number"))
op= (input("Enter your operator"))
N2=int(input("Enter your second number"))

if(op == "+"):
    print(N+N2)
elif(op=="-"):
    print(N-N2)
elif(op=="*"):
    print(N*N2)
elif(op=="/"):
    print(N/N2)
else:
    print("Not a valid operator")