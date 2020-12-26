#1.	ln  (1+x) function can be expanded  using Taylor series and the expanded series is given below.
 
Now write a single program to perform the following tasks:
  a.	Take the value of x and iteration (number of terms) number n and return the approximated value of  ln(1+x).							
  b.	Plot the ln  (1+x)  function for the interval -1<x<=1 with step size 0.1 using the built-in log (x) function.												
  c.	In the same plot (one plot for 1(a) and 1(b)) show five approximated functions for the same interval using different number of terms (1, 3, 5, 20, 50).			
  d.	Draw another plot showing the relative approx. error for each iteration while determining the value of  ln(1.5) upto 50 terms.			

#2.	In a chemical engineering process, water vapor (H2O) is heated to sufficiently high temperatures that a significant portion of the water dissociates, or splits apart, to form oxygen (O2) and hydrogen (H2):

      H2O←→ H2 + 1/2 O2

  If it is assumed that this is the only reaction involved, the mole fraction  x of H2O that dissociates can be represented by

  K = x/(1-x) *√(2pt/(2+x))

  Where K is the reaction’s equilibrium constant and p_t is the total pressure of the mixture. If p_t = 3 atm and K = 0.05, determine the value of x that satisfies given equation.
  Write a single program which does the following:
    •	Uses graphical model to estimate the value.			
    •	Uses Secant method and False Position method to estimate the value for εs=0.5%. Report the number of iterations for each  method  while achieving the expected result.

    Secant Method and False Position method should be implemented as separate functions following the prototype given below:
    •	Secant method (function , 1st initial guess, 2nd initial guess, expected relative approximation error, max iteration)

    •	False Position method (function , lower bound of the bracket, upper bound of the bracket, expected relative approximation error, max  iteration)
    Please note that following the prototypes is mandatory. 
