farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


#Function 1
#Write a for loop that returns all the animals from the NE Farm!
for farm in farms[0]["agriculture"]:
    print(farm)



#Function 2
#Ask a user to choose a farm (NE Farm, W Farm, or SE Farm). Return the plants/animals that are raised on that farm
farmnamelist=[]
for farm in farms:
    farmnamelist.append(farm["name"])
farmnames= ', '.join([str(elem) for elem in farmnamelist])
print (farmnames, sep= "\n")

answer= input("Choose a farm:  " )
for farm in farms:
    if answer == farm["name"]:
        print(farm["agriculture"])


#Function 3
# Ask a user to choose a farm (NE Farm, W Farm, or SE Farm)... but only return ANIMALS from that particular farm.




