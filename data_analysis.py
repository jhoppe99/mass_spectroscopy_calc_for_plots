import csv
import pandas as pd
import matplotlib.pyplot as plt

with open('background.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

data = data[3034:]

for n in range(0, len(data)):
    data[n] = data[n][0].split()

df = pd.DataFrame(data, columns=('mass', 'intensity'))
print(df)

for n in range(0, len(df)):
    x = df['mass'][n]
    x1 = x.replace(';', '')
    df['mass'][n] = x1

df['mass'] = df['mass'].astype(float)
df['intensity'] = df['intensity'].astype(float)
df.plot(y='intensity', x='mass', kind='line')
plt.show()

with open('dihydropiran.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

data = data[6022:]
print(data)

for n in range(0, len(data)):
    data[n] = data[n][0].split()

df2 = pd.DataFrame(data, columns=('mass', 'intensity'))

for n in range(0, len(df2)):
    x = df2['mass'][n]
    x1 = x.replace(';', '')
    df2['mass'][n] = x1

print(df2)
df2['mass'] = df2['mass'].astype(float)
df2['intensity'] = df2['intensity'].astype(float)
df2.plot(y='intensity', x='mass', kind='line')
plt.show()

'''
Drawing both characteristics on one plot
'''
plt.plot(df['mass'], df['intensity'], color='r', label='background')
plt.plot(df2['mass'], df2['intensity'], color='g', label='dihydropiran')
plt.xlabel("Mass")
plt.ylabel("Intensity")
#plt.title("Sine and Cosine functions")
plt.legend()
plt.show()
