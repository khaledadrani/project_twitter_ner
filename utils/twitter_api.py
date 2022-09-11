import os
from dotenv import load_dotenv
import requests 

#load your credentials through the .env file
load_dotenv()

def create_headers():    
    
    api_key = os.getenv('api_key')
    api_key_secret = os.getenv('api_key_secret')
    bearer_token = os.getenv('bearer_token')
    access_token = os.getenv('acess_token')
    access_token_secret = os.getenv('acess_token_secret')

    
    headers = {
        "access_token":access_token,
        "access_token_secret":access_token_secret,
        "Authorization":'Bearer '+bearer_token,
        "api_key_secret":api_key_secret,
        "api_key":api_key
    }

    
    return headers

def create_url(keyword, max_results = 10):
    
    search_url = "https://api.twitter.com/2/tweets/search/recent?"

    
    query_params = {'query': keyword,
                    'max_results': max_results,
                    'tweet.fields': 'public_metrics'}
                    
    return (search_url, query_params)


def connect_to_endpoint(url, headers, params):
    
    response = requests.request("GET", url, headers = headers, params = params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()



def get_response(keyword="stocks",max_results=10,verbose=False):
    headers = create_headers()
    url = create_url(keyword, max_results=10)
    json_response = connect_to_endpoint(url[0], headers, url[1])

    if verbose:
        print(json_response)
        print(type(json_response))

    return json_response['data']
    
    
    
if __name__=="__main__":
    dic = get_response(verbose=True)









# consumer_key,consumer_secret,bearer_token,access_token,access_token_secret = load_env_vars()

# import tweepy

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# api = tweepy.Client(auth)

# cursor = tweepy.Cursor(api.search_all_tweets(query="stocks",max_results=2))

# for i in cursor:
#     print(i)
# print('HERE ! ')
# public_tweets = api.home_timeline(count=2)
# print('HERE ! ')
# for tweet in public_tweets:
#     print(tweet.text)