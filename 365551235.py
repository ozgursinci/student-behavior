
import pandas as pd
from scipy.stats import ttest_ind
import statsmodels.api as sm

# Excel dosyasını yükleyin
df = pd.read_excel(r'C:\Users\Asus\Desktop\STAT365_Project\student_behavior.xlsx')


aile_evi = df[df['Where do you stay?'] == 'At home with family']


diger = df[df['Where do you stay?'] != 'At home with family']


aile_evi_female = aile_evi[aile_evi['What is your gender?'] == 'Female']

aile_evi_male = aile_evi[aile_evi['What is your gender?'] == 'Male']



diger_female = diger[diger['What is your gender?'] == 'Female']

diger_male = diger[diger['What is your gender?'] == 'Male']


aile_evi_female_AVG = aile_evi_female['I have flexible time to return home/dorm.'].mean()

aile_evi_male_AVG = aile_evi_male['I have flexible time to return home/dorm.'].mean()

diger_female_AVG = diger_female['I have flexible time to return home/dorm.'].mean()

diger_male_AVG = diger_male['I have flexible time to return home/dorm.'].mean()

# print(aile_evi_female_AVG, aile_evi_male_AVG, diger_female_AVG, diger_male_AVG)




Aile_Evi_Kadin_vs_Erkek = ttest_ind(aile_evi_female['I have flexible time to return home/dorm.'].dropna(), aile_evi_male['I have flexible time to return home/dorm.'].dropna())


print('Aile_Evi_Kadin_vs_Erkek', Aile_Evi_Kadin_vs_Erkek)




Diğer_Kadin_vs_Erkek = ttest_ind(diger_female['I have flexible time to return home/dorm.'].dropna(), diger_male['I have flexible time to return home/dorm.'].dropna())


print('Diğer_Kadin_vs_Erkek', Diğer_Kadin_vs_Erkek)


Kadin_vs_Kadin =  ttest_ind(diger_female['I have flexible time to return home/dorm.'].dropna(), aile_evi_female['I have flexible time to return home/dorm.'].dropna())

print('Kadin_vs_Kadin: ' ,Kadin_vs_Kadin)

Erkek_vs_Erkek =  ttest_ind(diger_male['I have flexible time to return home/dorm.'].dropna(), aile_evi_male['I have flexible time to return home/dorm.'].dropna())



print('Erkek_vs_Erkek: ' ,Erkek_vs_Erkek)







