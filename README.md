# Project-2-
# Housing Price Sentiment
_________

# Project Goal 
Create an investment tool that will allow the user to predict the trends of real estate by analyzing the increase in housing prices as it relates to the mortgage rates. The tool will analyze historical mortgage rates and look for confluence and divergence between the housing prices and mortgage rates. Using the 30yr and 15yr mortgage rates as an indicator we can predict the future outlook of the housing market. The sentiment will be gauged by using NLP to see if there is a correlation with sentiment on twitter and our predictor. We can use this tool to assess the correlations and judge if it is the right time to look for houses.

## **Our Challenge**
The Case-Shiller Home Price Index is delivered on a monthly basis. Although our data originates in 1987, 12 data points a year is not a lot. We decided to do 2 variations of our study. First we will **modify** our data by using a forward fill method which assigns the data that was delivered at the beginning of the month to fill all days in the month until the next delivery the following month. This will give us approximately 30x more data than the original dataset. 
Next we will use the **original** dataset as we ultimately want to be as unbiased as possible although it has less data points, it is true to delivery. This will give us the real picture. 

Biased : https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/Project_2_Housing_price_sentiment_Advisor(Biased).ipynb


Non Biased : https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/Project_2_Housing_price_sentiment_Advisor(Original).ipynb

# Group Questions
1. Is there a correlation with mortgage rates and housing prices?
2. What states index is lower than the US National benchmark?
3. What states index is Higher then the US National benchmark?
4. Do we foresee a slowdown or a correction in the future?
5. What is the overall sentiment of the housing market right now?

## Data Cleaning Process 

- Data was gathered using an API from **Pandas DataReader** being pulled from **FRED** or _Federal Reserve Econommic Data_. 
- Cleaned the Data by dropping na, removing null, we restructured our data using various column manipulation techniques.

---

## Sentiment Analysis
![alt="housingmarket_mortgagerates_wordcloud"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/housingmarket_mortgagerates_wordcloud.png?raw=true)

Our sentiment analysis tool scrapes twitter based on keywords, amount of tweets to be analyzed and amount of days back to scrape
Based on these tweets, we use regex to clean the tweets and sentiment intensity analyzer to analyze the tweets and give us a polarity score for each tweet. 
Using the sentiment from the intensity analyser we categorized our negative and positive tweets and ran several machine learning models. 
Results vary according to each search. On Average, according to our test accuracy scores, our model predicts around 60%.

In this wordcloud example we used Housing Market and Mortgage Rates as our search words, 1000 tweets in the last year (365 days). We can see interest rates, housing and inflation as some of the bigger words besides the search words. Some words that stand out to us here are demand, increase, rising, high.. Interestingly a few months populate in the graph (march, may, april) 

![alt="sentiment_analysis_piechart"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/sentiment_analysis_piechart.png?raw=true)

Based on our findings, we can see that there is 49% positive sentiment as it relates to the housing market and mortgage rates tweets on twitter while there is a 39% negative sentiment in tweets going around in the last year. 

![alt="naive_bayes_complementNB_twitter_sentiment"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/naive_bayes_complementNB_twitter%20sentiment.png?raw=true)
![alt="naive_bayes_multinominalNB_twitter_sentiment"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/naive_bayes_multinominalNB_twitter%20sentiment.png?raw=true)
![alt="logistic_regression_twitter_sentiment"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/logistic_regression_twitter%20sentiment.png?raw=true)

The three models we used on the sentiment are 1 logistic regression model and 2 naive bayes models, one being complement naive bayes the other multinomnal naive bayes. 
The compliment naive bayes model is the most balanced as it is able to predict both negative and positive tweets unlike the other 2 models. Although we do not have a lot of support we are still able to predict the sentiment with a 60% accuracy on average.

---

## Prophet
Using Prophet, we ran a dynamic time series study to analyze all Case Shiller Indices and the 15 and 30 year fixed mortgage rate trends. 

This is where things got interesting for us. Our data tells 2 very different stories. When we forward filled our data we do not see any softening in the near future just a smooth climb. There is a slight dip in the upper and lower yhats but doesnt seem any larger than anything we have seen in recent months, December. Looking at the non biased case shiller housing price index we can see fluctuations in housing prices which make more sense as the prices do in fact rise and drop. However, these fluctuations are relatively consistent ranging around 5000 or so, despite the approximate 15k climb in march of 2022.  Looking at the right side of the chart forecasting the future we can see a significant rally in the coming march by approximately 45k which is 3x the size of the previous march. Although our view is limited, the correction after marches spike seems significantly larger than the previous years pullback, indicating to us we may see a housing market crash in the coming March of 2023.

![alt="biased_ny_forecast"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/biased_ny_forecast.png?raw=true)

![alt="nonbiased_ny_forecast"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/nonbiased_ny_forecast.png?raw=true)

Initially we did not understand the significant decline in the housing prices we figured it was due to insufficient data points. We decided to increase amount of data points used by carrying the data delivered on the first of the month to be delivered daily until the beginning of the following month. After doing this we found our data was too biased and therefore giving us a total opposite outcome from the original data. 

---

## Machine Learning Outcomes

We wanted to see if we can predict the future price of the state housing price index using the average of the last 5 and 13 datapoints as our signal. 
 
Precision is the ability of a classifier not to label an instance positive that is actually negative. It is the ratio of True Positives to the sum of true and false positives — [ TP / (TP + FP ) ] ----

Recall is the ability of a classifier to find all positive instances. It is the ratio of True Positives to the sum of True positives and False Negatives. –[ TP / (TP + FN) ]--

The F1 score is a weighted harmonic mean of precision and recall such that the best score is 1.0 and the worst is 0.0. Generally speaking, F1 scores are lower than accuracy measures as they embed precision and recall into their computation.

### AdaBoost Classifier
Using the AdaBoost classifier we had a very high precision and recall score predicting higher pricing. However it has a 0 overall score predicting negative occurrences. 
Our non biased passive aggressive classification report did not have a lot of support. With an average score of .64 for positive occurrences and .11 for negative occurrences we were not confident with this outcome.

![alt="biased__ada"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/biased__ada.png?raw=true)
![alt="biased__ada_classification_report"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/biased__ada_classification_report.png?raw=true)
![alt="nonbiased__ada"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/nonbiased__ada.png?raw=true)
![alt="nonbiased__ada_classification_report"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/nonbiased__ada_classification_report.png?raw=true)

### Decision Tree

we had a very high precision and recall score using the Decision Tree classification report as it relates to predicting higher pricing. However it has a 0 overall score predicting negative occurrences. 

![alt="nonbiased__decision_tree"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/nonbiased__decision_tree.png?raw=true)
![alt="biased__decision_tree"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/biased__decision_tree.png?raw=true)

### Passive Aggressive 
We had a very high precision and recall score using the Biased Passive aggressive classification report as it relates to predicting higher pricing. However it has a 0 overall score predicting negative occurrences. Our non biased passive aggressive classification report did not have a lot of support but overall performed pretty well. 


![alt="non_biased_passive_aggressive_classification_report"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/non_biased_passive_aggressive_classification_report.png?raw=true)
![alt="non_biased_passive_aggressive_train_test_scores"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/non_biased_passive_aggressive_train_test_scores.png?raw=true)
![alt="biased_passive_aggressive_classification"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/biased_passive_aggressive_classification_report.png?raw=true)
![alt="biased_passive_aggressive_train_test_scores"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/biased_passive_aggressive_train_test_scores.png?raw=true)

---

## Data Analysis in summary

- We took the cleaned data and split data to get started for **Natural Language Processing** 
  - NLP we used a few different methods here **WordCloud, Vader Sentiment Intensity Analyzer, PorterStemmer/ Lemmatizer**
- After we took a look at the sentiments on _NLP_ we started our **Machine Learning**
   - **ML** we used Naive Bayes and Logistic Regression 
   - Naive bayes (https://machinelearningmastery.com/naive-bayes-for-machine-learning/) for a better understanding of now _Naive Bayes_ works.
- Another method of **ML** is _Logistic Regression_ (https://www.ibm.com/topics/logistic-regression#:~:text=Logistic%20regression%20estimates%20the%20probability,bounded%20between%200%20and%201.)
- Lastly for our _Data Analytics_ we used **Facebook Prophet** for Machine Learning on Index and Mortgage rates: SVM, ADABoostClassifier, Decision Tree Classifier, Passive Aggressive Classifier

## Professional Subjective Opinion

Based on our findings using the ***Non-Biased (not ffill) Data Points*** our data concludes ***Market Correction*** in the coming **2023 Year**.

**Mortage Rates** and **Housing prices** generally have an inverse correlation as shown in the **NonBiased** data set. When **Mortgage Rates** are high we can see that Housing prices are typically reduced.

There are only 2 states Illinois and Georiga that are Lower then the **US National Benchmark**, While only having data for select states we see that the other 10 states in our **nonbiased** dataset are higher then the US Benchmark.

A more detailed synopsis of our findings can be found in the provided slide deck:
https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/Project%202%20Housing%20Price.pdf

## A link to the Dashboard can be found below:
https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/streamlit_dashboard.py

# Appendix
![alt="NONbiased_ny_prophet_prediction"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/NONbiased_ny_prophet_prediction.png?raw=true)
![alt="all_states"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/all_states_index.png?raw=true)
![alt="biased__ada"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/biased__ada.png?raw=true)
![alt="biased__ada_classification_report"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/biased__ada_classification_report.png?raw=true)
![alt="biased__decision_tree"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/biased__decision_tree.png?raw=true)
![alt="biased__lr_classification_report"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/biased__lr_classification_report.png?raw=true)
![alt="biased_mortgage15_forecast"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/biased_mortgage15_forecast.png?raw=true)
![alt="biased_mortgage30_forecast"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/biased_mortgage30_forecast.png?raw=true)
![alt="biased_ny_forecast"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/biased_ny_forecast.png?raw=true)
![alt="biased_ny_prophet_prediction"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/biased_ny_prophet_prediction.png?raw=true)
![alt="biased_passive_aggressive_classification"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/biased_passive_aggressive_classification_report.png?raw=true)
![alt="biased_passive_aggressive_train_test_scores"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/biased_passive_aggressive_train_test_scores.png?raw=true)
![alt="biased_usa_forecast"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/biased_usa_forecast.png?raw=true)
![alt="biased_usa_prophet_prediction"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/biased_usa_prophet_prediction.png?raw=true)
![alt="ca_vs_us_index"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/ca_vs_us_index.png?raw=true)
![alt="data_cleaning"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/data_cleaning.png?raw=true)
![alt="fbprophet"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/fbprophet.png?raw=true)
![alt="georgia_vs_us_index"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/georgia_vs_us_index.png?raw=true)
![alt="housingmarket_mortgagerates_wordcloud"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/housingmarket_mortgagerates_wordcloud.png?raw=true)
![alt="keras-tensorflow"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/keras-tensorflow.jpg?raw=true)
![alt="linear_sequence_15year"]([https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/keras-tensorflow.jpg?raw=true](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/linear_sequence_15year.png?raw=true))
![alt="linear_sequence_30year"]([images/linear_sequence_30year.PNG](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/linear_sequence_30year.png?raw=true))
![alt="logistic_regression_twitter_sentiment"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/logistic_regression_twitter%20sentiment.png?raw=true)
![alt="more_expensie_than_us_index"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/more_expensie_than_us_index.png?raw=true)
![alt="naive_bayes_complementNB_twitter_sentiment"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/naive_bayes_complementNB_twitter%20sentiment.png?raw=true)
![alt="naive_bayes_multinominalNB_twitter_sentiment"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/naive_bayes_multinominalNB_twitter%20sentiment.png?raw=true)
![alt="nltk"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/nltk.png?raw=true)
![alt="non_biased_passive_aggressive_classification_report"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/non_biased_passive_aggressive_classification_report.png?raw=true)
![alt="non_biased_passive_aggressive_train_test_scores"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/non_biased_passive_aggressive_train_test_scores.png?raw=true)
![alt="nonbiased__ada"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/nonbiased__ada.png?raw=true)
![alt="nonbiased__ada_classification_report"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/nonbiased__ada_classification_report.png?raw=true)
![alt="nonbiased__decision_tree"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/nonbiased__decision_tree.png?raw=true)
![alt="nonbiased__lr_classification_report"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/nonbiased__lr_classification_report.png?raw=true)
![alt="nonbiased_mortgage15_forecast"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/nonbiased_mortgage15_forecast.png?raw=true)
![alt="nonbiased_mortgage30_forecast"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/nonbiased_mortgage30_forecast.png?raw=true)
![alt="nonbiased_ny_forecast"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/nonbiased_ny_forecast.png?raw=true)
![alt="nonbiased_svm"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/nonbiased_svm.png?raw=true)
![alt="nonbiased_svm_classification_report"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/nonbiased_svm_classification_report.png?raw=true)
![alt="nonbiased_usa_forecast"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/nonbiased_usa_forecast.png?raw=true)
![alt="ny_vs_us_index"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/ny_vs_us_index.png?raw=true)
![alt="prophet"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/prophet.png?raw=true)
![alt="sentiment_analysis_piechart"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/sentiment_analysis_piechart.png?raw=true)
![alt="sklearn"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/sklearn.png?raw=true)
![alt="stock_houses"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/stock_houses.jpg?raw=true)
![alt="usa_index_forecast"](https://github.com/RichieGarafola/Project2_Housing_Price_Sentiment_Advisor/blob/main/Project%202/images/usa_index_forecast.png?raw=true)
    
    
