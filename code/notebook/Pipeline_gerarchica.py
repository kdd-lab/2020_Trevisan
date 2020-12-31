#!/usr/bin/env python
# coding: utf-8

# ### Pipeline gerarchica
# 
# **PIPELINE - APPROCCIO GERARCHICO**
# 
# Contributo algoritmico per semplificare il grafo trovando strutture ripetitive-ricorsive al suo interno.
# 
# Procedura:
# 
# ```
# Identificare sottografo motif (figure come la prima iterazione di un frattale)
# Collassare il motif in un solo nodo
# Aggiornare il peso e il colore degli archi
# Riapplicare il procedimento al grafo risultante (nuovo livello)
# ```

# In[1]:


from IPython import get_ipython


# In[2]:


import streamlit as st


# In[3]:


get_ipython().system('jupyter nbconvert   --to script Pipeline_gerarchica.ipynb')


# In[15]:


get_ipython().system("awkg '!/ipython/' Pipeline_gerarchica.py >  temp.py && mv temp.py app.py && rm Pipeline_gerarchica.py")


# In[ ]:


get_ipython().system('jupyter nbconvert   --to script Pipeline_gerarchica.ipynb')
get_ipython().system("awk '!/ipython/' Pipeline_gerarchica.py >  temp.py && mv temp.py app.py && rm Pipeline_gerarchica.py")
get_ipython().system('streamlit run Pipeline_gerarchica.py')


# In[ ]:


get_ipython().system('streamlit run temp.py')


# In[ ]:


import pandas as pd


# In[ ]:


st.title('My first app')


# In[ ]:


st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


# In[ ]:


"""
# My first app
Here's our first attempt at using data to create a table:
"""

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df


# In[ ]:


import numpy as np


# In[ ]:


chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


# In[ ]:


map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)


# In[ ]:


if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)


# In[ ]:


option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option


# In[ ]:


import networkx as nx
import itertools
from grandiso import find_motifs


# In[ ]:


get_ipython().run_line_magic('load_ext', 'pycodestyle_magic')
# %%pycodestyle


# #### Grafo test di base `G`

# In[ ]:


# grafo test di base G

G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (2, 4), (2, 5), (4, 5), (3, 6), (4, 6), (5, 6)])
# nx.draw(G)


# #### Sottografo `motif`

# In[ ]:


# Sottografo motif da trovare nel grafo G: TRIANGOLO

motif = nx.Graph()
motif.add_edges_from([("A", "B"), ("B", "C"), ("C", "A")])
# nx.draw(motif)


# In[ ]:


# Sottografo motif da trovare nel grafo G: QUADRATO

motif1 = nx.Graph()
motif1.add_edges_from([("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")])
# nx.draw(motif1)


# ## TODO: definisci una serie di pattern 

# In[ ]:


def identify(motif, G):
    lista1 = find_motifs(motif, G)
    lista2 = [list(d.values()) for d in lista1]
    lista3 = list(set(tuple(sorted(s)) for s in lista2))
    risultato = [list(el) for el in lista3] 
    return risultato

identify(motif, G)


# In[ ]:


identify(motif1, G)


# ## TODO: Collassare motif in un solo nodo rinominandolo

# In[ ]:


def contract(G):
    ris = identify(motif, G)
    a, b, c = ris[0][0], ris[0][1], ris[0][2]
    M = nx.contracted_nodes(G, a, b)
    MM = nx.contracted_nodes(M, a, c)
    print(MM.nodes())
    #nx.draw(MM)
    return MM


# livello 2

# In[ ]:


G1 = contract(G)


# livello 3

# In[ ]:


# in un loop sarebbe meglio
G2 = contract(G1)

