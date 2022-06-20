# Project2_Housing_Price_Sentiment_Advisor


Housing Price Sentiment Advisor. Our tool will analyze 15 and 30 year fixed mortgage rates from FRED economic database and look for correlations with Case Shiller housing prices. The fixed mortgage rates will act as indicators to help us understand the future outlook of the housing market. The economic sentiment will be gauged using NLP. This tool will assess the correlations and judge if it is the right time to look for houses based on our predictions.

**Final Product:**
- *Dashboard*
- *Housing Price Sentiment Advisor (Lex)*

Our advisor will parse through our dictionary and answer the future outlook of each states housing prices 


**How will our tool forecast housing prices?**
- We will run a time series study using Prophet to analyze the 15 and 30 year fixed mortgage rate trend. We will also run a dynamic study on the state of the user's choice as well as the U.S. National Home Price Index. 

- Once we establish our baseline we will also use various machine learning algorithms to make predictions.
Some machine learning algorithms we will be using are: Logistic Regression, Ada Boost, Decision Tree Classifier, K-Nearest Neighbors, Random Forest, Support Vector Machine, XGBoost

- We will be using a Min-Max Scaler to view the housing prices in comparison to rates.

**How will we monitor the sentiment?**
- We will use Natural Language Processing to analyze the sentiment of the market. Particularly we will be using Vader and Word Cloud.


Our Lex Sentiment advisor will provide the user insights into our studies and our findings will be clearly depicted on a dashboard.
