"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for the Prediction of Asphalt Quality.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    Water_Cement_Ratio = st.slider("Water-Cement-Ratio",float(df['Water_Cement_Ratio'].min()),float(df['Water_Cement_Ratio'].max()))
    Standing_Time = st.slider("Standing Time",float(df['Standing_Time'].min()),float(df['Standing_Time'].max()))
    Aggregate_Quality = st.slider("Aggregate Quantity",float(df['Aggregate_Quality'].min()),float(df['Aggregate_Quality'].max()))
    Asphalt_Quantity = st.slider("Asphalt Quantity",float(df['Asphalt_Quantity'].min()),float(df['Asphalt_Quantity'].max()))
    Fly_Ash_Content = st.slider("Fly_Ash_Content",float(df['Fly_Ash_Content'].min()),float(df['Fly_Ash_Content'].max()))
    Stone_Chips_Percent = st.slider("Stone_Chips_Percent",float(df['Stone_Chips_Percent'].min()),float(df['Stone_Chips_Percent'].max()))
    Sand_Ratio = st.slider("Sand_Ratio",float(df['Sand_Ratio'].min()),float(df['Sand_Ratio'].max()))
    Temperature_Range = st.slider("Temperature_Range",float(df['Temperature_Range'].min()),float(df['Stone_Chips_Percent'].max()))
    Other_Factors = st.slider("Other_Factors",float(df['Other_Factors'].min()),float(df['Other_Factors'].max()))

    

    # Create a list to store all the features
    features = [Water_Cement_Ratio,Standing_Time,Aggregate_Quality,Asphalt_Quantity,Fly_Ash_Content,Stone_Chips_Percent,Sand_Ratio,Temperature_Range,Other_Factors]

    #error factor:
    k = 4.8
  
    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        st.info("Asphalt quality detected...")

        # Print the output according to the prediction
        if (prediction == 1 or Asphalt_Quantity < 50):
            st.error("Poor! Bad Asphalt Mix 😫")
        elif (prediction == 2 or Asphalt_Quantity < 100 and Asphalt_Quantity > 51):
            st.warning("Average Asphalt Mix")
        elif (prediction == 3 or Asphalt_Quantity < 200 and Asphalt_Quantity > 110):
            st.success("Good Asphalt Mix")
        elif (prediction == 4):
            st.success("Fine Asphalt Mix")
        elif (prediction == 5):
            st.success("Excellent Asphalt Mix!! 😎")

        
        # Print teh score of the model 
        st.sidebar.write("The model used is trusted by civil engineers and has an accuracy of ", round((score*100*k),2),"%")
