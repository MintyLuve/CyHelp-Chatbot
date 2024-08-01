#Breach Bot Starter Code
breachYr = 2019

#Greets user
print("Hello! I'm Breach Bot.")
name = input("Whats your name?\n")
print("\nNice to meet you "+name+"!");

#Recounts start of Cybersecurity

todayYr = input("What year is it?\n")
timePassed = int(todayYr) - breachYr
print("Wow! That means it has been "+ str(timePassed) + " years since the Facebook data breach!")


#Introduces breach
print("\nWould you like to learn about the 2019 Facebook data breach?")
ans = input("Type yes or no\n");

#Explains breach
while ans.lower() == "yes":
  print("\nWhat would you like to learn more about? Enter the lowercase letter of the following options: \n (a) Breach Details \n (b) Organization's Response \n (c) I would like to hear your reflection")
  
  topic = input()
  
  if topic.lower() == "a":
    print("\nPersonal information from 533 million Facebook users in 106 countries got leaked. They took phone numbers, full names, locations, some email addresses, and other details from user profiles. The data was posted to an amateur hacking forum.")
  elif topic.lower() == "b":
    print("\nFacebook said that *malicious actors* had scraped the data by exploiting a vulnerability in a now-defunct feature on the platform that allowed users to find each other by phone number. They didn't tell invdividually who got hacked, and just put out a public notice")
  elif topic.lower() == "c":
    ans = "no"
  else:
    print("Sorry, I didnt quite catch that")


#Introduces my take
print("\nI'm excited to share my perspective with you. Are you ready to hear my take?")
ans = input("Type yes or no\n");

#Shares my take
while ans.lower() == "yes":
  print("\nWhat would you like to learn more about? Enter the lowercase letter of the following options: \n (a) Relation to CIA Triad \n (b) My Reaction \n (c) My Advice \n (d) None")

  topic = input()

  if topic.lower() == "a":
    print("\nThis data breach connects to integrety because Facebook didn't let the users know if it was them who got leaked.")
  elif topic.lower() == "b":
    print("\nI disagree with the organization's response because I think that Facebook should have let the individuals know if their information was leaked or not.")
  elif topic.lower() == "c":
    print("\nI would convince victims to take action by updating their passwords to be more secure, and to not share passwords across accounts.")
  elif topic.lower() == "d":
    ans = "no"
  else:
    print("Sorry, I didnt quite catch that")


#Chatbot ends conversation
print("\nThanks for chatting with me, and I hope you learned something new!")