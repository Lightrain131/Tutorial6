# Student number: 1234567
def f(x):  # Define the function
    return -(x**2) + 3*x - 2

print(" # # # f(x) = -x^2 + 3x + 2 from a=1 to b=2 # # # ")
x = 1
sum = 0
while x < 2.01:  # Create a while loop
    print("When x =", x, "=> f(x) =", f(x))
    sum += f(x)  # Calculate middle sum by using loops.
    x += 0.1  # Increment 0.1

print(" # # # Example of Trapezium Rule Values # # # ")
first = f(1)  # Variable first
last = f(2)  # Variable last
sum -= first  # Middle sum do not include f(1) and f(2)
sum -= last

h = 0.1
T = (h/2)*(first + 2*sum + last)  # Calculate integration
ET = 1/6                          # Exact integration
E = ((ET - T)*100) / ET           # Calculate %Error
print("First Height:", first)
print("Last Height:", last)
print("Middle Sum:", sum)
print("Integration is approximately", T)
print("True value of integration is 1/6")
print("Therefore the error is", E, "%")

quit()


