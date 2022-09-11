import spacy
import re

ner = spacy.load('trf_ner\model-best')

def test_model():
    '''
    Check if the model is loaded properly
    '''
     
    ner = spacy.load('trf_ner\model-best')#need to have model in this path

    samples = ["Facebook has a price target of $ 20 for this quarter",
            "$ AAPL is gaining a new momentum"]

    doc = ner.pipe(samples[0])

    for doc in ner.pipe(samples,disable=['tagger','parser']):
        for ent in doc.ents:
            print(ent.label_, ent.text)
        print('-----')


def clean_tweets(texts):
    '''
    Preprocessing necessary for tweets, removing urls and three dots punctuations
    '''
    filtered = []
    url_pattern = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    for text in texts:
        string = re.sub(r''+str(url_pattern), '', text, flags=re.MULTILINE)
        string = re.sub(r'…','',string)
        string = re.sub(r'\.\.\.','',string)
        # print('This is Tweet: ',string)
        filtered.append(string)

    return filtered

def extract_ents(data):
    '''
    Main function to implement NER functionality
    '''
    texts = [tweet['text'] for tweet in data]
    for index,doc in enumerate(ner.pipe(clean_tweets(texts),disable=['tagger','parser'])):
        data[index]['entities'] = [{'text':ent.text,'label':ent.label_} for ent in doc.ents]
    return data