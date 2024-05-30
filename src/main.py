def main():
    print("Hello and welcom to the Adventure Game!")
    print("Are you ready to take an adventure in this cave?")
    answer = input("Yes or No: ")
    if answer.lower() == "yes":
        pass
    elif answer.lower() == "no":
        return 0
    else:
        print("Please enter a valid input.")
    
main()
    

