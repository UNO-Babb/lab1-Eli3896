#FirstProgram.py
#Name:eli burklund
#Date: 8/28
#Assignment:

def main():
  print("First Program")
  #Say hello
  print("hello")
  #Ask for the user's name
  answer=input("what is your name?")
  #Use the user's name in the program.
  print("thank you "+ answer)
  #Ask the user for their age.
  age = input("what is your age?")
  #Tell the user what year they were born in.
  age = int(age)
  birthyear= 2024-age
  print(birthyear)
  #Assume that they have not had their birthday yet this year.


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
