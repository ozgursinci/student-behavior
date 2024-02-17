import pandas as pd
from scipy.stats import ttest_ind
import statsmodels.api as sm

# Excel dosyasını yükleyin
df = pd.read_excel(r'C:\Users\Asus\Desktop\STAT365_Project\student_behavior.xlsx')


aile_evi = df[df['Where do you stay?'] == 'At home with family']


diger = df[df['Where do you stay?'] != 'At home with family']



aile_evi_genel = aile_evi['How much money do you spend for needs per month (without rent/dorm cost || including clothes, eating and drinking, etc)']

diger_genel = diger['How much money do you spend for needs per month (without rent/dorm cost || including clothes, eating and drinking, etc)']

#diğer
(len(diger[diger_genel == 'Less than 2500']))
(len(diger[diger_genel == '2500-5000']))
(len(diger[diger_genel == '5001-7500']))
(len(diger[diger_genel == '7501-10000']))
(len(diger[diger_genel == 'More than 10000']))


# aile evinde yaşayanlar
(len(aile_evi[aile_evi_genel == 'Less than 2500']))
(len(aile_evi[aile_evi_genel == '2500-5000']))
(len(aile_evi[aile_evi_genel == '5001-7500']))
(len(aile_evi[aile_evi_genel == '7501-10000']))
(len(aile_evi[aile_evi_genel == 'More than 10000']))

# Harcama kategorilerini sayısal değerlere dönüştüren fonksiyon
def convert_spending_to_numeric(category):
    conversion_dict = {
        'Less than 2500': 1250,  # Bu aralık için temsil edilen ortalama bir değer
        '2500-5000': 3750,       # Bu aralığın ortası
        '5001-7500': 6250,       # Bu aralığın ortası
        '7501-10000': 8750,      # Bu aralığın ortası
        'More than 10000': 11250 # Bu aralık için temsil edilen ortalama bir değer
    }
    return category.map(conversion_dict)

# Her iki gruptaki harcama kategorilerini sayısal değerlere dönüştürme
converted_aile_evi = convert_spending_to_numeric(aile_evi['How much money do you spend for needs per month (without rent/dorm cost || including clothes, eating and drinking, etc)'])
converted_diger= convert_spending_to_numeric(diger['How much money do you spend for needs per month (without rent/dorm cost || including clothes, eating and drinking, etc)'])

# T-testi uygulama
t_stat, p_value = ttest_ind(converted_aile_evi, converted_diger, equal_var=False)

print(t_stat, round(p_value,99))
