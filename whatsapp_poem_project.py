from pprint import pprint
from random import choice, randint
import requests
import os


poetry_database_api_url = "https://poetrydb.org/author/"
poets_to_get = [
    "Edgar Allan Poe",
    "Emily Dickinson",
    "John Keats",
    "Oscar Wilde",
    "William Shakespeare",
    "William Wordsworth",
]


def fetch_poems():
    """fetching poems from poem DB and passing them as msg contents"""
    #  getting random poets
    poet_to_fetch = choice(poets_to_get)

    # fetching poems of that poet
    poem_response = requests.get(f"{poetry_database_api_url}{poet_to_fetch}")
    poem_response.raise_for_status
    poem_data = choice(poem_response.json())
    poem_title = poem_data["title"]
    poem_lines = "\n".join(poem_data["lines"])
    poem_to_mail = create_poem_body(poet_to_fetch, poem_title, poem_lines)
    return poem_to_mail


def create_poem_body(poet, title, poem):
    """Create email message body"""
    poet_name = f"- {poet}"
    ending_message = f"To Jan, from Div"
    if randint(0, 11) == 10:
        special_message = "I love you more than football, also if you get this message today's gonna be lucky since there is only a 0.1% chance of this happening :p"
        poem_to_send = (
            f"☾\n{special_message}\n{title}\n{poem}\n{poet_name}\n{ending_message}\n☽"
        )
        return poem_to_send
    else:
        poem_to_send = f"🌕\n{title}\n{poem}\n{poet_name}\n{ending_message}\n🌕"
        return poem_to_send
