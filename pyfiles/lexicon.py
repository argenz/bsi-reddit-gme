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
    'still': 3.0, 
    'rh': 1.0, 
    'holding': 4.0, 
    'trading': 1.0, 
    'webull': 3.5, 
    'late': 1.5, 
    'etoro': 1.0, 
    'wsb': 0.5, 
    'sold': -3.0, 
    'fuck': -1.5, 
    'bb': 1.0,
    'ig': 0.0, 
    'stop': -1.0, 
    'td': -1.5,       
    'keep': 1.5, 
    'nok': 1.0, 
    'hedge': -3.0, 
    'trading212': 0.0, 
    'fidelity': -1.0, 
    'etrade': 0.0, 
    'melvin': -1.0, 
    'missed': -1.0, 
    'fellow': 0.5, 
    'fucking': 0.0, 
     'diamond': 3.0,  
     'trade': 0.0, 
     'selling': -3.0, 
     'mods': 0.0,     

    }

def update_new_words(words, incoming_words):
    old_keys = set([k for k,v in words.items()]) 
    new_words = []
    for word in incoming_words: 
        if word not in old_keys:
            new_words.append(word)
    return new_words
