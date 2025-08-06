def readFile():
    """
    function: In this function, the process of file open, file read, reads each line,
              splits the line by commas and file close is implemented.
              in this function, read lines is used which converts the elements of the text file to lists
    """
    file=open("coursework.txt","r") #open file in read mode
    a=file.readlines() #readlines method converts the elements from text file into a list
    nl=[]
    for each in a:     #for each loop (for each is every line that exist in a)
        newLine=each.replace("\n","").split(",")
        """newline is a new list where \n is replaced with empty character, split is giving
        identity to every components on the basis of comma""" 
        nl.append(newLine) #putting all of the small list into a new list
    file.close()    #closing the opened file
    return nl
