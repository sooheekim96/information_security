#!/usr/bin/env python
# coding: utf-8

# In[12]:


f= open("C:/Users/User/Downloads/ciphertextB.txt", 'r')
data=f.read()
def friedman(c,k):
    freq=[[0]*26 for i in range(k)]
    for i in range(len(c)):
        freq[i%k][ord(c[i])-65]+=1
    a1=0
    a2=0
    for i in range(k):
        a2+=sum(freq[i])*(sum(freq[i])-1)
        for j in range(26):
            a1+=freq[i][j]*(freq[i][j]-1)
    return a1/a2

key_length=[0,0]
for i in range(1, 11):
    
    if key_length[1]<friedman(data,i):
        key_length[0]=i
        key_length[1]=friedman(data,i)
print("key length:"+str(key_length[0]))
length=key_length[0]


# In[39]:


alphabetDict={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z'}
def findkey(encode, keylength):
    encode=list(encode)
    keylength=int(keylength)

    many=[]

    for i in range(0,keylength):
        many.append([])
    for i in range(0,len(encode)):
        many[i%keylength].append(encode[i])
        print(many[i%keylength])
        

    key=""
    #print(many[3])
    split_alphabet_frequency=[]
    for i in range(0,keylength):
        split_alphabet_frequency.append([])
        #print(split_alphabet_frequency)

    for i in range(0, keylength):
        for j in range(1,27):
            a=alphabetDict[j]
            split_alphabet_frequency[i].append([many[i].count(a),a])
            #print(split_alphabet_frequency[i])
        split_alphabet_frequency[i].sort(reverse=True)
        #print(split_alphabet_frequency[i])
        si=ord(split_alphabet_frequency[i][0][1])-ord('E')

        if si<0:
            si=si+65+26
            key=key+chr(si)
        else:
            si=si+65
            key=key+chr(si)
        count=0
        for j in many[i]:
            zi=ord('J')-(si-65)
            if zi<65:
                zi+=26
            #print(many[i])

            many[i][count]=chr(zi)
            count+=1
    return key
print(findkey(data, length))


# In[7]:


def decrypt(ciphertext, key):
    key_length=len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext=''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i]-key_as_int[i%key_length])%26
        plaintext+=chr(value+65)
    return plaintext


# In[10]:


print(decrypt(data, ))


# In[ ]:




