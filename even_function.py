"""import numpy as np
import matplotlib.pyplot as plt

# Define the range of x values
x = np.linspace(-5, 5, 100)

# Define the even function f(x) = x^2
def even_function(x):
    return x**2

# Compute the corresponding y values
y = even_function(x)

# Plot the graph
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='f(x) = x^2', color='blue')
plt.title('Graph of an Even Function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)  # Add x-axis
plt.axvline(0, color='black', linewidth=0.5)  # Add y-axis
plt.legend()
plt.show()"""
import numpy as np
import matplotlib.pyplot as plt

# Define the range of x values
x = np.linspace(-5, 5, 100)

# Define the odd function f(x) = x^3
def odd_function(x):
    return x**3

# Compute the corresponding y values
y = odd_function(x)

# Plot the graph
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='f(x) = x^3', color='red')
plt.title('Graph of an Odd Function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)  # Add x-axis
plt.axvline(0, color='black', linewidth=0.5)  # Add y-axis
plt.legend()
plt.show()
