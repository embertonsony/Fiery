#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[52]:


def_value_by_key(data):
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[9]:


# 7568 - 덩치

N = int(input())
size = []

for i in range(N):
    size.append(list(map(int, input().split())))

great = []
for i in range(N):
    for j in range(N):
        if size[i][0] < size[j][0] and size[i][1] < size[j][1]:
            great.append(size[j])
    print(len(great)+ 1, end=" ")
    great = []


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[51]:


a = ["SK하이닉스", "삼성전자", "LG전자"]
for i in a:
    print( i[0])


# In[ ]:





# In[76]:


a = ["I", "study", "python", "language", "!"]

for i in a:
    if i
        print(i)
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[8]:


a = 100
b = 3 / 5

i = 1

while  i <= 10:
    a = a * b
    print(i, a)
    i = i+1


# In[ ]:





# In[10]:


a = int(input())

if a == 1:
    print('일')
if a == 2:
    print('이')
if a == 3:
    print('삼')
    


# In[ ]:





# In[ ]:





# In[15]:


a = int(input())

if a <= 1924:
    print('가장 위대한 세대')

elif a <= 1945:
    print('침묵세대')
    
elif a <= 1964:
    print('x세대')
    
elif a <= 1980:
    print('밀레니러')

else:
    a >= 1997
    print('z세대')


# In[21]:


import pandas as pd
import numpy as np


# In[23]:


pd.Series(np.arange(3, 12,2), dtype='float32')


# In[26]:


pd.Series(list('가나다라마바사아'))


# In[32]:


sample = pd.Series(np.arange(10,60,10), index=list('가나다라마'))
sample


# In[38]:


sample[['나','라']]


# In[39]:


np.random.seed(20)
sample2 = pd.Series(np.random.randint(100,200, size=(15,)))
sample2


# In[44]:


sample2[sample2 <= 160]


# In[46]:


sample2[(sample2>=130)&(sample2<=170)]


# In[ ]:





# In[47]:


pd.Series(['apple', np.nan, 'banana', 'kiwi', 'gubong'], index=list('가나다라마'))


# In[48]:


sample = pd.Series(['IT서비스', np.nan, '반도체', np.nan, '바이오', '자율주행'])
sample


# In[50]:


sample[sample.isnull()]


# In[51]:


sample[sample.notnull()]


# In[52]:


np.random.seed(0)
sample = pd.Series(np.random.randint(100, 200, size=(10,)))
sample


# In[54]:


sample[2:7]


# In[55]:


np.random.seed(0)
sample2 = pd.Series(np.random.randint(100, 200, size=(10,)), index=list('가나다라마바사아자차'))
sample2


# In[58]:


sample2[5:]


# In[ ]:





# In[60]:


sample2[:3]


# In[65]:


sample2[1:6]


# In[ ]:





# In[2]:


import pandas as pd
PATH = "00_data/" # 00_데이터 폴더 안으로 들어가고 패스라는 변수로 지정했다.


# In[ ]:





# In[3]:


customers = pd.read_csv(PATH + "olist_customers_dataset.csv", encoding = "utf-8-sig")
geolocation = pd.read_csv(PATH + "olist_geolocation_dataset.csv", encoding = "utf-8-sig")
items = pd.read_csv(PATH + "olist_order_items_dataset.csv", encoding = "utf-8-sig")
payments = pd.read_csv(PATH + "olist_order_payments_dataset.csv", encoding = "utf-8-sig")
reviews = pd.read_csv(PATH + "olist_order_reviews_dataset.csv", encoding = "utf-8-sig")
orders = pd.read_csv(PATH + "olist_orders_dataset.csv", encoding = "utf-8-sig")
sellers = pd.read_csv(PATH + "olist_sellers_dataset.csv", encoding = "utf-8-sig")
category = pd.read_csv(PATH + "product_category_name_translation.csv", encoding = "utf-8-sig")
products = pd.read_csv(PATH + "olist_products_dataset.csv", encoding = "utf-8-sig")


# In[ ]:





# In[6]:


customers['customer_id'].nunique()


# In[42]:


items.head(11)


# In[40]:


items_1 = (items['freight_value']<10)
items_1


# In[43]:


items.loc[items_1,'price'] = 100


# In[44]:


items.loc[items_1]


# In[46]:


items.head()


# In[90]:


items.iloc[1:3, ['order_id']]


# In[85]:


items.loc[1:3,['order_id', 'price']]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[8]:


customers['customer_city'].value_counts()


# In[14]:


a  = customers.groupby('customer_city')['customer_id'].nunique().sort_values(ascending=False)
a


# In[ ]:





# ## 고객은 어떤 지불방법을 사용 했는가?

# In[4]:


payments


# In[7]:


payments.isnull().sum()


# In[ ]:





# In[12]:


payments_type_sum = payments.groupby('payment_type')['payment_value'].sum().sort_values(ascending=False)
payments_type_sum


# In[15]:


payments.groupby('payment_type')['order_id'].nunique().sort_values(ascending=False)


# In[ ]:





# ## 평균 거래액은 얼마인가?
# 

# In[16]:


orders


# In[21]:


orders.info()


# In[27]:


orders.isnull().sum()


# In[33]:


orders_drop = orders.dropna()
orders_drop.isnull().sum()
orders['order_id'].value_counts().max()


# In[36]:


payments.isnull().sum()
payments.info()
payments['order_id'].value_counts()


# In[38]:


payments.groupby('order_id').sum()


# In[37]:


payments[payments['order_id'] == 'fa65dad1b0e818e3ccc5cb0e39231352']


# In[40]:


merged = pd.merge(orders, payments, on='order_id')
merged.head()


# In[43]:


merged['order_approved_at'] = pd.to_datetime(merged['order_approved_at'], format='%Y-%m-%d %H:%M:%S', errors='raise')
merged['order_approved_at'].info()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




