import streamlit as st
import pandas as pd
import numpy as np

# Membuat DataFrame contoh
data = pd.DataFrame({
    'Kolom A': np.random.rand(10),
    'Kolom B': np.random.rand(10),
    'Kolom C': np.random.rand(10)
})

# Menampilkan DataFrame sebagai tabel interaktif
st.dataframe(data)

import streamlit as st
import pandas as pd
import numpy as np

# Membuat DataFrame contoh
data = pd.DataFrame({
    'Kolom A': [1, 2, 3, 4, 5],
    'Kolom B': [10, 20, 30, 40, 50],
    'Kolom C': [100, 200, 300, 400, 500]
})

# Menampilkan DataFrame sebagai tabel statis
st.table(data)