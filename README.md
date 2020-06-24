# Introduction

The overall aim of this project is building an NLP based application to detect and project future coronavirus death rates to help identify patterns, trends and public awareness levels related to coronavirus disease. This is to help simulate health system utilization levels and react immediately to prevent the spread of the virus and reduce death rates. 


# Overview

<img src="" width="100%">



# Data

A sample of tweets between 15 March 2020 and 30 May 2020 that contains coronavirus and UK as keywords are imported for sentiment analysis. With inclusion of retweets 39873 tweets (22250 unique tweets) are used. 

To create a custom language model around 1400 tweets labelled manually and accepted as grand truth. Later on the remaining tweet data is labelled through 

[Official coronavirus figures](https://coronavirus.data.gov.uk/)  announced daily by the UK Government are used for time series analysis. 

# Methodology

For sentiment analysis:

- Vader Sentiment Analyser 
- Bert-base-uncased language model

For time series analysis:

- SARIMA time series model

For machine learning modelling:

- Decision Tree classifier
- Random Forest classifier
- XGBoost classifier

are used. 

Recall, accuracy and f1 scores are used for evaluation metrics. 

## Sentiment Analysis:

The tweet data cleaned by removing punctuations, emojis, symbols, flags, pictographs and etc. in order to prevent any type of errors during modelling with VADER Sentiment Analyser. The polarity scores positive, negative, neutral and compound are added to the tweet dataframe as separate columns. As the Vader Sentiment analyzer calculates the four scores for each sentence, the compound scores are grouped as -1(negative) if the compound scores as below - 0.05, 1(positive) if they are  above 0.05, scores between labelled as 0(neutral). 

To further analyze the change in sentiments and compare with the Vader Analyzer's results with a custom model,  a pre-trained language model bert-base-uncased is choosen. This language model has 12-layers,  110M parameters and trained on lower-cased English text.


To create a custom language model initially 1000 tweets labelled manually. It is important to note that the tweets about Covid-19 are highly negative and at some points it is difficult to distinct between neutral and negative ones. At first attempt to build the language model, only 0.70 accuracy achieved due to class imbalance. In order to overcome class imbalance further 400 positive and neutral tweets are labelled.   

While the custom model achieved 84% accuracy, the VADER analyser could only predicted with 53% accuracy. As the visuals show the custom model outperformed VADER at analysing our sentiments. 

Vader polarity scores:
<img src="https://github.com/esraguzel/dsc-capstone-project-v2-onl01-dtsc-ft-012120/blob/master/images/vader.png?raw=true" width="100%">

Bert pre-trained model:
<img src="https://github.com/esraguzel/dsc-capstone-project-v2-onl01-dtsc-ft-012120/blob/master/images/sentiment.png?raw=true" width="100%">

Bert model change ratio of sentiments:
<img src="https://github.com/esraguzel/dsc-capstone-project-v2-onl01-dtsc-ft-012120/blob/master/images/change_sentiment.png?raw=true" width="100%">


## Time Series Analysis

For time series analysis, the data between 15 March - 30 May 2020 inspected for stationarity. The p-value was found to be less than 0.05. Therefore no  methods used to stationarize the data. 

In order to find the optimal p, d, q values with the lowest AIC value for SARIMA model a grid search conducted. 

Dynamic forecast:
<img src="https://github.com/esraguzel/dsc-capstone-project-v2-onl01-dtsc-ft-012120/blob/master/images/dynamicforecast.png?raw=true" width="100%">

<img src="https://github.com/esraguzel/dsc-capstone-project-v2-onl01-dtsc-ft-012120/blob/master/images/forecast.png?raw=true" width="100%">

## Machine Learning Classifiers 

In order to explore how the change in death rates affected our sentiments, in particular negative sentiments, DecisionTree, RandomForest and XGBoost Classifiers are used. 

The negative sentiment binned into two groups as target variable. Besides death rates, day of the weeks, shifted death rates, shifted positive sentiment change and shifted negative sentiment as features to predict change in negative sentiment. 

# Interpretation
## Findings:

## Recommendations:

This model, other than Coronavirus pandemic, can be used for any large scale of events to evaluate and take necessary measures to protect public mental health.

## Future work:

- In order to reach meaningful insights, more data points are needed covering a longer time period.

- Not only UK dataset, also Covid-19 related other datasets including R rate(infection rate), case number may be used for further exploration.






    


