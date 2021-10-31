def DataIntegrityCheck(Indicat0r):
    # dataIntegrityCheck checks if all lists have the same lenght to prevent serious bugs in other modules
    # If this one fails it means that the Indicator module is not providing enough Datapoints in any of the Lists
    # Lists must have the same lengths to pass this Check
    dataIntegrityCheck = []
    
    for element in Indicat0r:
        if type(element) is list:
            length = len(element)
            dataIntegrityCheck.append(length)

    # Uisng all()method
    result = all(element == dataIntegrityCheck[0] for element in dataIntegrityCheck)
    if result == True:
        print("Passed dataIntegrityCheck at ", Indicat0r[3], dataIntegrityCheck) 
    elif result == False:
        print("Failed dataIntegrityCheck at ", Indicat0r[3], dataIntegrityCheck)

    # return result