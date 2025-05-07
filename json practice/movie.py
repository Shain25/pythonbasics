import json

add_movie={'id':"", 'title':"", 'director':"", 'rating':"", 'genres': ["",""]}
free_id=1

# 1. Load the movie.json
with open("movie.json", "r") as file:
    data = json.load(file)

# 2. Allow the user to search for a movie by title
search_input=input("Search a movie title: ").lower()

for movie in data["movies"]:
    free_id+=1
    if movie["title"].lower()==search_input:
        print(f"The movie details is: {movie}")
        break
else:
        print("Movie not found")

# 3. Add a new movie
add_movie["id"]=free_id
add_movie["title"]=input("Add new movie title: ")
for movie in data["movies"]:
    if add_movie["title"].lower()==movie["title"]:
        add_movie["title"]=input("This movie already exists, Add new movie title: ")
add_movie["director"]=input("Add new movie director: ")
add_movie["rating"]=int(input("Add new movie rating: "))
add_movie["genres"]=input("Add new movie genres (seperate by commas): ").split(",")
data["movies"].append(add_movie)

# 4. Update rating
data["movies"][0]["rating"]=7

# 5. Save all changes
json.dump(data, open("movie.json", "w"), indent=4)