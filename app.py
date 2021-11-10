#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: hamzafarooq@ MABA CLASS
"""

import streamlit as st
import pandas as pd

st.title("Final Project")
st.subheader("Abstract")


@st.cache(persist=True)
def load_data():
    df = pd.read_csv("https://datahub.io/machine-learning/iris/r/iris.csv")
    return (df)


def run():
    st.subheader("Sentiment Analysis for Text based Customer Reviews ")
    st.markdown(
        "The main idea for this project is to extract the sentiment based on some raw textual information which may include "
        "social media posts, customer reviews, new articles etc. This categorization will allow to take further action on things "
        "that may be effecting negatively in the society. For instance, if there is a lot of fake news that is surrounding it "
        "may affect people's lives in an unimaginable way."

        "This project specifically deals with categorizing the reviews as this may be a useful information to identify key "
        "issues and possibly prevent a customer churn. Categorizing the reviews to positive or negative sentiments is an outcome."
    )
    st.caption("Input:")
    st.markdown("User will present a text based review")

    st.caption("Model:")
    st.markdown(
        "Vectorizing the text data and applying Logistic Regression, K-NN, SVM to analyse the best performing model")

    st.caption("Output: ")
    st.markdown("Provides whether a review is positive or negative.")

    st.subheader("Reflection:")

    st.markdown("- Following the given instructions, everything has worked out smooth and easy.")
    st.markdown("- Deployed the streamlit app and was able to see dynamic changes reflect on the deployed app. ")
    st.markdown("- I had the opportunity to help and this has re-iterated some learnings along the way for myself.")


if __name__ == '__main__':
    run()
