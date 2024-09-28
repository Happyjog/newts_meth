print("Enter the degree of the polynomial:")
degree = int(input())
coef_list = []
print("Enter the coefficients for each  term of the polynomial (Include negatives and when there isn't one for the degree, enter 0): ")

for i in range(degree + 1):
    print("Enter the coefficieent for degree ", degree-i, ":")
    coef_list.append(int(input()))

def polyn_maker(d):
    polyn = []
    for i in range(d):
        polyn.append(d-i)
    polyn.append(0)
    return  polyn
def polyn_solver(x, coeff, power):
    value;
    for i in range(coeff):
        value +=  coeff[i] * (x ** power[i])
    return value

print("Your polynomial is: ")
for i in range(degree):
    print(coef_list[i], "x^", polyn_maker(degree)[i],  "+", end = " ")
    if(degree-i == 1):
        print(coef_list[i])




def deriv_taker(p):
    first = p[0]
    del p [0]
    for i  in range(len(p)):
        return p




    
store_x = []
store_y = []

print("Type 1 for Neighborhood mode and 2 for Iteration mode")

mode = input()

print(polyn_maker(6))

if(input == 1):
    print("Type the neighborhood in which the iterations will terminate.")

else:
    print("Type the number of times you want the iterations to run")



x_choice = input()