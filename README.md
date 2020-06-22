# Introduction

The overall aim of this project is building an NLP based application to detect and project future coronavirus death rates to help identify patterns, trends and public awareness levels related to coronavirus disease. This is to help simulate health system utilization levels and react immediately to prevent the spread of the virus and reduce death rates. 

In order to achive this aim:

- two different sentiment analysis on how the people's sentiments on Covid-19 changed on Twitter conducted, 
- time series analysis applied on UK daily coronavirus data to predict how the deaths rates will proceed,
- different regression models  explored to idenify any types of relationship between the daily change in UK coronavirus deaths and sentiments of the people on social media.

# Process Overview




# Data

A sample of Tweets between 15 March 2020 and 30 May 2020 that contains coronavirus and UK as keywords are imported for sentiment analysis. With inclusion of retweets 39873 tweets (22250 unique tweets) are used. 

Official coronavirus figures announced daily by the UK Government(https://coronavirus.data.gov.uk/) are used for time series analysis and as target values. 

# Methodology

The tweet data cleaned by removing punctuations, emojis, symbols, flags, pictographs and etc. in order to prevent any type of errors during modelling with VADER Sentiment Analyser. The polarity scores positive, negative, neutral and compound are added to the tweet dataframe as separate columns. As the Vader Sentiment analyzer calculates the four scores for each sentence, the compound scores are grouped as -1(negative) if the compound scores as below - 0.05, 1(positive) if they are  above 0.05, scores between labelled as 0(neutral). 

To further analyze the change in sentiments and compare with the Vader Analyzer's results with a custom model,  a pre-trained language model bert-base-uncased is choosen. This language model has 12-layers,  110M parameters and trained on lower-cased English text.

UK coronavirus death data is analyzed with Seasonal Arima model

To create a custom language model initially 1000 tweets labelled manually. It is important to note that the tweets about Covid-19 are highly negative and at some points it is difficult to distinct between neutral and negative ones. At first attempt to build the language model, only 0.70 accuracy achieved due to class imbalance. In order to overcome class imbalance further 400 positive and neutral tweets are labelled and this time 0.84 accuracy achieved.  




    


