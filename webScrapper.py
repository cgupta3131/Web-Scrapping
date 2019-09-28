from bs4 import BeautifulSoup
import requests
import json
 
 
 
def main():
    url = "http://ethans_fake_twitter_site.surge.sh"
    response = requests.get(url, timeout = 5)
    content = BeautifulSoup(response.content,"html.parser")
    tweetArr = []
 
    # print(content)
 
    for tweet in content.findAll('div', attrs={"class": "tweetcontainer"}):
        # print(tweet)
        tweetObject = {
        "author": tweet.find('h2', attrs={"class": "author"}).text,
        "date": tweet.find('h5', attrs={"class": "dateTime"}).text,
        "tweet": tweet.find('p', attrs={"class": "content"}).text,
        "likes": tweet.find('p', attrs={"class": "likes"}).text,
        "shares": tweet.find('p', attrs={"class": "shares"}).text,
        }
        tweetArr.append(tweetObject)
 
    with open('twitterData.json','w') as outFile:
        json.dump(tweetArr, outFile)
 
if __name__ == '__main__':
    main()