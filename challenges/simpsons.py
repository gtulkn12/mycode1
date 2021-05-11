challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]
trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]
nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

#Challenge -  My eyes! The goggles do nothing!
print(f"My {challenge[2][1]}! The {challenge[2][0]} do {challenge[3]}")

#Trial -  My eyes! The goggles do nothing!
print(f"My {trial[2]['goggles']}! The {trial[2]['eyes']} do {trial[3]}")

#Nightmare -  My eyes! The goggles do nothing!
eyes= nightmare[0]["user"]["name"]["first"]
goggles= nightmare[0]["kumquat"]
nothing= nightmare[0]["d"]
print(f"My {eyes}! The {goggles} do {nothing}!")
