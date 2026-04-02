import math 
def title(): #Cool title!
    print("""
  __  __       _   _        _____ _                _         _               _   
 |  \/  |     | | | |      / ____| |              | |       | |             | |  
 | \  / | __ _| |_| |__   | |    | |__   ___  __ _| |_   ___| |__   ___  ___| |_ 
 | |\/| |/ _` | __| '_ \  | |    | '_ \ / _ \/ _` | __| / __| '_ \ / _ \/ _ \ __|
 | |  | | (_| | |_| | | | | |____| | | |  __/ (_| | |_  \__ \ | | |  __/  __/ |_ 
 |_|  |_|\__,_|\__|_| |_|  \_____|_| |_|\___|\__,_|\__| |___/_| |_|\___|\___|\__| """)
    print("")

def main():                                          
    play = "y"                                      
    title()                                          
    while play in ("y","Y"):
        print("""
   +--------------------------------------------------------------+
        [1]   Substitution encryption (Any Number)
        [2]   Substitution decryption (Any Number)
        [3]   Hill Cipher encryption
        [4]   Hill Cipher decryption
        [5]   Prime number checks
        [6]   Linear Congruential Generator Random Number Sequence
        [7]   UPC Bar Code check digit calculator")
        [8]   EAN-13 Bar Code check digit calculator")
        [9]   ISBN check digit calculator")
        [10]  Affine cipher encryption")
        [11]  Affine cipher decryption")
        [12]  RSA cipher encryption")
        [13]  RSA cipher decryption")
   +--------------------------------------------------------------+
              """)  
        choice = int(input("Enter an option "))      
        match choice:
            case 1:
                encrypt()
            case 2:
                decrypt()
            case 3:
                encrypt_Hill()
            case 4:
                decrypt_Hill()
            case 5:
                prime()       
            case 6:
                LCG()
            case 7:
                Barcode(1)
            case 8:
                Barcode(2)
            case 9:
                Barcode(3)
            case 10:
                affine_encode()
            case 11:
                affine_decrypt()
            case 12:
                RSA_encode()
            case 13:
                RSA_decrypt()
        play=input("Play again Y/N ")

def encrypt():
    key = int(input("Please enter the amount to Substitute Cesar is 3 and Rot-13 is 13 "))
    message = get_word("Encrypt")
    Cypher_word = []
    for ch in message:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shifted = (ord(ch) - base + key) % 26
            S_letter = chr(base + shifted)
        elif ch.isdigit():
            shifted = (int(ch) + key) % 10
            S_letter = str(shifted)
        else:
            S_letter = ch
        Cypher_word.append(S_letter)
    New_Word = "".join(Cypher_word)
    print(New_Word)

def decrypt():
    key = int(input("Please enter the amount to Substitute Cesar is 3 and Rot-13 is 13 "))
    message = get_word("Decrypt")
    Cypher_word = []
    for ch in message:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shifted = (ord(ch) - base - key) % 26
            S_letter = chr(base + shifted)
        elif ch.isdigit():
            shifted = (int(ch) - key) % 10
            S_letter = str(shifted)
        else:
            S_letter = ch
        Cypher_word.append(S_letter)
    New_Word = "".join(Cypher_word)
    print(New_Word)

def get_word(Word):
    word = input(f"Enter the phrase you want to {Word} ")
    return word                                         

def Check_prime(num):
    if num <=1:
        return False 
    for loop in range(2,int(math.sqrt(num))+1):
        if num % loop ==0:
            return False
    return True

def prime():
    loop = int(input("How many numbers would you like to check? "))
    for x in range(loop):
        Pnum = int(input("Please enter a number to check "))
        if Check_prime(Pnum):
            print(f"{Pnum} is a prime number")
        else:
            print(f"{Pnum} is not a prime number")
    
def LCG(): #test string x=0 c=1 a=2 m=5
    print("Linear Congruential Generator (LCG) Random Number Sequence")
    print("(a * x + c) % m")
    x = int(input("Enter the initial value (x): "))
    a = int(input("Enter the multiplier (a): "))
    c = int(input("Enter the increment (c): "))
    m = int(input("Enter the modulus (m): "))
    seen = set() #Holy based imagine having an easy way to make an unordered unique list built in without effort!!!!!
    current = (a * x + c) % m
    count = 0
    print(f"X{count} = {x}")
    while current not in seen:
        count += 1
        seen.add(current)
        print(f"X{count} = {current} = (a * x +c) % m")
        current = (a * current + c) % m
    print(f"The program ran {count} times before repeating")

def Barcode(Key):
    N1 = int(input("Please enter N1 "))
    N2 = int(input("Please enter N2 "))
    N3 = int(input("Please enter N3 "))
    N4 = int(input("Please enter N4 "))
    N5 = int(input("Please enter N5 "))
    N6 = int(input("Please enter N6 "))
    N7 = int(input("Please enter N7 "))
    N8 = int(input("Please enter N8 "))
    N9 = int(input("Please enter N9 "))
    if Key == 1:
        N10 = int(input("Please enter N10 "))
        N11 = int(input("Please enter N11 "))
        N12 = -(3*N1 + N2 + 3*N3 + N4 + 3*N5 + N6+ 3*N7 + N8+ 3*N9 + N10+ 3*N11) % 10
        print(f"{N12} = -(3 x {N1} + {N2} + 3 x {N3} + {N4} + 3 x {N5} + {N6} + 3 x {N7} + {N8} + 3 x {N9} + {N10} + 3 x {N11}) mod 10")
        print(f"Check digit N12 = {N12}")
        print("The last digit should be the check digit")
    elif Key == 2:
        N10 = int(input("Please enter N10 "))
        N11 = int(input("Please enter N11 "))
        N12 = int(input("Please enter N12 "))
        N13 = -(N1 + 3*N2 + N3 + 3*N4 + N5 + 3*N6+ N7 + 3*N8+ N9 + 3*N10+ N11 + 3*N12) % 10
        print(f"{N13} = -({N1} + 3 x {N2} + {N3} + 3 x {N4} + {N5} + 3 x {N6}+ {N7} + 3 x {N8}+ {N9} + 3 x {N10}+ {N11} + 3 x {N12}) mod 10")
        print(f"Check digit N13 = {N13}")
        print("The last digit should be the check digit")
    elif Key == 3:
        N10 = (N1 + 2*N2 + 3*N3 + 4*N4+ 5*N5 +6*N6+ 7*N7+ 8*N8+ 9*N9) % 11
        print("N10 = (N1 + 2*N2 + 3*N3 + 4*N4+ 5*N5 +6*N6+ 7*N7+ 8*N8+ 9*N9) mod 11")
        print(f"Check digit N10 = {N10}")

def encrypt_Hill():
    check = "0"
    Correct = "N"
    while Correct !="Y":
        a = int(input("Enter matrix Pos A "))
        b = int(input("Enter matrix Pos B "))
        c = int(input("Enter matrix Pos C "))
        d = int(input("Enter matrix Pos D "))
        print(f"""
            +--------------------+
            | A = {a}   B = {b}  |
            |                    |
            | C = {c}   D = {d}  |
            +--------------------+
        """)
        Correct = input("Is the correct?")
    while not check.isalpha():
        p1 = input("Enter the first letter ")
        check = p1
    p1 = alpha_pos(p1)
    check = "0"
    while not check.isalpha():
        p2 = input("Enter the Second letter ")
        check = p2
    p2 = alpha_pos(p2)
    c1 = (a*p1 + b*p2) % 26
    c2 = (c*p1 + d*p2) % 26
    print(f"Initial values {p1} , {p2}")
    print(f"New Values {c1} , {c2}")

def decrypt_Hill():
    check = "0"
    Correct = "N"
    while Correct !="Y":
        a = int(input("Enter matrix Pos A "))
        b = int(input("Enter matrix Pos B "))
        c = int(input("Enter matrix Pos C "))
        d = int(input("Enter matrix Pos D "))
        print(f"""
            +--------------------+
            | A = {a}   B = {b}  |
            |                    |
            | C = {c}   D = {d}  |
            +--------------------+
        """)
        Correct = input("Is the correct? ").upper()
    det = (a*d - b*c) %26
    print(det)
    print("""
       a  | ā mod 26
       1  | 1
       3  | 9
       5  | 21
       7  | 15
       9  | 3
       11 | 19
       15 | 7
       17 | 23
       19 | 11
       21 | 5
       23 | 17
       25 | 25
    """)
    inv_det = int(input("enter the inverse of det from the list")) #i think i need some sort of like modulo for loop to actuly work this out but fuck that
    b = -b
    c = -c
    print(f"""
            +--------------------+
            | D = {d}  -B = {b}  |
            |                    |
            | -C = {c}  A = {a}  |
            +--------------------+
    """)
    while not check.isalpha():
        p1 = input("Enter the first letter ")
        check = p1
    p1 = alpha_pos(p1)
    check = "0"
    while not check.isalpha():
        p2 = input("Enter the Second letter ")
        check = p2
    p2 = alpha_pos(p2)
    c1 = (inv_det * (d*p1 + b*p2)) % 26
    c2 = (inv_det * (c*p1 + a*p2))% 26
    print(f"Initial values {p1} , {p2}")
    print(f"New Values {c1} , {c2}")

def alpha_pos(letter):
    if 'a' <= letter <= 'z':
        return ord(letter) - ord('a') 
    elif 'A' <= letter <= 'Z':
        return ord(letter) - ord('A') 

def divCheck(): #code this later nerd!
    print("Check if a number is devisable without a remainder")
    print("to check divisibility take the last digit of the number double it then subtract it from the remainder")
    print("Do this until you have a 2 digit number then check if it is a multiple of the divisor")
    print("E.g. (Div 7) 1946 becomes 194 - 12 (2x6) = 182 then 182 becomes 18 - 4 which becomes 12 which is not a multiple of 7 ")
    print("""
Better method if looking for divisability by 9
          a number is divisible by 9 if the sum of its digits is divisible by 9 (E.g. 2133 = 9 witch is dv 9)
""")
    print(""" 
And another method for div 11 
 find the difference between the sum of the digits in the odd positions and the sum of the digits in the even positions. 
If this difference is zero or a multiple of 11, then the number is divisible by 11. 
          
E.g. 1,234,567 
odd numbers from the right added = 7+5+3+1 = 16 
Even from the right = 6+4+2 = 12
16-12 = 4 which is not divisible by 11
so the number is not divisible by 11
""")

def primeFact():
    print("The process of spiting a number by its divisible until you end up with prime numbers for example below")
    print("""
                                            72
                                           /  \
                                          2   36
                                              / \
                                             2   18
""")
    print("""
Start  dividing with the smallest prime we can
we keep going until we end up with a prime we can no longer divide
all of the primes, multiplied together are the prime factorisation
""")
    print("to go greatist common divisor with large numbers just prime factorise both then compare common numbers")
    print("""E.g. 48 = 2x2x2x2x3
          180 = 2x2x3x3x5 
          so the GCD is 2, 2, 3""")
    

def affine_encode(): #tested wih hello 
    print("""
       a  | ā mod 26
       1  | 1
       3  | 9
       5  | 21
       7  | 15
       9  | 3
       11 | 19
       15 | 7
       17 | 23
       19 | 11
       21 | 5
       23 | 17
       25 | 25
    """)
    p = get_word("Encrypt")
    a = int(input("[A] enter a value that had a inverse a from the above list "))
    b = int(input("[B] Enter any value from 0-25 "))
    Cypher_word = []
    for ch in p:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            temp =ord(ch) - base
            shifted = (a * temp + b) % 26 + base
            S_letter = chr(shifted)
            print(f" ({a} X {temp} + {b}) % 26 = {S_letter}")
        else:
            S_letter = ch
        Cypher_word.append(S_letter)
    New_Word = "".join(Cypher_word)
    print(New_Word)

def affine_decrypt():
    print("""
       a  | ā mod 26
       1  | 1
       3  | 9
       5  | 21
       7  | 15
       9  | 3
       11 | 19
       15 | 7
       17 | 23
       19 | 11
       21 | 5
       23 | 17
       25 | 25
    """)
    p = get_word("Decrypt")
    a = int(input("[A] enter the inverse value of A from the encryption "))
    b = int(input("[B] Enter the second key value from the encrypted phrase "))
    Cypher_word = []
    for ch in p:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            temp = ord(ch) - base
            shifted = a * (temp - b)  % 26 + base
            S_letter = chr(shifted)
            print(f" ({a} X {temp} + {b}) % 26 = {S_letter}")
        else:
            S_letter = ch
        Cypher_word.append(S_letter)
    New_Word = "".join(Cypher_word)
    print(New_Word)

def RSA_encode():  #Tested with turn n= 15 e=7 worked correctly
    print("RSA Encoding")
    p = get_word("Encrypt")
    n = int(input("Enter a value for N "))
    e = int(input("Enter a value for E"))
    Cypher_word = []
    for ch in p:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            temp = ord(ch) - base
            shifted = temp**e % n + base
            S_letter = chr(shifted)
            print(f"{shifted - base} = {temp}**{e} % {n} ")
            print("new character = {S_letter}")
        else:
            S_letter = ch
        Cypher_word.append(S_letter)
    New_Word = "".join(Cypher_word)
    print(New_Word)

'''
right im going crazy 
p = large prime 
q = large prime 
n = p x q 
r = (p-1) X (q-1)
e = 3 , 5 , 17 , 65537 E.g. usuly prime numbers
d = e pow -1 mod (r)
5d = 1 (mod12)
'''

def RSA_decrypt():
    print("RSA Decoding")
    print("For 2 digit encryption 2 decrypted chunks make 1 letter ")
    print("For 3 digit encryption each chunk makes a letter ")
    Len = int(input("How many Chunks do you wish to decode "))
    n = int(input("Enter a value for N "))
    k = int(input("Enter a value for K "))
    for x in range(Len):
        c = int(input(f"Enter chunk number "))
        p1 = c**k % n
        print("") 
        print(f"{p1} = {c}**{k} % {n}")
        print("")


#Computer Randomization is deterministic 

#Substitution Ciphers are vunrable to pattern recognition and brute forcing  

"""
Chunking 
19201713
as 2s 19 20 17 13 
as 3s 192 017 13_ pad
"""

main()
