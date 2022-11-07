def get_ratings(file_name):
    """Restaurant rating lister."""

    ratings = {}
    file = open(file_name)

    for line in file:
        line = line.split(":")
        ratings[line[0]]=line[1].strip()

    user_restaurant = input("What restaurant would you like to rate? ")
    user_rating = input("On a scale from 1 to 5, what do you rate this restaurant? ")
    ratings[user_restaurant]=user_rating

    ratings=sorted(ratings.items(), key=lambda item: item[1], reverse=True)

    for ratings in ratings:
        print (f"{ratings[0]} is rated at {ratings[1]}.")





results= get_ratings('scores.txt')

