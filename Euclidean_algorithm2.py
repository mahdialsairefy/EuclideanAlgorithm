class EuclideanGCD:
    ## Function to calculate euclidean greatest common divisior of any 2 integers
    ## Takes as input 2 integers a and b and returns an integer which is their gcd
    def euclidean_gcd(a,b):
    
        # First get absolute value of each integer
        if b < 0:
            b = -b
        if a < 0:   
            a = -a
        
        # Now check if any of the 2 integers is 0, then set the other as gcd
        if a == 0:
            return b
        elif b == 0:
            return a
        
        # Now use the Euclidean algorithm: loop over  to find the gcd 
        #We will iterate the process until B becomes 0, Divide a by b and keep the remainder
        while b != 0:
            remainder = a - (a // b) * b
            a = b
            b = remainder
            
        return a
if __name__ == "__main__":
    # main app to test the functionality of our code
    ## Take input integers and print their gcd
    
    print("Euclidean Algorithm")
    try:
        a= int(input("Enter the first integer: "))
        b=int(input("Enter the second integer: "))
        gcd_value = EuclideanGCD.euclidean_gcd(a, b)
        print("GCD of", a, "and", b, "is", gcd_value, ".")    
    # make sure a and b are integers, else return error message
    except ValueError:
        
        print("Invalid input: You should enter valid integers.")
    
        
        