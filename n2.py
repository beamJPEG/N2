program = []

while True:
    # Get user input
    user_input = input("> ")
    
    # Check for keywords and execute corresponding actions
    if user_input.startswith("print "):
        # Extract text from user input
        text = user_input.split("print ", 1)[1]
        # Print text to console
        print(text)
        
    elif user_input == "end":
        # End program
        break
    
    elif user_input == "start":
        # Start program
        program = []
        
    elif user_input.startswith("var "):
        # Extract variable name and value from user input
        _, var_name, var_value = user_input.split()
        # Add variable to program
        program.append((var_name, var_value))
        
    elif user_input.endswith(" run"):
        # Extract variable name from user input
        var_name = user_input.split(" run")[0]
        # Find variable in program
        for var in program:
            if var[0] == var_name:
                # Set variable value to True
                program.remove(var)
                program.append((var_name, True))
                break
                
    elif user_input.endswith(" unrun"):
        # Extract variable name from user input
        var_name = user_input.split(" unrun")[0]
        # Find variable in program
        for var in program:
            if var[0] == var_name:
                # Set variable value to False
                program.remove(var)
                program.append((var_name, False))
                break
                
    elif user_input.startswith("if "):
        # Extract variable name and value from user input
        _, var_name, var_value = user_input.split()
        # Find variable in program
        for var in program:
            if var[0] == var_name:
                # Execute if statement if variable value is True
                if var[1]:
                    print(f"If statement is true: {var_value}")
                # Otherwise, execute else statement
                else:
                    print("Else statement")
                break
                
    else:
        print("Invalid input")
    
    elif user_input.startswith("repeat "):
        # Extract number from user input
        n = int(user_input.split("repeat ", 1)[1])
        # Repeat loop n times
        for i in range(n):
            print(f"Loop {i+1}")
                
    elif user_input.startswith("print formatte "):
        # Extract formatted text from user input
        text = user_input.split("print formatte ", 1)[1]
        # Print formatted text to console
        print(text.format())
        
    else:
        print("Invalid input")


