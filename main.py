#CyHelp Starter Code
cyberBirthYr = 1970

#Greets user
print("Hello! I'm CyHelp.")
name = input("Whats your name?\n")
print("Nice to meet you "+name+"!");

#Recounts start of Cybersecurity

todayYr = input("What year is it?\n")
timePassed = int(todayYr) - cyberBirthYr
print("Wow! That means it has been "+ str(timePassed) + " years since Cybersecurity began!")

print("The field of Cybersecurity started in the 1970s when more and more information started being stored on computer systems and networks!")

input("Press enter to continue.\n")

#Describes Cybersecurity
print("Cybersecurity refers to the practices that people use to protect computer systems and networks from cyber attacks.")

print("\nThese people can be governments/nations, individuals, companies, community organizations, and hackers.\n")


#Introduces CIA Triad
print("The CIA Triad is the model used to discuss cybersecurity. CIA stands for confidentiality, integrity, and availability")

print("Would you like to learn about the CIA Triad?")
ans = input("Type yes or no");


#Explains pillars of CIA Triad
while ans.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n (a) confidentiality \n (b) integrity \n (c) availability \n (d) none")
  
  topic = input()
  
  if topic.lower() == "a":
    print("Confidentiality makes sure data is private.")
  elif topic.lower() == "b":
    print("Integrity makes sure data has not been tampered with and can be trusted.")
  elif topic.lower() == "c":
    print("Availability makes sure authorized people can access the data.")
  elif topic.lower() == "d":
    ans = "no"
  else:
    print("Sorry, I didnt quite catch that")
  

#Chatbot ends conversation
print("\nThanks for chatting with me, and I hope you learned something new!")