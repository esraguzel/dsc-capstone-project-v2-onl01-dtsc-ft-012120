import matplotlib.pyplot as plt

def remove_emojis(text):
    import re
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', text)


# Define text processing function
def preprocess(text):
    import re, string
    
    text = text.replace('(<br/>)', ' ')
    text = text.replace('(&amp)', ' ')
    text = text.replace('(&gt)', ' ')
    text = text.replace('(&lt)', ' ')
    text = text.replace('(\xa0)', ' ')
    text = text.replace(r'\n',' ',)
    text = text.replace('"',' ',)
    text = text.replace("'",' ',)
    
    # Remove URL
    text = re.sub(r"(?:\@|http?\://|https?\://|www.)\S+", "", text)
    
    # Remove emoji
    text = remove_emojis(text)
    
    # Remove punctuation
    text = text.translate(str.maketrans(' ', ' ', string.punctuation))
    
    # Remove white space
    text = " ".join(text.split())
    
    return text

# plot confusion matrix
def plot_con_matrix(labels, predictions, normalize=False, cmap='Spectral'):
    
    import pandas as pd
    import numpy as np
    import itertools
    import seaborn as sns
    from sklearn.metrics import confusion_matrix
    
    cm = confusion_matrix(labels, predictions)
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    df_cm = pd.DataFrame(cm, ['POS', 'NEG'], ['POS', 'NEG'])
    sns.heatmap(df_cm, annot=True, annot_kws={'size':16}, fmt='g', cmap=cmap)
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()
    
#plot roc curve    
def plot_roc_curve(labels, predictions, y_score):
    
    from sklearn.metrics import roc_curve, auc, roc_auc_score
    import seaborn as sns
    
    fpr, tpr, thresholds = roc_curve(labels, y_score)
    print('AUC: {}'.format(auc(fpr, tpr)))
    #Seaborns Beautiful Styling
    sns.set_style("darkgrid", {"axes.facecolor": ".9"})
    plt.figure(figsize=(10,8))
    lw = 2
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve')
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.yticks([i/20.0 for i in range(21)])
    plt.xticks([i/20.0 for i in range(21)])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic (ROC) Curve')
    plt.legend(loc="lower right")
    plt.show()
    