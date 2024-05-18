import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from sklearn.linear_model import LinearRegression


# Загрузка данных
df = pd.read_csv('Electric_Vehicle_Population_Data.csv')

numeric_columns = ['Postal Code', 'Model Year', 'Electric Range', 'Base MSRP',
                   'Legislative District', 'DOL Vehicle ID', '2020 Census Tract']

non_numeric_columns = ['VIN (1-10)', 'County', 'City', 'State', 'Make', 'Model',
                       'Electric Vehicle Type', 'Clean Alternative Fuel Vehicle (CAFV) Eligibility',
                       'Vehicle Location', 'Electric Utility']

sample = df['Model Year']

sample_small = sample.sample(n=5000, random_state=42)  # Для теста Шапиро

alpha = 0.05  # уровень значимости

# Получение основной информации о данных
print('Main info: ')
print(df.info())
print()

# Удаление столбцов с пропущенными значениями
df.dropna(inplace=True)






# 22222 #
# Для отображения всех столбцов в корреляции и квантилях
pd.set_option('display.max_columns', None)

# Вычисление основных статистических характеристик данных для числовых столбцов:
print("mean: ")
print(df[numeric_columns].mean())
print()

print("dispersion: ")
print(df[numeric_columns].var())
print()

print("min value: ")
print(df[numeric_columns].min())
print()

print("max value: ")
print(df[numeric_columns].max())
print()

print("quantiles: ")
print(df[numeric_columns].quantile([0.25, 0.5, 0.75]))
print()

print("correlation: ")
print(df[numeric_columns].corr())
print()






# 333333333333 #
# Построение гистограмм
df[numeric_columns].hist(figsize=(10, 10))
plt.show()

# Построение боксплотов (сделано через цикл,
# тк иначе будет слишком большой разброс

# Построение гистограмм с графиком функции распределения
for col in numeric_columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(df[col], kde=True)
    plt.title(f'Hist and allocation {col}')
    plt.show()

# Построение боксплотов
for col in numeric_columns:
    plt.figure(figsize=(10, 6))
    sns.boxplot(df[col])
    plt.title(col)
    plt.show()

# Построение диаграмм рассеивания
sns.pairplot(df[numeric_columns])
plt.show()




# 444444444 #
# Поиск выбросов с помощью межквартильного размаха
print('Emissions: ')
Q1 = df[numeric_columns].quantile(0.25)
Q3 = df[numeric_columns].quantile(0.75)
IQR = Q3 - Q1

# Удаление выбросов
filtered_df = df[~((df[numeric_columns] < (Q1 - 1.5 * IQR)) | (df[numeric_columns] > (Q3 + 1.5 * IQR))).any(axis=1)]

print(filtered_df)






# 555555 #
# Проверка гипотезы о среднем значении
# Нулевая гипотеза: среднее значение равно "2020.51551167733" (это mean для Model Year)
mean_hypothesis_test = stats.ttest_1samp(sample, 2020.51551167733)

print(f"t-test : {mean_hypothesis_test}" + "\n")

if mean_hypothesis_test.pvalue > alpha:
    print("there is no reason to reject the null hypothesis" + "\n")
else:
    print("null hypothesis rejected" + "\n")

# Проверка гипотезы о нормальности распределения
# Нулевая гипотеза: данные распределены нормально
normality_test = stats.shapiro(sample_small)

print(f"normality test (Shapiro): {normality_test}" + "\n")

if normality_test[1] > alpha:
    print("there is no reason to reject the null hypothesis" + "\n")
else:
    print("null hypothesis rejected" + "\n")







# 666666 #
X = df[['Model Year', 'Electric Range']]  # Признаки
y = df['Base MSRP']  # Целевая переменная

# Удаление пропущенных значений для регрессии
X = X.dropna()
y = y.dropna()

model = LinearRegression()
model.fit(X, y)

print(f'regression coefficient: {model.coef_}')
print(f'Free member (intercept): {model.intercept_}')

# Прогнозирование и визуализация
y_pred = model.predict(X)
plt.figure(figsize=(10, 6))
plt.scatter(X['Model Year'], y, color='blue')
plt.plot(X['Model Year'], y_pred, color='red')
plt.xlabel('Model Year')
plt.ylabel('Base MSRP')
plt.title('Linear Regression: Model Year vs Base MSRP')
plt.show()
