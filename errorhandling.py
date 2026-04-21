info = 0
error = 0
warning = 0
try:
    with open("log_level.log", "r") as file:
        for line in file:
            if "INFO" in line:
                info += 1
            elif "ERROR" in line:
             error += 1
            elif "WARNING" in line:
                warning += 1


        print("INFO:", info)
        print("ERROR:", error)
        print("WARNING:", warning)

except FileNotFoundError:
    print("PLEASE PROVIDE VALID FILE ")
