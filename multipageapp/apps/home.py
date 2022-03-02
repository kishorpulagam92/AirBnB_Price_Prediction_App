import streamlit as st
import pandas as pd
from sklearn import datasets

# def app():
#     st.title('Home')

#     st.write('This is the `home page` of this multi-page app.')

#     st.write('In this app, we will be building a simple classification model using the Iris dataset.')


def app():
    st.title('Home')

    st.write('In this app, we will be building a simple classification model using the Iris dataset.')

    st.write("This is the `Data` page of the multi-page app.")

    st.write("The following is the DataFrame of the `iris` dataset.")

    iris = datasets.load_iris()
    X = pd.DataFrame(iris.data, columns = iris.feature_names)
    Y = pd.Series(iris.target, name = 'class')
    df = pd.concat([X,Y], axis=1)
    df['class'] = df['class'].map({0:"setosa", 1:"versicolor", 2:"virginica"})

    st.write(df)