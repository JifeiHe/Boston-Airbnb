#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 15:30:11 2017

@author: jifeihe
"""
import graphlab
import numpy as np
import pandas as pd


reviews = graphlab.SFrame("reviews.csv")
listings = graphlab.SFrame("listings.csv")


columns_to_keep = ["description", "review_scores_rating"]

listings = listings[columns_to_keep]

print listings.head()
listings['word_count'] = graphlab.text_analytics.count_words(listings['description'])
print listings.head()
graphlab.canvas.set_target('ipynb')

print len(listings)
listings['sentiment'] = listings['review_scores_rating']>=90
listings=listings.dropna()
print listings.head()

train_data,test_data = listings.random_split(.8, seed=0)
sentiment_model = graphlab.logistic_classifier.create(train_data,
                                                     target='sentiment',
                                                     features=['word_count'],
                                                     validation_set=test_data)

#Evaluate the sentiment model
sentiment_model.evaluate(test_data, metric='roc_curve')
sentiment_model.show(view='Evaluation')
#Applying the learned model to understand sentiment for description
listings['predicted_sentiment'] = sentiment_model.predict(listings, output_type='probability')
print listings.head()

listings = listings.sort('predicted_sentiment', ascending=False)
print listings.head()

##Most positive description
print listings[0]['description']

##Show most negative description
print listings[-1]['description']
