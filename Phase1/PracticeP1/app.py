import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.header('First Deployment')
st.write('First Text')

@st.cache
def fetch_data():
    df = pd.read_csv('https://raw.githubusercontent.com/ardhiraka/PFDS_sources/master/campus.csv')
    return df

df = fetch_data()
st.write(df)

st.sidebar.header('User Input Features')
st.sidebar.write('Text in sidebar')

def user_input():
    gender = st.sidebar.selectbox('Gender', df['gender'].unique())
    ssc = st.sidebar.number_input('Secondary School Points', value=67.00)
    hsc = st.sidebar.number_input('High School Points', 0.0, value=91.0)
    hsc_s = st.sidebar.selectbox('High School Spec', df['hsc_s'].unique())
    degree_p = st.sidebar.number_input('Degree Points', 0.0, value=58.0)
    degree_t = st.sidebar.selectbox('Degree Spec', df['degree_t'].unique())
    workex = st.sidebar.selectbox('Work Experience?', df['workex'].unique())
    etest_p = st.sidebar.number_input('Etest Points', 0.0, value=78.00)
    spec = st.sidebar.selectbox('Specialization', df['specialisation'].unique())
    mba_p = st.sidebar.number_input('MBA Points', 0.0, value=54.55)

    data = {
        'gender': gender,
        'ssc_p': ssc,
        'hsc_p': hsc,
        'hsc_s': hsc_s,
        'degree_p': degree_p,
        'degree_t': degree_t,
        'workex': workex,
        'etest_p': etest_p,
        'specialisation':spec,
        'mba_p': mba_p
    }
    features = pd.DataFrame(data, index=[0])
    return features

input = user_input()

st.subheader('User Input (ini subheader) ')
st.write(input)

nama_depan = st.text_input("Nama Depan: ")
nama_belakang= st.text_input("Nama Belakang: ")
umur = st.slider("Umur: ",1,100)
kelamin = st.radio("Pilih jenis kelamin:",('Laki-laki','Perempuan'))

if st.button("Submit"):
    biodata = pd.DataFrame({'Nama Depan' : nama_depan,
                            'Nama Belakang' : nama_belakang,
                            'Usia' : umur,
                            'Jenis Kelamin' : kelamin},
                            index=[idex])

    st.write('Data Berhasil Masuk')
    st.write('Nama Depan :', nama_depan)
    st.write('Nama Belakang :', nama_belakang)
    st.write('Usia :', umur)
    st.write('Jenis Kelamin :', kelamin)
    biodata    

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


# load_model = joblib.load("my_model.pkl")

# prediction = load_model.predict(input)

# if prediction == 1:
#     prediction = 'Placed'
# else:
#     prediction = 'Not Placed'

# st.write('Based on user input, the placement model predicted: ')
# st.write(prediction)
