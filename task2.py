file=open("output.txt","r+")
user_input=input(" Enter the data  you would like to add to File ")
file.writelines( user_input )
print("data entered successfully "
      )
userinput2=input(" Enter the data  you would like to append ")

file.writelines( "\n" +userinput2)
print("data appended successfully "
      )
file.close()
file=open("output.txt","r+")
PrintData=file.read()
print(PrintData)

file.close()