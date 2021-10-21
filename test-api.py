import pytest
import json
import requests

list_of_presidents = ['Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe', 'Jackson', 'Van Buren', 'Harrison', 'Tyler', 'Polk', 'Taylor', 'Fillmore', 'Pierce', 'Buchanan', 'Lincoln', 'Johnson', 'Grant', 'Hayes', 'Garfield', 'Arthur',
                      'Cleveland', 'McKinley', 'Roosevelt', 'Taft', 'Wilson', 'Harding', 'Coolidge', 'Hoover', 'Truman', 'Eisenhower', 'Kennedy', 'Nixon', 'Ford', 'Carter', 'Reagan', 'Bush', 'Clinton', 'Obama', 'Trump', 'Biden']


# performing request for DuckDuckGo API
url = 'https://api.duckduckgo.com'
response = requests.get(
    url + '/?q="presidents of the united states"&format=json&pretty=1')
jsonRes = response.json()

# The data I'm searching will be located in
# jsonRes['RelatedTopics'][0]['Text']

# this code loops through the list_of_presidents.
# For each president, call test_presidents_list passing in president name
# if the president string is found in a RelatedTopic['Text'], the
# function returns True, else it returns False


def test_presidents_list(list_of_presidents):
    for name in list_of_presidents:
        assert test_ind_name(name) == True


def test_ind_name(name):
    for rts in jsonRes['RelatedTopics']:
        if name in rts['Text']:
            return True
    return False


test_presidents_list(list_of_presidents)
