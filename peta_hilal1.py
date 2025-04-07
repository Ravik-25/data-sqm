#CONToh perhitungan python secara manual
data = [1, 2, 3, 4, 5]
hasil = [x + 1 for x in data] #perlu di lakukan looping 
print (hasil)

#contoh implementasi pengunaa numpy
import numpy as np
data = np.array([1, 2, 3, 4, 5])
hasil = data + 5 #lansung di eksekusi 
print (hasil)

#contoh implementasi yang lain 
data = np.array([1, 2, 3, 4, 5, 16, 76, 79])
print ("Rata-rata:" ,np.mean(data))
print ("Nilai Maksimum:" ,np.max(data))
print ("Nilai Minimum:" ,np.min(data))
print ("Standart Deviasi:" ,np.std(data))

#pengunaan linspace >>> membagi data ke beberapa bagian 
data = np.linspace(0, 10, 5)
print(data)

#pengunaan library pandas
import pandas as pd
data = {"nama": ["ali", "diana", "citra"],
        "usia": [25, 30, 22],
        "kota": ["jakarta", "bandung", "surabaya"],
}
df = pd.DataFrame(data)
print (df)
df = pd.read_csv("https://github.com/Ravik-25/data-sqm.git")

### LIBRARY MATPLOTLIB ### >>>> sambunganya di file "matplotlib_visualisasi_data.py"
import matplotlib.pyplot as pt
data = {'buah': ['apel', 'jeruk', 'semangka', 'durian', 'kurma'],
        'jumlah': [23, 25, 59, 45, 55]}
df = pd.DataFrame(data)
#untuk menvisualisasikanya 
import matplotlib.pyplot as plt
plt.bar(df['buah'], df['jumlah'])
plt.xlabel('buah')
plt.ylabel('jumlah')
plt.title('jumlah buah')
plt.show()
