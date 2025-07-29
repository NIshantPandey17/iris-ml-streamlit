import pickle
import streamlit as st

model1=pickle.load(open("iris_data.pkl","rb"))

def mydeploy():
    st.title("Iris Flower Species Predictor"  )
    
    sepal_length= st.number_input("Enter sepal length in cm :")
    sepal_width= st.number_input("Enter sepal width in cm :")
    petal_length= st.number_input("Enter petal length  in cm :")
    petal_width= st.number_input("Enter petal width in cm :")
    
    pred=st.button("Predict species")

    if pred:
        pre = model1.predict([[sepal_length, sepal_width, petal_length,petal_width]])

        if pre[0] == 0:
            st.success("Predicted Species: Setosa")
        elif pre[0] == 1:
            st.success("Predicted Species: Versicolor")
        else:
            st.success("Predicted Species: Virginica")


 
mydeploy()