import re, google, urllib
from bs4 import BeautifulSoup, SoupStrainer


def addToDict(string,dict):
    if string in dict:
        dict[string]+= 1
    else:
        dict[string] = 1;

def findMostCommon(dict, content):
    most_common_key = ""
    most_common_count = 0;
    for key in dict.keys():
        if dict[key] > most_common_count and key.lower()[:len(key)-1] not in content.lower():
            most_common_key = key
            most_common_count = dict[key]
    #print most_common_name.lower()
    #print content_words.lower()
    return most_common_key

def findWho(text, content):
    names = {}
    regex = "([A-Z]\w*|Mr.|Mrs.|Ms.|Dr|Sir.)\s([A-Z]\w*\s?)+"
    for match in re.finditer(regex, text):
        addToDict(match.group(),names)
    return findMostCommon(names, content)

def findWhen(text, content):
    dates = {}
    regex = "(January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{1,4}( BC| AD|)?"
    for match in re.finditer(regex, text):
        addToDict(match.group(),dates)
    return findMostCommon(dates, content)

def findWhere(google_results, content):
    locations=["street","alley","avenue","place","st","drive","ave","manor","house","school","tower","building","road","city","state","nation"]
    regex="((\d{1,4}\w?) [A-Z]\w+ ([A-Z]\S+ )+)"
    results = re.findall(regex,google_results)
    answers={}
    print results
    for result in results:
        loc=False;
        for word in result[0].split(" "):
            if word.lower() in locations:
                loc=True
        if loc:
            addToDict(result[0],answers)
    print answers
    return findMostCommon(answers,content)

def search_query(question):
    question_word= (question.split(" ")[0]).lower()
    content_words=" ".join(question.split(" ")[1:])
    g= google.search(question, num=20, stop=20)
    search_results=""
    only_p= SoupStrainer("p")

    for result in g:
        search_results += BeautifulSoup(urllib.urlopen(result),parse_only=only_p).get_text()
        #print search_results

    response=""
    if question_word == "who":
        response = findWho(search_results,content_words)
    elif question_word == "where":
        response = findWhere(search_results, content_words)
    elif question_word == "when":
        response = findWhen(search_results,content_words)
    return response
