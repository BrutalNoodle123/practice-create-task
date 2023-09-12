restaurants = ["In N Out", "Mcdonalds", "Chick Fil A", "Jack in the Box", "Taco Bell"]

new_res = input("What Restaurant would you like to rank into your list?")

def rank_restaurant(new_res, restaurant):

    for i in range(len(restaurants)):

        rank = input("Do you like A) " + new_res + "more or B) "+ restaurant(i) + "more? A/B")

        if rank == "A":
            restaurants.inset(i, new_res)
            break
        elif rank == "B":
            continue

    if new_res not in restaurants:
        restaurant.append(new_res)
    
    return restaurants 

print("YOur new ranking of restaurants is ", rank_restaurant(new_res, restaurants))

    