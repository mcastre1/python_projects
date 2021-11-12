from decimal import getcontext, Decimal

class N_Pi:
    """Class used to get the n_digit of pi
        Author: Miguel Castrejon"""

    n = 0   # Keeps track of the requested n.

    def __init__(self, n):
        """ Initializes and makes sure a correct type value is used."""
        try:
            self.n = int(n) # Tries to convert a given value into an integer.

        except Exception as ex: # Breaks and prompts the user if fails.
            print("Please enter an integer.")

    def calculate(self):
        """ Method used to calculat the requested n-digit of pi."""
        getcontext().prec = self.n + 1 # Used to tell python we need more decimal points.

        n_digit = 0 # Keeps track of the final float value of pi to the n-th digit.

        for i in range(self.n): # David Bailey, Peter Borwein, and Simon Plouffe formula for  finding the n-th digit of pi.
            n_digit += Decimal((1/(16**i)) * ((4/((8*i)+1)) - (2/((8*i)+4)) - (1/((8*i)+5)) - (1/((8*i)+6))))

        return n_digit # Returns the final value.

if __name__ == "__main__":
    n_pi = N_Pi(100)
    print(n_pi.calculate())