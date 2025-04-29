try:
 file=open("sample.txt","r")
 reading_file=file.readlines()
 print("Line1:",reading_file[0].strip())
 print("Line2:",reading_file[1].strip())

 file.close()
except:
 print("Error: there is no file available with this name ")