import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.markdown("---")
st.header("1. Menampilkan Teks")
st.markdown("""
```python
import streamlit as st

st.write("Ini adalah teks sederhana.")
st.write("Anda bisa menggunakan *Markdown* untuk format teks.")
```
""")

st.write("Ini adalah teks sederhana.")
st.write("Anda bisa menggunakan *Markdown* untuk format teks.")
st.markdown("---")

st.header("2. Menampilkan Angka")
st.markdown("""
```python
number = 42
st.write("Angka favorit saya adalah", number)
```
""")

number = 42
st.write("Angka favorit saya adalah", number)

st.markdown("---")

st.header("3. Menampilkan DataFrame")
st.markdown("""
```python
import pandas as pd

data = {
    'Kolom A': [1, 2, 3],
    'Kolom B': [4, 5, 6]
}
df = pd.DataFrame(data)
st.write("Ini adalah DataFrame:", df)
```
""")



data = {
    'Kolom A': [1, 2, 3],
    'Kolom B': [4, 5, 6]
}
df = pd.DataFrame(data)
st.write("Ini adalah DataFrame:", df)

st.markdown("---")

st.header("4. Menampilkan Grafik Matplotlib")
st.markdown("""
```python
import matplotlib.pyplot as plt
import numpy as np

# Buat data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Buat grafik
fig, ax = plt.subplots()
ax.plot(x, y)

# Tampilkan grafik dengan st.write()
st.write(fig)
```
""")

# Buat data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Buat grafik
fig, ax = plt.subplots()
ax.plot(x, y)

# Tampilkan grafik dengan st.write()
st.write(fig)

st.markdown("---")

st.header("5. Menampilkan Gambar")
st.markdown("""
```python
st.write("![](https://seeklogo.com/images/S/streamlit-logo-1A3B208AE4-seeklogo.com.png)")
```
""")

st.write("![](https://seeklogo.com/images/S/streamlit-logo-1A3B208AE4-seeklogo.com.png)")

st.markdown("---")

st.header("6. Menampilkan Objek Python Lainnya")
st.markdown("""
```python
# Menampilkan dictionary
dict_data = {"key1": "value1", "key2": "value2"}
st.write("Ini adalah dictionary:", dict_data)

# Menampilkan list
list_data = ["item1", "item2", "item3"]
st.write("Ini adalah list:", list_data)
```
""")

# Menampilkan dictionary
dict_data = {"key1": "value1", "key2": "value2"}
st.write("Ini adalah dictionary:", dict_data)

# Menampilkan list
list_data = ["item1", "item2", "item3"]
st.write("Ini adalah list:", list_data)

st.markdown("---")

st.header("7. Menampilkan Visualisas Interaktif Plotly")
st.markdown("""
```python
import plotly.express as px
import numpy as np
            
# Visualisasi data
df = px.data.gapminder().query("year == 2007")
fig = px.treemap(df, path=[px.Constant("world"), 'continent', 'country'], values='pop',
                  color='lifeExp', hover_data=['iso_alpha'],
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(df['lifeExp'], weights=df['pop']))
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
            
# Menampilkan hasil visualisasi
st.write(fig)
```
""")

import plotly.express as px
import numpy as np
df = px.data.gapminder().query("year == 2007")
fig = px.treemap(df, path=[px.Constant("world"), 'continent', 'country'], values='pop',
                  color='lifeExp', hover_data=['iso_alpha'],
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(df['lifeExp'], weights=df['pop']))
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
st.write(fig)