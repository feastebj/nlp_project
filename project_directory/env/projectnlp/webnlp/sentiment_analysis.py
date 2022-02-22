import nltk
from nltk.corpus import sentiwordnet as swn
import spacy

nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('sentiwordnet')
nlp = spacy.load('en_core_web_sm')

def sentiwordnet_analyze(text):

    # tokenize and POS tag
    tagged_text = [(token.text, token.tag_) for token in nlp(text)]
    token_count = 0
    scored_tokens = []

    # get wordnet synsets based on POS tags and get sentiment scores if synsets found
    for word, tag in tagged_text:
        ss_set = None
        if 'NN' in tag and list(swn.senti_synsets(word, 'n')):
            ss_set = list(swn.senti_synsets(word, 'n'))[0]
        elif 'VB' in tag and list(swn.senti_synsets(word, 'v')):
            ss_set = list(swn.senti_synsets(word, 'v'))[0]
        elif 'JJ' in tag and list(swn.senti_synsets(word, 'a')):
            ss_set = list(swn.senti_synsets(word, 'a'))[0]
        elif 'RB' in tag and list(swn.senti_synsets(word, 'r')):
            ss_set = list(swn.senti_synsets(word, 'r'))[0]
        
        if ss_set:
            scored_tokens.append((word , ss_set.pos_score() - ss_set.neg_score()))
            token_count += 1
        else:
            scored_tokens.append((word, None))

    
    # aggregate final scores
    final_score = sum([tok[1] if tok[1] else 0 for tok in scored_tokens])
    norm_final_score = round(final_score / token_count, 2)
        
    return norm_final_score, scored_tokens

def get_sentiment_color(sent):
    if sent is None:
        return "#000"
    r = g = 0
    if sent < 0:
        r = int(abs(sent * 255))
    else:
        g = int(sent*255)
    return '#%02X%02X00' % (r, g)