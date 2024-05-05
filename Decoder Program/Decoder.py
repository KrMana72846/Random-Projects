def decode(message_file):
    thisdict = {}
    file = open(message_file,"r")
    lines = len(file.readlines())
    file = open(message_file,"r")
    
    # Sets up dictonary
    for i in range(1,lines):
        thisdict.update({i: ""})
    
    # Sort lines from text file in to a dictionary in numerical order
    for i in range(lines):
        newchar = ""
        x = 1
        while x == 1:
            char = file.read(1)
            #Check is numbers have been read
            if char == " ":
                x = 0
                # writes word associated with number in dictionary from textfile
                write = file.readline()
                thisdict[int(newchar)] = write[:-1]
            #Continues reading the rest of the number
            else:
                newchar = newchar + char
    

    #Creates Pyramid and decodes message corresponding to the numbers at the end of each pyramid line 
    newline = 1 # The new line of the pyramid
    checkline = 1 #Checks if pyramid line is at an endpoint
    sentence = ""
    for i in range(1,lines+1):
        # Checks if a pyramid line has reach its endpoint
        if checkline == newline:
            newline += 1
            checkline = 1
            sentence = sentence + thisdict[i] + " "
        else:
            checkline += 1
    return sentence
            
        
    
        
        
        







def main():
    file = "coding_qual_input.txt"
    print(decode(file))

    
main()