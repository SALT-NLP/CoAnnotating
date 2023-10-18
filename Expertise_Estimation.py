import pandas as pd

df=pd.read_csv('result.csv', index=False)
#translate (label 1,2,3,6)
def check(text):
    if 'not' in str(text):
        return 0
    else:
        return 1

#translate (label 4,5,6)
def check4(text):
    text=str(text).lower()
    if 'true' in text:
        return 1
    elif 'false' in text:
        return 0
    else:
        return 2

def check5(text):
    text=str(text).lower()
    if 'true' in text:
        return 0
    elif 'false' in text:
        return 1
    else:
        return 2
\
#translate (label7)
def check7(text):
    first_word=str(text).split()[0]
    if 'a' in first_word:
        return 1
    else:
        return 0

#translate (label8,9)
def check8(text):
    first_word=str(text).split()[0]
    if 'yes' in first_word:
        return 1
    elif 'no' in first_word:
        return 0
    else:
        return 2

def check9(text):
    first_word=str(text).split()[0]
    if 'yes' in first_word:
        return 0
    elif 'no' in first_word:
        return 1
    else:
        return 2

df['pred1']=df['label1'].apply(check)
df['pred2']=df['label2'].apply(check)
df['pred3']=df['label3'].apply(check)
df['pred4']=df['label4'].apply(check4)
df['pred5']=df['label5'].apply(check5)
df['pred6']=df['label6'].apply(check)
df['pred7']=df['label7'].apply(check7)
df['pred8']=df['label8'].apply(check8)
df['pred9']=df['label9'].apply(check9)

# Define a function to calculate entropy
def calculate_entropy(labels):
    n_labels = len(labels)
    if n_labels <= 1:
        return 0
    value_counts = {label: labels.count(label) for label in set(labels)}
    probabilities = [float(count) / n_labels for count in value_counts.values()]
    entropy = -sum([p * math.log2(p) for p in probabilities if p != 0])
    return entropy

entropy_res=[]
for index, row in df.iterrows():
    tmp=[]
    tmp.append(row['pred1'])
    tmp.append(row['pred2'])
    tmp.append(row['pred3'])
    tmp.append(row['pred4'])
    tmp.append(row['pred5'])
    tmp.append(row['pred6'])
    tmp.append(row['pred7'])
    tmp.append(row['pred8'])
    tmp.append(row['pred9'])
    entropy = calculate_entropy(tmp)
    entropy_res.append(entropy)
df['entropy']=entropy_res
df.to_csv('mrpc_train(entropy).csv',index=False)

#MV
modes=[]
for index, row in df.iterrows():
    tmp=[]
    tmp.append(row['pred1'])
    tmp.append(row['pred2'])
    tmp.append(row['pred3'])
    tmp.append(row['pred4'])
    tmp.append(row['pred5'])
    tmp.append(row['pred6'])
    tmp.append(row['pred7'])
    tmp.append(row['pred8'])
    tmp.append(row['pred9'])
    count = Counter(tmp)
    mode = count.most_common(1)
    modes.append(mode[0][0])
df['MV']=modes
df.to_csv('mrpc_train(entropy).csv',index=False)