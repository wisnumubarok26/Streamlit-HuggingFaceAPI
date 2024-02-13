import streamlit as st
from model import query


### Streamlit

st.header('Sentimen Analisis')
st.text('Muhamad Wisnu Mubarok')
st.title('   ')
st.text('')
input = st.text_input(label='Silahan masukan kalimat untuk di analisis',value='hello')

## code

output = query({
	"inputs": input,
})

# Mengambil nilai score tertinggi
max_score = max(output[0], key=lambda x: x['score'])

# Mengambil label dari hasil dengan score tertinggi
label = max_score['label']

if label == 'anger':
  kata = "Marah"
elif label == 'happy':
  kata = 'Senang'
elif label == 'love':
  kata = 'Menyukai'
elif label == 'sadness':
  kata = 'Sedih'
elif label == 'fear':
  kata = 'Takut'

print(kata)
st.write('Hasil : ', kata)


