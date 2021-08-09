import requests
from tqdm import tqdm 
from pprint import pprint as print


def get_url(author, start_index):
    base_url = "https://www.googleapis.com/books/v1/volumes?"
    q = f"q=inauthor:{author}"
    start_index = f"startIndex={start_index}"
    max_results = "maxResults=40"
    return base_url + q + "&" + start_index + "&" + max_results


def get_total_items(response):
    return response.json()['totalItems']


def get_items(response):
    try:
        return response.json()["items"]
    except:
        return []


def get_volume_info(item):
    return item["volumeInfo"]


def get_book_info(volume_info):
    result = {}
    try:
        result['description'] = volume_info['description']
        result['avatar'] = volume_info['imageLinks']['thumbnail']
        result['title'] = volume_info['title']
    except Exception as e:
        return None
    return result


def search_books_by_author(author:str) -> dict:
    books = []

    response = requests.get(get_url(author, 1))
    total_items = get_total_items(response)

    print(f"По автору {author} найдено {total_items} книги.")

    books_counter = 1

    for page in tqdm( range(1, total_items//40 + 2, 1) ):
        response = requests.get(get_url(author, books_counter))
        books_counter += 40
        items = get_items(response)
        for i in items:
            volume_info = get_volume_info(i)
            book_info = get_book_info(volume_info)
            books.append(book_info)
            
    cleared_books = []
    for book in books:
        if book != None:
            cleared_books.append(book)
            
    return cleared_books
