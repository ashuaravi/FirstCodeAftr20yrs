print ("hello friend" )
name1 = input("what's your name?\n")
print ("hello , "+name1)
print("Hey "+name1+", do you want to chat about today's weather?")
answer = input("Type yes or no\n")
               
while (answer=="yes"):
       print ("I'm your code, Hows weather today?)")
       weather= input("Was it Hailing/rainy/snowy/sunny? type one of the options\n")
       if weather == "Hailing" :
              print ("RUN!!,Hide under your umbrella")
       elif  weather =="rainy":
              print ("Its alright,Just wipe your nose and walk home")
       elif weather == "snowy":
              print ("Stretch your arms and catch the snowflakes, each of them might have different patterns")
       elif weather == "sunny":
              print ("Cmon!! Get the sunscreen ,Remove your jacket, Drink all your water!!") 
       else: 
              print ("Cheating!!!,that was not in my options,try again")
       answer = input("do you want to try again \n Type yes or no \n")
print("byebye!!")