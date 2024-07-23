import pickle
import streamlit as st

#untuk load model
model = pickle.load(open('stroke_model.sav', 'rb'))

#website

#judul
st.title('Prediksi Brain Stroke')


#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    Gender = st.selectbox('Jenis Kelamin',['Laki-Laki', 'Perempuan'])
with col1:
    Age = st.text_input('Usia')
with col1:
    Smoking = st.selectbox('Merokok', ['YES','NO'])
with col1:
    Hypertensi = st.selectbox('Hypertensi', ['YES','NO'])
with col1:
    Hyperdiease = st.selectbox('Memiliki penyakit jantung', ['YES','NO'])
with col2:
    Married = st.selectbox('Sudah menikah', ['YES','NO'])
with col2:
    Tipe_pekerjaan = st.selectbox('Jenis Pekerjaan', ['Private','Pegawai Negeri','Swasta'])
with col2:
    Residence = st.selectbox('Memiliki Tempat Tinggal', ['YES','NO'])
with col2:
    avg_glukosa = st.slider('Rata-rata Gula: mg/dL', 0,300,140)
with col2:
    bmi = st.slider('BMI (Indek Masa Tubuh)', 0,50,24)


categorical_mapping = {
    'YES' : 1, 'NO' : 0,
    'Laki-Laki' : 1, 'Perempuan' : 0,
    'Private' : 0, 'Pegawai Negeri' : 1, 'Swasta' : 2
}
# code prediksi
stroke_diagnonis = ''

#membuat tombol
if st.button('Test Prediksi Kanker Paru-Paru'):
    stroke_prediction = model.predict([[categorical_mapping[Gender],Age,categorical_mapping[Hypertensi], categorical_mapping[Hyperdiease],
                                            categorical_mapping[Married], categorical_mapping[Tipe_pekerjaan], 
                                           categorical_mapping[Residence], avg_glukosa,bmi,
                                           categorical_mapping[Smoking]]])
    if(stroke_prediction[0] == 1):
        stroke_diagnonis = 'Model memprediksi pasien kemungkinan terkena Stroke'
        st.error(stroke_diagnonis)
    else :
        stroke_diagnonis = 'Model memprediksi pasien kemungkinan tidak terkena Stroke'
        st.success(stroke_diagnonis)
    
# Footer
st.markdown("---")
footer = """
    <style>
    .footer {
        left: 0;
        bottom: 0;
        width: 100%;
        color: White;
        text-align: center;
        padding: 10px;
    }
    </style>
    <div class="footer">
        © 2024 Cronk
    </div>
"""
st.markdown(footer, unsafe_allow_html=True)
