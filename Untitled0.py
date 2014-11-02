
# coding: utf-8

# In[9]:

from bs4 import BeautifulSoup
from steve.util import (get_project_config, get_from_config, load_json_files, save_json_files)
from steve import richardapi
import requests


# In[7]:

cfg = get_project_config()


# In[10]:

apiurl = get_from_config(cfg, 'api_url')


# In[14]:

category = richardapi.get_category(apiurl, 'PyCon US 2009')


# In[16]:

videos = category['videos']
    


# In[25]:

stevedata = []
for v in videos:
    r = requests.get(v)
    j = r.json()
    stevedata.append(('%s.json' % j['id'], j))


# In[27]:

save_json_files(cfg, stevedata)


# In[30]:

soup = BeautifulSoup(open('talks.html'))


# In[38]:

proposals_soup = soup.find_all('div', class_='proposal_list_summary')


# In[41]:

psoup = proposals_soup[0]


# In[82]:

def get_title_and_speakers(soup):                                                                                       
    header = soup.h2                                                                                                    
    spans = header.a.find_all('span')                                                                                   
    title = spans[1].text.strip()                                                                                       
    author = header.next_sibling.next_sibling.text                                                                      
    return title, author 


# In[89]:

speakerd = {}
for p in proposals_soup:
    title, speaker = get_title_and_speakers(p)
    speakerd[title] = speaker


# In[107]:

titles = []
for data in stevedata:
    title = data[1].get('title')
    titles.append(title.replace('PyCon 2009: ', ''))


# In[111]:

import json


# In[121]:

json.dump(stevedata, open('stevedata.json', 'w'), indent=2, sort_keys=True)


# In[120]:

json.dump(speakerd, open('scrapedspeakers.json', 'w'), indent=2, sort_keys=True)


# In[ ]:



