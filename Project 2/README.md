# Project-2-
# Housing Price Sentiment
_________

# Project Goal 
Create an investment tool that will allow the user to predict the trends of real estate by analyzing the increase in housing prices as it relates to the mortgage rates. The tool will analyze historical mortgage rates and look for confluence and divergence between the housing prices and mortgage rates. Using the 30yr and 15yr mortgage rates as an indicator we can predict the future outlook of the housing market. The sentiment will be gauged by using NLP to see if there is a correlation with sentiment on twitter and our predictor. We can use this tool to assess the correlations and judge if it is the right time to look for houses.

## **Our Challenge**
- The Case-Shiller Home Price Index is delivered on a monthly basis. Although our data originates in 1987, 12 data points a year is not a lot. We decided to use both forward fill to get the monthly data to be “delivered” daily so we have more data points. Also to use the non biased data sets to get the real picture. 
- Using the ***Non biased*** data gives the Group a more _REAL_ outlook on what is going on in the housing market The Case-Shiller Home Price Index only provided us with about _680 Data Points_. This was considered **low** to us. Using the Foward Fill method to fill in data in between the months we get our **biased** data

# Group Questions
1. Is there a correlation with mortgage rates and housing prices?
2. What states index is lower than the US National benchmark?
3. What states index is Higher then the US National benchmark?
4. Do we foresee a slowdown or a correction in the future?
5. What is the overall sentiment of the housing market right now?

## Data Cleaning Process 

- we gathered data through an API using _Pandas DataReader_ with the data from **FRED** or _Federal Reserve Econommic Data_. This is where we find the *Case-Shiller* monthly index. At this point we decided to use the _ffill()_ method to see if the increse in data points were needed for an outcome. 
- cleaned the Data by the normal process (ie. dropping na, removing null, column manipulation, etc.) then splitting up the data for testing and training.

## Data Analysis

- We took the cleaned data and split data to get started for **Natural Language Processing** 
  - NLP we used a few different methods here **WordCloud, Vader Sentiment Intensity Analyzer, PorterStemmer/ Lemmatizer**
- After we took a look at the sentiments on _NLP_ we started our **Machine Learning**
   - **ML** we used Naive Bayes and Logistic Regression 
   - Naive bayes (https://machinelearningmastery.com/naive-bayes-for-machine-learning/) for a better understanding of now _Naive Bayes_ works.
- Another method of **ML** is _Logistic Regression_ (https://www.ibm.com/topics/logistic-regression#:~:text=Logistic%20regression%20estimates%20the%20probability,bounded%20between%200%20and%201.)
- Lastly for our _Data Analytics_ we used **Facebook Prophet** for Machine Learning on Index and Mortgage rates: SVM, ADABoostClassifier, Decision Tree Classifier, Passive Aggressive Classifier

## Professional Subjective Opinion
Based on our findings using the ***Non-Biased (not ffill) Data Points*** we for told about a ***Market Crash*** in the coming **2023 Year**.
Our findings were based on the ***Non-Biased (not ffill) Data Points***. First we did not understand why we got this, this point we had figured it was due to insufficent data points. This is where we used the _ffill_ to get more data point but with the increase of data points we had a more _biased_ data set. With the new dataset we had a total opposite outcome.
**Mortage Rates** along with the ___Housing Prices___ have an inverse correlation as shown in the **NonBiased** data set. When __Mortgage Rates__ are high we can see that Housing prices are lower.
There are only 2 states Illinois and Georiga that are Lower then the **US National Benchmark**, While only having data for select states we see that the other 10 states in our **nonbiased** dataset are higher then the US Benchmark. Overall we group 2 see that there is going to be a correction this upcoming ***March of 2023*** 




# Appendix
![alt=""](images/NONbiased_ny_prophet_prediction.PNG)
![alt=""](images/all_states_index.PNG)
![alt=""](images/biased__ada.PNG)
![alt=""](images/biased__ada_classification_report.PNG)
![alt=""](images/biased__decision_tree.PNG)
![alt=""](images/biased__lr_classification_report.PNG)
![alt=""](images/biased_mortgage15_forecast.PNG)
![alt=""](images/biased_mortgage30_forecast.PNG)
![alt=""](images/biased_ny_forecast.PNG)
![alt=""](images/biased_ny_prophet_prediction.PNG)
![alt=""](images/biased_passive_aggressive_classification_report.PNG)
![alt=""](images/biased_passive_aggressive_train_test_scores.PNG)
![alt=""](images/biased_usa_forecast.PNG)
![alt=""](images/biased_usa_prophet_prediction.PNG)
![alt=""](images/ca_vs_us_index.PNG)
![alt=""](images/data_cleaning.PNG)
![alt=""](images/fbprophet.PNG)
![alt=""](images/georgia_vs_us_index.PNG)
![alt=""](images/housingmarket_mortgagerates_wordcloud.PNG)
![alt=""](images/keras-tensorflow.JPG)
![alt=""](images/linear_sequence_15year.PNG)
![alt=""](images/linear_sequence_30year.PNG)
![alt=""](images/logistic_regression_twitter%20sentiment.PNG)
![alt=""](images/more_expensie_than_us_index.PNG)
![alt=""](images/naive_bayes_complementNB_twitter%20sentiment.PNG)
![alt=""](images/naive_bayes_multinominalNB_twitter%20sentiment.PNG)
![alt=""](images/nltk.PNG)
![alt=""](images/non_biased_passive_aggressive_classification_report.PNG)
![alt=""](images/non_biased_passive_aggressive_train_test_scores.PNG)
![alt=""](images/nonbiased__ada.PNG)
![alt=""](images/nonbiased__ada_classification_report.PNG)
![alt=""](images/nonbiased__decision_tree.PNG)
![alt=""](images/nonbiased__lr_classification_report.PNG)
![alt=""](images/nonbiased_mortgage15_forecast.PNG)
![alt=""](images/nonbiased_mortgage30_forecast.PNG)
![alt=""](images/nonbiased_ny_forecast.PNG)
![alt=""](images/nonbiased_svm.PNG)
![alt=""](images/nonbiased_svm_classification_report.PNG)
![alt=""](images/nonbiased_usa_forecast.PNG)
![alt=""](images/ny_vs_us_index.PNG)
![alt=""](images/prophet.PNG)
![alt=""](images/sentiment_analysis_piechart.PNG)
![alt=""](images/sklearn.PNG)
![alt=""](images/stock_houses.JPG)
![alt=""](images/usa_index_forecast.PNG)
    
    
