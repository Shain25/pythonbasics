import json

num=1

#1 Read the books.json file and load the data
with open("books.json", "r") as file:
    data = json.load(file)

#2 Print each book's title and average rating.
for book in data["books"]:
    avgra= sum(book["rating"]) / len(book["rating"])
    print(f"Title: {book['title']}, Rating: {avgra:.2f}")
    num+=1

#3+4 Create a new book, check if a book with the same title already exists
if book["title"].lower() != "the great gatsby":
    data["books"].append({"id":num, "title": "The Great Gatsby", "rating": [2, 4, 5]})
    json.dump(data, open("books.json", "w"), indent=4)

else:
    [print("The book already exists in the list.")]