#A Weather Outfit Picker that asks about temperature, rain, wind, and puddles, then uses if and if-else statements to decide what outfit, umbrella, windbreaker, and shoes to wear, all while keeping every block properly indented.

print("---Weather Outfit Picker---")
temperature = float(input("Enter the temperature in degrees:"))
is_raining = input("Is it raining? (yes/no)")
is_windy = input("Is it windy? (yes/no):")
have_puddles = input("Are there any puddles outside? (yes/no):")

outfit = ""
umbrella = ""
windbreaker = ""
shoes = ""

if temperature >= 80:
    outfit = "You should wear T-shirt and shorts"
elif temperature >= 60:
    outfit = "You should wear a light not too heavy sweatshirt and jeans/sweatpants"
else:
    outfit = "You should wear a heavy and thick jacket/longsleeves and warm pants"

if is_windy == "yes":
    windbreaker = "You should wear a windbreaker jacket"
else:
    if temperature < 60:
        windbreaker = "You should wear a heavy winter coats"
    else:
        windbreaker = "No extra windbreaker jackets are needed..."


if have_puddles == "yes" or is_raining == "yes":
    shoes = "You should wear waterproof rain boots"
else:
    if temperature >=80:
        shoes = "You should wear confortable sandles or crocs"
    else:
        shoes = "You should wear regular sneakers"    

print("")
print("Your Recommendation:")
print(f"-outfit: {outfit}")
print(f"-Jacket/Windbreaker: {windbreaker}")
print(f"-Umbrella status: {umbrella}")
print(f"-shoes {shoes}")