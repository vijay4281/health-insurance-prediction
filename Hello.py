# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import pickle 
import pandas as pd
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Health Insurance Prediction",
    )

    html_temp = """
    <div style="background-color:lightblue;padding:16px;">
        <h2 style="color:black;text-align:center;">Health Insurance Cost Prediction</h2>
    </div>
    
    """

    st.markdown(html_temp, unsafe_allow_html=True)
    
    model = pickle.load(open('model_healthinsurance_gbr', 'rb'))
    
        
    p1 = st.slider("Enter Your Age",18,100)
    
    s1=st.selectbox("Sex",("Male","Female"))
    if s1=="Male":
        p2=1
    else:
        p2=0

    p3 =st.number_input("Enter Your BMI Value")
    p4 = st.slider("Enter Number of Children",0,4) 
    
    s2=st.selectbox("Smoker",("Yes","No"))
    if s2=="Yes":
        p5=1
    else:
        p5=0
        
    p6 = st.slider("Enter Your Region [1-4]",1,4)
    
    data = {
        'age': p1,
        'sex':p2,
        'bmi':p3,
        'children':p4,
        'smoker':p5,
        'region':p6
        }
    
    df = pd.DataFrame(data, index=[0])
    
    if st.button('Predict'):
        prediction = model.predict(df)
        st.snow()
        st.success('Insurance Amount is ${} '.format(round(prediction[0],2)))


if __name__ == "__main__":
    run()
