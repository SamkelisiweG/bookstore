import requests

# Paste the URL of your books resource from mockapi.io, with no trailing slash
API_URL = "https://6af1569a11a6aa866e802448.mockapi.io/books"


def get_books():
    """GET all books and print the JSON and status code."""
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        print("GET all books")
        print(response.json())
        print("Status code:", response.status_code)
        return response.json()
    except requests.exceptions.HTTPError as err:
        print("HTTP error:", err)


def add_book(book):
    """POST a new book. Expect status code 201."""
    try:
        response = requests.post(API_URL, json=book)
        response.raise_for_status()
        print("POST new book")
        print(response.json())
        print("Status code:", response.status_code)
        return response.json()
    except requests.exceptions.HTTPError as err:
        print("HTTP error:", err)


def update_book(book_id, book):
    """PUT: replace the book with the given id."""
    try:
        response = requests.put(f"{API_URL}/{book_id}", json=book)
        response.raise_for_status()
        print(f"PUT book {book_id}")
        print(response.json())
        print("Status code:", response.status_code)
        return response.json()
    except requests.exceptions.HTTPError as err:
        print("HTTP error:", err)


def delete_book(book_id):
    """DELETE the book with the given id."""
    try:
        response = requests.delete(f"{API_URL}/{book_id}")
        response.raise_for_status()
        print(f"DELETE book {book_id}")
        print("Status code:", response.status_code)
    except requests.exceptions.HTTPError as err:
        print("HTTP error:", err)


def get_book(book_id):
    """GET a single book by id (used to confirm a deletion)."""
    try:
        response = requests.get(f"{API_URL}/{book_id}")
        response.raise_for_status()
        print(response.json())
        print("Status code:", response.status_code)
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error confirmed for id {book_id}:", err)


if __name__ == "__main__":
    # a. GET all books
    get_books()

    # b. POST a 6th book
    new_book = {
        "title": "Deep Work",
        "author": "Cal Newport",
        "rating": "8",
    }
    add_book(new_book)

    # c. PUT: replace book with id 2
    updated_book = {
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt",
        "rating": "9",
    }
    update_book(2, updated_book)

    # d. DELETE book 3, then GET it to confirm it is gone
    delete_book(3)
    get_book(3)  # should print an HTTP 404 error
