import re 
import spacy

new_words = {
    'citron': -4.0,  
    'hidenburg': -4.0,        
    'moon': 4.0,
    'highs': 2.0,
    'mooning': 4.0,
    'long': 2.0,
    'short': -2.0,
    'call': 4.0,
    'calls': 4.0,    
    'put': -4.0,
    'puts': -4.0,    
    'break': 2.0,
    'tendie': 2.0,
    'tendies': 2.0,
    'town': 2.0,     
    'overvalued': -3.0,
    'undervalued': 3.0,
    'buy': 4.0,
    'sell': -4.0,
    'gone': -1.0,
    'gtfo': -1.7,
    'paper': -1.7,
    'bullish': 3.7,
    'bearish': -3.7,
    'bagholder': -1.7,
    'stonk': 1.9,
    'green': 1.9,
    'money': 1.2,
    'print': 2.2,
    'rocket': 2.2,
    'bull': 2.9,
    'bear': -2.9,
    'pumping': -1.0,
    'sus': -3.0,
    'offering': -2.3,
    'rip': -4.0,
    'downgrade': -3.0,
    'upgrade': 3.0,     
    'maintain': 1.0,          
    'pump': 1.9,
    'hot': 1.5,
    'drop': -2.5,
    'rebound': 1.5,  
    'crack': 2.5
}

new_words_updated = {
    'citron': -4.0,  
    'hidenburg': -4.0,        
    'moon': 4.0,
    'highs': 2.0,
    'mooning': 4.0,
    'long': 2.0,
    'short': -2.0,
    'call': 4.0,
    'calls': 4.0,    
    'put': -4.0,
    'puts': -4.0,    
    'break': 2.0,
    'tendie': 2.0,
    'tendies': 2.0,
    'town': 2.0,     
    'overvalued': -3.0,
    'undervalued': 3.0,
    'buy': 4.0,
    'sell': -4.0,
    'gone': -1.0,
    'gtfo': -1.7,
    'paper': -1.7,
    'bullish': 3.7,
    'bearish': -3.7,
    'bagholder': -1.7,
    'stonk': 1.9,
    'green': 1.9,
    'money': 1.2,
    'print': 2.2,
    'rocket': 2.2,
    'bull': 2.9,
    'bear': -2.9,
    'pumping': -1.0,
    'sus': -3.0,
    'offering': -2.3,
    'rip': -4.0,
    'downgrade': -3.0,
    'upgrade': 3.0,     
    'maintain': 1.0,          
    'pump': 1.9,
    'hot': 1.5,
    'drop': -2.5,
    'rebound': 1.5,  
    'crack': 2.5,
    
    ######New
    'gme': 0.0,
    'robinhood': 1.0, 
    'bought': 3.0, 
    'hold': 4.0, 
    'amc': 2.0, 
    'revolut': 1.0, 
    'buying': 3.5, 
    #'anyone', 
    'still': 3.0, 
    #'new', 
    'rh': 1.0, 
    'holding': 4.0, 
    #'guys', 
    'trading': 1.0, 
    #'someone', 
    'webull': 3.5, 
    #'got', 
    'late': 1.5, 
    'etoro': 1.0, 
    'wsb': 0.5, 
    'sold': -3.0, 
    #'get', 
    'fuck': -1.5, 
    #'everyone', 
    'bb': 1.0,
    #'don’t', 
    #'need', 
    #"can't", 
    #'know', 
    'ig': 0.0, 
    #'first', 
    'stop': -1.0, 
    #'dont', 
    #'uk', 
    'td': -1.5,       #toronto bank
    #'people', 
    #'can’t', 
    'keep': 1.5, 
    #'want', 
    #'think', 
    #'next', 
    #'hey', 
    #'help', 
    'nok': 1.0, 
    'hedge': -3.0, 
    #'one', 
    #'please', 
    #'im', 
    #'let’s', 
    #'made', 
    'trading212': 0.0, 
    #'lets', 
    'fidelity': -1.0, 
    #'would', 
    #'much', 
    #'even', 
    'etrade': 0.0, 
    'melvin': -1.0, 
    'missed': -1.0, 
    #"let's", 
    #'question', 
    #'like', 
    #'time', 
    'fellow': 0.5, 
    #'it’s', 
    #'could', 
    #'psa:', 
    #'trying', 
    #'what’s', 
    #'good', 
    #'going', 
    #'1', 
    'fucking': 0.0, 
    #'looks',
     #"what's", 
     #'love', 
     #'look', 
     #'finally', 
     #'go', 
     #'real', 
     'diamond': 3.0, 
     #'best', 
     #'cant', 
     #'many', 
     'trade': 0.0, 
     'selling': -3.0, 
     #'happens', 
     #'never', 
     #'another', 
     'mods': 0.0,     #minecraft ref?
     #'make', 
     #'thank', 
     #'today', 
     #'see', 
     #'us'
    }

def update_new_words(words, incoming_words):
    old_keys = set([k for k,v in words.items()]) 
    new_words = []
    for word in incoming_words: 
        if word not in old_keys:
            new_words.append(word)
    return new_words

    #emoji

def remove_emoji(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags 
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)
    
nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])

def space(comment):
    doc = nlp(comment)
    return " ".join([token.lemma_ for token in doc])