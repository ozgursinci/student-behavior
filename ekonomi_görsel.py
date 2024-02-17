import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import ttest_ind
import statsmodels.api as sm

# Excel dosyasını yükleyin
df = pd.read_excel(r'C:\Users\Asus\Desktop\STAT365_Project\student_behavior.xlsx')


# "At home with family" ve diğerlerini ayırma
aile_evi = df[df['Where do you stay?'] == 'At home with family']
diger = df[df['Where do you stay?'] != 'At home with family']

# Harcama kategorilerinin sayısını hesaplama
aile_evi_genel = aile_evi['How much money do you spend for needs per month (without rent/dorm cost || including clothes, eating and drinking, etc)'].value_counts()
diger_genel = diger['How much money do you spend for needs per month (without rent/dorm cost || including clothes, eating and drinking, etc)'].value_counts()

# Pasta grafikleri için veri hazırlama
labels = aile_evi_genel.index
sizes_aile_evi = aile_evi_genel.values
sizes_diger = diger_genel.reindex(labels).fillna(0).values

# Pasta grafiklerini çizme
fig, axes = plt.subplots(1, 2, figsize=(14, 7))
axes[0].pie(sizes_aile_evi, labels=labels, autopct='%1.1f%%', startangle=140)
axes[0].set_title('Aile Evi ile Yaşayan Öğrencilerin Harcamaları')

axes[1].pie(sizes_diger, labels=labels, autopct='%1.1f%%', startangle=140)
axes[1].set_title('Diğer Öğrencilerin Harcamaları')

plt.tight_layout()
plt.show()
