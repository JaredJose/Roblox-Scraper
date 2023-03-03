#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import nltk
from nltk import ngrams
from nltk.corpus import stopwords
import re
from sklearn.feature_extraction.text import TfidfVectorizer
import pyLDAvis.gensim
import gensim
import pickle 
import pyLDAvis
pyLDAvis.enable_notebook()
import os
import gensim.corpora as corpora
from nltk.corpus import stopwords
from gensim.utils import simple_preprocess


# In[22]:


df = pd.read_csv('data/robloxParentsComments.csv')


# In[23]:


df.head()


# In[24]:


df['comment']


# In[25]:


df['comment'].str.count('game').sum()


# In[26]:


text = " ".join(df['comment'].dropna().astype(str))
tokens = nltk.word_tokenize(text)
tokens = [re.sub(r'[^\w\s]', '', token) for token in tokens]
stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in tokens if token.lower() not in stop_words and token.strip() != '']


bi_grams = ngrams(filtered_tokens, 2)


# In[27]:


bi_grams_list = list(bi_grams)
bi_grams_list = [tuple(filter(None, bg)) for bg in bi_grams_list]
print(bi_grams_list)


# In[28]:


pattern = r'^\s*(who|what|when|where|why|how)\b.*\?$'
questions = df['comment'].str.extract('({})'.format(pattern), flags=re.IGNORECASE)[0].dropna()


# In[29]:


print(questions)


# In[30]:


bi_grams_list1 = [' '.join(bi_gram) for bi_gram in bi_grams_list if '(' not in bi_gram and ')' not in bi_gram]

freq_dist = nltk.FreqDist(bi_grams_list1)
most_common = freq_dist.most_common(1)
print('The most common bi-gram is:', most_common[0][0], 'with a frequency of', most_common[0][1])


# In[31]:


sums = tfidf.sum(axis = 0)
data1 = []
for col, term in enumerate(feature_names):
    data1.append( (term, sums[0, col] ))
ranking = pd.DataFrame(data1, columns = ['term', 'rank'])
words = (ranking.sort_values('rank', ascending = False))
print ("\n\nWords : \n", words.head(7))


# In[32]:


include_list = ['can','what','where','when','how','which','who','why']
df_ques = df['comment'].str.lower().str.contains('|'.join(include_list), na=False)
df_true = df.loc[df_ques]
print(df_true['comment'])


# In[ ]:





# In[33]:


df_ques = df['comment'].str.endswith('?')
df_true = df.loc[df_ques]
print(df_true['comment'])


# In[34]:


df['comment_processed'] = \
df['comment'].map(lambda x: re.sub('[,\.\!?]', '', x))

df['comment_processed'] = \
df['comment_processed'].map(lambda x: x.lower())

df['comment_processed'].head()


# In[35]:


stop_words = stopwords.words('english')
stop_words.extend(['from', 'subject', 're', 'edu', 'use'])
def sent_to_words(sentences):
    for sentence in sentences:
        # deacc=True removes punctuations
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))
def remove_stopwords(texts):
    return [[word for word in simple_preprocess(str(doc)) 
             if word not in stop_words] for doc in texts]
data = df.comment.values.tolist()
data_words = list(sent_to_words(data))
# remove stop words
data_words = remove_stopwords(data_words)
print(data_words[:1][0][:30])


# In[36]:


id2word = corpora.Dictionary(data_words)
texts = data_words
corpus = [id2word.doc2bow(text) for text in texts]
num_topics = 10
lda_model = gensim.models.LdaMulticore(corpus=corpus,
                                       id2word=id2word,
                                       num_topics=num_topics)

LDAvis_data_filepath = os.path.join('./results/ldavis_prepared_'+str(num_topics))
# # this is a bit time consuming - make the if statement True
# # if you want to execute visualization prep yourself
if 1 == 1:
    LDAvis_prepared = pyLDAvis.gensim.prepare(lda_model, corpus, id2word)
    with open(LDAvis_data_filepath, 'wb') as f:
        pickle.dump(LDAvis_prepared, f)
# load the pre-prepared pyLDAvis data from disk
with open(LDAvis_data_filepath, 'rb') as f:
    LDAvis_prepared = pickle.load(f)
s.makedirs('./results/ldavis_prepared_10')
pyLDAvis.save_html(LDAvis_prepared, './results/ldavis_prepared_'+ str(num_topics) +'.html')
LDAvis_prepared
pyLDAvis.display(LDAvis_prepared)


# In[ ]:





# In[ ]:





# In[ ]:




