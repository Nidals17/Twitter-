import tweepy
import json
import pandas as pd
import re
from collections import Counter
import plotly.express as px
import plotly.figure_factory as ff
from nltk import ngrams
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from worddcloud import *
api_key=''
api_key_secret=''

access_token=''
access_token_secret=''

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


stop1 = ["ourselves", "hers", "between", "yourself", "but", "again", "there", "about","The", "once", "during", "out",
            "very", "having", "with", "they", "own", "an", "be", "some", "for", "do", "its", "yours", "such", "into", "of",
            "most", "itself", "other", "off", "is", "s", "am", "or", "who", "as", "from", "him", "each", "the", "themselves",
            "until", "below", "are", "we", "these", "your", "his", "through", "don", "nor", "me", "were", "her", "more", "himself",
            "this", "down", "should", "our", "their", "while", "above", "both", "up", "to", "ours", "had", "she", "all", "no",
            "when", "at", "any", "before", "them", "same", "and", "been", "have", "in", "will", "on", "does", "yourselves", "then", 
            "that", "because", "what", "over", "why", "so", "can", "did", "not", "now", "under", "he", "you", "herself", "has", "just",
            "where", "too", "only", "myself", "which", "those", "i", "after", "few", "whom", "t", "being", "if", "theirs", "my", 
            "against", "a", "by", "doing", "it", "how", "further", "was", "here", "than","b", "c", "d", "e", "f", "g", "h", "i", 
            "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","rt"]
fields = 'keyword',
def fetch(entries):
    for entry in entries:
        #field = entry[0]
        text  = entry[1].get()
        #print(type(field), type(text)) 
        
        
        #search tweets
        limit=1000
        tweets1=tweepy.Cursor(api.search_tweets , count=100, q=text, lang='en',
                             tweet_mode='extended').items(limit)
        liste1=[]
        with open('verlaine1.json', 'w') as file:
            for i in tweets1:
                liste1.append(i._json)
        
        #creation de la dataframe pour contenir les tweets 
        df1=pd.DataFrame(liste1)
        df=df1[["full_text"]]
        df.drop_duplicates(keep=False, inplace=True)
        #le code suivant supprime les hashtags, re-tweet, les liens hypertext,...
        clean_tweet1=[]
        k=[]

        for i in df["full_text"]:
            k=re.sub("@[A-Za-z0-9_]+","", i)    
            k=re.sub("#[A-Za-z0-9_]+","", k)
            k=re.sub('VIDEO:', '', k)
            k=re.sub('AUDIO:', '', k)
            k=re.sub('(RT\s@[A-Za-z]+[A-Za-z0-9-_]+)', '', k)
            k=re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', " ", k)
            clean_tweet1.append(k)

        df2=pd.DataFrame()
        df2["clean_text"]=pd.DataFrame(clean_tweet1)
        df2["clean_text"]=df2["clean_text"].str.replace('[^A-Za-z0-9]', ' ', flags=re.UNICODE)
        df2["clean_text"]=df2["clean_text"].apply(str.lower)
        df2["clean_text"] = df2["clean_text"].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop1)]))
        
        df3=pd.DataFrame()
        df3['clean_text'] = df2['clean_text'].apply(lambda x:str(x).split())
        
        #plot most common word
        top = Counter([item for sublist in df3['clean_text'] for item in sublist])
        temp = pd.DataFrame(top.most_common(20))
        temp.columns = ['Common_words','count']
        temp.style.background_gradient(cmap='Blues')

        fig = px.bar(temp, x="count", y="Common_words", title='Commmon Words in Selected Text', orientation='h', 
             width=700, height=700,color='Common_words')
        fig.show()
        
        plot_wordcloud(df2["clean_text"],mask=mask)
        
        list_articles = df2['clean_text'].tolist()
        # Tokenisation des articles
        list_tokens = ' '.join(list_articles).split()
        # Identification et compte des bigrams
        list_bigrams = list(ngrams(list_tokens, 3)) 
        counter = Counter(list_bigrams)
        # Création d'un dataframe contenant le top 20 bigramme les plus fréquents
        df_plot = pd.DataFrame(counter.most_common(35))
        # Création du graphique
        plt.figure(figsize=(15,5))
        plot = sns.barplot(x=df_plot[1], 
                           y=df_plot[0],
                           color='#44546a')

        plt.xlabel('occurrence')
        plt.ylabel("bigramme")
        plt.title(f"Top 20 bigrammes") 
        plt.show()
        

        #create word network
        df_plot["bigrams"]=df_plot[0]
        df_plot["count"]=df_plot[1]
        del df_plot[0]
        del df_plot[1]
        # Create dictionary of bigrams and their counts
        d = df_plot.set_index('bigrams').T.to_dict('records')

        # Create network plot 
        G = nx.Graph()

        # Create connections between nodes
        for k, v in d[0].items():
            G.add_edge(k[0], k[1], weight=(v * 10))

        G.add_node("queen", weight=100)

        fig, ax = plt.subplots(figsize=(15, 10))

        pos = nx.spring_layout(G, k=2)

        # Plot networks
        nx.draw_networkx(G, pos,
                         font_size=10,
                         width=1,
                         edge_color='black',
                         node_color='cyan',
                         with_labels = False,
                         ax=ax)

        # Create offset labels
        for key, value in pos.items():
            x, y = value[0]+.135, value[1]+.045
            ax.text(x, y,
                    s=key,
                    bbox=dict(facecolor='white', alpha=0.25),
                    horizontalalignment='center', fontsize=8)
        plt.show()
     
