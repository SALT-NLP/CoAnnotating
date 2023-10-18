import json
import openai 
import pandas as pd
import time
import math
from collections import Counter

# This is set to `azure`
openai.api_type = "azure"
openai.api_key = ""
openai.api_base = ''
openai.api_version = '2023-03-15-preview'

# test
def prompt(text):
    response = openai.ChatCompletion.create(
        engine='chat',
        model="gpt-3.5-turbo",
        n=1,
        messages=[
            {
                "role": "user", 
                "content": text
            },
        ]
    )
    return response['choices'][0]['message']['content'].lower()

#df=df.read_csv('mrpc_train.csv')
#df=df.sample(n=1500,random_state=0)
df=pd.read_csv('mrpc_sample.csv')

#create prompts
df['prompt1']='Please label if the following two sentences are paraphrases of each other. Please give your answer as “paraphrase” or “not paraphrase”\n'+df['text']
df['prompt2']=df['text']+'\nPlease label if the two sentences above are paraphrases of each other. Please give your answer as “paraphrase” or “not paraphrase”'
df['prompt3']='Given the following two sentences, please classify the relationship of the following two sentences as “paraphrase” or “not paraphrase”\n'+df['text']
df['prompt4']='Is it true that the following two sentences are paraphrases of each other? Give your answer as “true” or “false”\n'+df['text']
df['prompt5']='Is it true that the following two sentences are not paraphrases of each other? Give your answer as “true” or “false”\n'+df['text']
df['prompt6']='What relationship do the following two sentences have? Is it “paraphrase” or “not paraphrase”?\n'+df['text']
df['prompt7']='Please choose one option that best describes the relationship between the following two sentences\n'+df['text']+'\n(A)Paraphrase\n(B)Not paraphrase'
df['prompt8']='I think the following two sentences are paraphrases of each other. Do you agree? Please give your answer in “yes” or “no”\n'+df['text']
df['prompt9']='I think the following two sentences are not paraphrases of each other. Do you agree? Please give your answer in “yes” or “no”\n'+df['text']

#df.to_csv('mrpc_train2.csv', index=False)

#inference
prompts=df['prompt1'].tolist()
res=[]
for p in prompts:
    try:
        resp = prompt(p)
        print(resp)
        res.append(resp)
        time.sleep(0.3)
    except:
        try:
            time.sleep(2)
            resp = prompt(p)
            print(resp)
            res.append(resp)
        except:
            print('ERROR!')
            res.append('error')
df['label1']=res


prompts=df['prompt2'].tolist()
res=[]
for p in prompts:
    try:
        resp = prompt(p)
        print(resp)
        res.append(resp)
        time.sleep(0.3)
    except:
        try:
            time.sleep(2)
            resp = prompt(p)
            print(resp)
            res.append(resp)
        except:
            print('ERROR!')
            res.append('error')
df['label2']=res


prompts=df['prompt3'].tolist()
res=[]
for p in prompts:
    try:
        resp = prompt(p)
        print(resp)
        res.append(resp)
        time.sleep(0.3)
    except:
        try:
            time.sleep(2)
            resp = prompt(p)
            print(resp)
            res.append(resp)
        except:
            print('ERROR!')
            res.append('error')
df['label3']=res


prompts=df['prompt4'].tolist()
res=[]
for p in prompts:
    try:
        resp = prompt(p)
        print(resp)
        res.append(resp)
        time.sleep(0.3)
    except:
        try:
            time.sleep(2)
            resp = prompt(p)
            print(resp)
            res.append(resp)
        except:
            print('ERROR!')
            res.append('error')
df['label4']=res

prompts=df['prompt5'].tolist()
res=[]
for p in prompts:
    try:
        resp = prompt(p)
        print(resp)
        res.append(resp)
        time.sleep(0.3)
    except:
        try:
            time.sleep(2)
            resp = prompt(p)
            print(resp)
            res.append(resp)
        except BaseException as e:
            print('ERROR!')
            res.append('error')
df['label5']=res


prompts=df['prompt6'].tolist()
res=[]
for p in prompts:
    try:
        resp = prompt(p)
        print(resp)
        res.append(resp)
        time.sleep(0.3)
    except:
        try:
            time.sleep(2)
            resp = prompt(p)
            print(resp)
            res.append(resp)
        except:
            print('ERROR!')
            res.append('error')
df['label6']=res

prompts=df['prompt7'].tolist()
res=[]
for p in prompts:
    try:
        resp = prompt(p)
        print(resp)
        res.append(resp)
        time.sleep(0.3)
    except:
        try:
            time.sleep(2)
            resp = prompt(p)
            print(resp)
            res.append(resp)
        except:
            print('ERROR!')
            res.append('error')
df['label7']=res

prompts=df['prompt8'].tolist()
res=[]
for p in prompts:
    try:
        resp = prompt(p)
        print(resp)
        res.append(resp)
        time.sleep(0.3)
    except:
        try:
            time.sleep(2)
            resp = prompt(p)
            print(resp)
            res.append(resp)
        except:
            print('ERROR!')
            res.append('error')
df['label8']=res

prompts=df['prompt9'].tolist()
res=[]
for p in prompts:
    try:
        resp = prompt(p)
        print(resp)
        res.append(resp)
        time.sleep(0.3)
    except:
        try:
            time.sleep(2)
            resp = prompt(p)
            print(resp)
            res.append(resp)
        except:
            print('ERROR!')
            res.append('error')
df['label9']=res

df.to_csv('result.csv', index=False)
