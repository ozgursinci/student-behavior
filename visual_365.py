
import pandas as pd
from scipy.stats import ttest_ind
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
# Excel dosyasını yükleyin
df = pd.read_excel(r'C:\Users\Asus\Desktop\STAT365_Project\student_behavior.xlsx')

# İlgili sütunları seçelim ve gruplara ayıralım
aile_evi = df[df['Where do you stay?'] == 'At home with family']
diger = df[df['Where do you stay?'] != 'At home with family']

aile_evi_female = aile_evi[aile_evi['What is your gender?'] == 'Female']
aile_evi_male = aile_evi[aile_evi['What is your gender?'] == 'Male']

diger_female = diger[diger['What is your gender?'] == 'Female']
diger_male = diger[diger['What is your gender?'] == 'Male']

# Eve dönüş saatlerindeki esneklik sütununu kontrol edelim
flexibility_column = 'I have flexible time to return home/dorm.'

# Her grubun esneklik ortalamasını hesaplayalım
averages = {
    "Women living With Family": aile_evi_female[flexibility_column].mean(),
    "Men living With Family": aile_evi_male[flexibility_column].mean(),
    "Other Women": diger_female[flexibility_column].mean(),
    "Other Men": diger_male[flexibility_column].mean()
}

# t-test için gerekli kütüphaneyi import edelim
from scipy.stats import ttest_ind

# t-testlerini yapalım
t_test_results = {
    "Aile Evi Kadın vs Erkek": ttest_ind(aile_evi_female[flexibility_column].dropna(), aile_evi_male[flexibility_column].dropna()),
    "Diğer Kadın vs Erkek": ttest_ind(diger_female[flexibility_column].dropna(), diger_male[flexibility_column].dropna())
}

averages, t_test_results


# Ortalamaları bar grafiği olarak görselleştirelim
groups = list(averages.keys())
avg_values = list(averages.values())

plt.figure(figsize=(10, 6))
sns.barplot(x=groups, y=avg_values, palette="vlag")
plt.title('Average of Returning Flexibility Hours of Home/Dormitory According to Groups')
plt.ylabel('Average Flexibility Score')
plt.xlabel('Groups')
plt.ylim(0, 5)  # Esneklik puanlarının 1 ile 5 arasında olduğunu varsayıyoruz
plt.xticks(rotation=45)
plt.show()
