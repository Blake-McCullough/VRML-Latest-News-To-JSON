import requests
from bs4 import BeautifulSoup
import json

newslist = []

#
#
#get news from VRML (Scheduled once a day)
#
#
def get_VRML_NEWS(game):

    url = 'https://api.vrmasterleague.com/' + game['vrmlgameformat']
    response = requests.get(url, verify=False)

    newsjson = response.json()

    newsbody = ""
    soop = BeautifulSoup(newsjson["newsPosts"][1]['html'], "html.parser")

    for linkyboi in soop.find_all("p"):

        linkyboii = linkyboi.text

        newsbody = newsbody + linkyboii + '\\n'

    date = newsjson["newsPosts"][1]["dateEditedUTC"]
    title = newsjson["newsPosts"][1]["title"]
    source = 'VRML-' + game['readfriendly']
    newslist.append({
        "Contents": newsbody,
        "Date": date,
        "Title": title,
        'Source': source
    })


#
#
#Final Result
#
#

if __name__ == "__main__":
    gameslist = [{
        'vrmlgameformat': 'snapshot',
        'readfriendly': 'Snap Shot'
    }, {
        'vrmlgameformat': 'echoarena',
        'readfriendly': 'Echo Arena'
    }, {
        'vrmlgameformat': 'onward',
        'readfriendly': 'Onward'
    }, {
        'vrmlgameformat': 'pavlov',
        'readfriendly': 'Pavlov'
    }, {
        'vrmlgameformat': 'contractors',
        'readfriendly': 'Contractors'
    }, {
        'vrmlgameformat': 'FinalAssault',
        'readfriendly': 'Final Assault'
    }]
    for game in gameslist:
        get_VRML_NEWS(game)
    print(newslist)
    with open('latest-vrml-news.json', 'w') as f:
        json.dump(newslist, f)
