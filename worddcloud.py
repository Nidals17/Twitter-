import random
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def plot_wordcloud(text, mask):
                
                if "queen" in text or "elizabeth" in text:
                    mask = np.array(Image.open('C:/Users/verla/OneDrive/Documents/Université de Strasbourg/Advanced_programming-main/Projet/queen.jpg'))            
 
  
                else:
                    mask = np.array(Image.open('C:/Users/verla/OneDrive/Documents/Université de Strasbourg/Advanced_programming-main/Projet/cloud.jpg'))
                wordcloud = WordCloud(background_color='white',
                 max_words = 200,
                 max_font_size = 100, 
                 random_state = 42,
                 width=400, 
                 contour_color="gray",
                 contour_width=0.1,stopwords=STOPWORDS,
                   
                 height=200,
                 mask = mask)
                wordcloud.generate(str(text))
                
                plt.figure(figsize=(24.0,16.0))
                plt.imshow(wordcloud, interpolation="bilinear");

                plt.axis('off');
                plt.tight_layout() 
