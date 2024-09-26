import math

def bhaskara(a, b, c):
  """Calculates the roots of a quadratic equation using Bhaskara's formula.

  Args:
    a: The coefficient of the quadratic term.
    b: The coefficient of the linear term.
    c: The constant term.

  Returns:
    A list of roots.
  """

  delta = b**2 - 4*a*c

  if delta < 0:
    return []  # No real roots
  elif delta == 0:
    return [-b / (2*a)]  # One real root
  else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    return [x1, x2]  # Two real roots

# Get coefficients from the user
a = float(input("Insira o coeficiente a: "))
b = float(input("Insira o coeficiente b: "))
c = float(input("Insira o coeficiente c: "))

# Calculate and print the roots
roots = bhaskara(a, b, c)
if len(roots) == 0:
  print("A equação não tem raízes reais")
elif len(roots) == 1:
  print("A equação tem uma raiz real:", roots[0])
else:
  print("A equação tem duas raízes reais:", roots)