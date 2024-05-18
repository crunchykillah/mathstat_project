# Link to dataset

https://drive.google.com/file/d/1_UFh2h3RG1Q658vrkZ64ED3Fhm_yd2kD/view?usp=drive_link

# Main info about dataset

| №   | Column                                             | Non-Null Count   | Dtype   |
|-----|----------------------------------------------------|------------------|---------|
| 0   | VIN (1-10)                                         | 177866 non-null  | object  |
| 1   | County                                             | 177861 non-null  | object  |
| 2   | City                                               | 177861 non-null  | object  |
| 3   | State                                              | 177866 non-null  | object  |
| 4   | Postal Code                                        | 177861 non-null  | float64 |
| 5   | Model Year                                         | 177866 non-null  | int64   |
| 6   | Make                                               | 177866 non-null  | object  |
| 7   | Model                                              | 177866 non-null  | object  |
| 8   | Electric Vehicle Type                              | 177866 non-null  | object  |
| 9   | Clean Alternative Fuel Vehicle (CAFV) Eligibility  | 177866 non-null  | object  |
| 10  | Electric Range                                     | 177866 non-null  | int64   |
| 11  | Base MSRP                                          | 177866 non-null  | int64   |
| 12  | Legislative District                               | 177477 non-null  | float64 |
| 13  | DOL Vehicle ID                                     | 177866 non-null  | int64   |
| 14  | Vehicle Location                                   | 177857 non-null  | object  |
| 15  | Electric Utility                                   | 177861 non-null  | object  |
| 16  | 2020 Census Tract                                  | 177861 non-null  | float64 |
dtypes: float64(3), int64(4), object(10)

memory usage: 23.1+ MB


### Статистические характеристики данных:

**Средние значения:**
- Postal Code: 98,260.2
- Model Year: 2,020.517
- Electric Range: 58.827
- Base MSRP: 1,070.61
- Legislative District: 29.128
- DOL Vehicle ID: 220,252,700
- 2020 Census Tract: 53,039,810

**Дисперсия:**
- Postal Code: 92,230.64
- Model Year: 8.935
- Electric Range: 8,459.117
- Base MSRP: 69,671,080.0
- Legislative District: 221.7794
- DOL Vehicle ID: 5,753,684,000,000,000
- 2020 Census Tract: 262,548,000,000,000

**Минимальные значения:**
- Postal Code: 98,001
- Model Year: 1,997
- Electric Range: 0
- Base MSRP: 0
- Legislative District: 1
- DOL Vehicle ID: 4,385
- 2020 Census Tract: 53,001,950,000

**Максимальные значения:**
- Postal Code: 99,403
- Model Year: 2,024
- Electric Range: 337
- Base MSRP: 845,000
- Legislative District: 49
- DOL Vehicle ID: 479,254,800
- 2020 Census Tract: 53,077,940,000

### Результаты статистического анализа:

#### T-тест:
- T-значение: 0.0
- p-значение: 1.0
- Степени свободы: 177,865

**Вывод:** Нет оснований отвергнуть нулевую гипотезу.

#### Тест на нормальность (Shapiro):
- Статистика: 0.857
- p-значение: 0.0

**Вывод:** Нулевая гипотеза отвергнута.

#### Регрессионный анализ:
- Коэффициенты:
  - Для Model Year: -645.42
  - Для Electric Range: -0.18
- Свободный член (intercept): 1,305,165.10

**Выводы:** 
- Коэффициент для Model Year указывает на то, что с каждым увеличением года выпуска модели на 1, базовая цена автомобиля в среднем уменьшается на 645.42 доллара, при условии, что Electric Range остается неизменным.
- Коэффициент для Electric Range указывает на то, что с каждым увеличением электрического диапазона на 1, базовая цена автомобиля в среднем уменьшается на 0.18 доллара, при условии, что Model Year остается неизменным.
- Свободный член (или пересечение) указывает на то, что если Model Year и Electric Range оба равны нулю, то ожидаемая базовая цена автомобиля будет равна 1,305,165.10 долларов.




