import time

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

print("~~~~~~~~~~~~~~~WELCOME~~~~~~~~~~~~~~~\n")
time.sleep(0.5)
print("e---> Encode \nd---> Decode \ns---> Shift\nq---> Quit the program  \n")


def loop():
    while True:
        continue1=input("\nDo you want to continue{Y/N}: ")
        if continue1=='y' or continue1=='Y':
            main()                                                                          #calling the main function
        
        elif continue1=='n' or continue1=='N':
            quit()                                                                             #quit from the programme
        else:
            print("\t!!!Invalid decision!!!","\n\tCheck the decisions again and enter the correct letter.")
            continue                                                                         #going to start of the while loop again


def main():                                                                                  #function to ask the user for a decision
    decision=input("Enter your decision: ")
    if decision=='e' or decision=='E':                                                      #checks the decision is encoding or not 
        encode_message=input("Enter the message to encode: ")                                
        while True:
            try:
                shift_value1=int(input("Enter the shift value: "))
                if shift_value1 in range(1,26):
                    encode(encode_message,shift_value1)
                    break                                                                   #go to the function to perform the encoding
                else:
                     time.sleep(0.3)
                     print("\t!!!Shift value should be between 1-25!!!","\n\tCheck the value again and reenter.")          
                     continue                                                                                         #going to the start of the loop to prompt for shift value again
            except ValueError:
                time.sleep(0.3)
                print("\t!!!Shift value should be a numerical character!!!","\n\tCheck the value again and reenter.")
                continue                                                                                              #going to the start of the loop to prompt for shift value again   
    elif decision=='d' or decision=='D':
        decode_message=input("Enter the message to decode: ")                       #checks the decision is decoding or not
        while True:
            try:
                shift_value2=int(input("Enter the shift value: "))
                if shift_value2 in range(1,26):
                    decode(decode_message,shift_value2)                                  
                    break                                                             #go to the function to perform the decoding
                else: 
                     time.sleep(0.3)
                     print("\t!!!Shift value should be between 1-25!!!","\n\tCheck the value again and reenter.")
                     continue                                                                                              #going to the start of the loop to prompt for shift value again
            except ValueError:
                time.sleep(0.3)
                print("\t!!!Shift value should be a numerical character!!!","\n\tCheck the value again and reenter.")
                continue                                                                                                   #going to the start of the loop to prompt for shift value again                      
    elif decision=='q' or decision=='Q':
        quit()                                            #quit the program
    elif decision=='s' or decision=='S':
        encoded_string=input("Enter the encoded string: ")
        hint=input("Enter the hint: ")
 
        
    else:
        time.sleep(0.3)
        print("\t!!!Invalid decision!!!","\n\tCheck the decisions again and enter the correct letter.")
        

main()        #calling the main function
loop()        #calling the loop
            


