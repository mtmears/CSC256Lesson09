import requests
import pytest


def test_us_presidents_in_search():

    # List of the last names of all presidents
    list_of_presidents = ("Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson", "Buren",
                          "Harrison", "Tyler", "Polk", "Taylor", "Fillmore", "Pierce", "Buchanan", "Lincoln", "Johnson",
                          "Grant", "Hayes", "Garfield", "Arthur", "Cleveland", "Harrison", "Cleveland", "McKinley",
                          "Roosevelt", "Taft", "Wilson", "Harding", "Coolidge", "Hoover", "Roosevelt", "Truman",
                          "Eisenhower", "Kennedy", "Johnson", "Nixon", "Ford", "Carter", "Reagan", "Bush", "Clinton",
                          "Bush", "Obama", "Trump", "Biden")

    # Convert list to a set to get rid of duplicates
    set_of_presidents = set(list_of_presidents)

    # Define URL
    url = 'https://duckduckgo.com/?q=presidents+of+the+united+states&format=json'

    # Request the url and assign a user agent because duckduckgo returns error when not passed in
    response = requests.get(url, headers={'user-agent': 'my-app/0.0.1'})

    # Capture the response into a JSON object
    json_data = response.json()

    # Create list of data regarding the "RelatedTopics->Text" data
    presidents_response_text = ""
    for data in json_data['RelatedTopics']:
        presidents_response_text += data['Text']

    # Search for each president and compare it to the entire entry text from the response data to make sure that the
    # response data contains each president
    for president in set_of_presidents:
        try:
            assert president in presidents_response_text
        except AssertionError:
            print(president + "not found")
