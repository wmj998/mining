import pandas as pd

ob = pd.Series([2, 3, 5, 7, 3, 1], index=['a', 'b', 'c', 'd', 'e', 'f'])
print(ob)

dt = [1, 2, 3, 4, 5]
id = ['a', 'b', 'c', 'd', 'e']
print(pd.Series(dt, id))

data_1 = {
    'subject_id': ['1', '2', '3', '4', '5'],
    'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}
data_2 = {
    'subject_id': ['4', '5', '6', '7', '8'],
    'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}
data_3 = {
    'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
    'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
df1 = pd.DataFrame(data_1)
df2 = pd.DataFrame(data_2)
df3 = pd.DataFrame(data_3)

df12x = pd.concat([df1, df2], axis=1)
df12y = pd.concat([df1, df2], axis=0)

print(df1[:3])

data = pd.DataFrame([['Neijiang', 20, 6], ['Chengdou', 21, 8], ['Beijing', 24, 10]], columns=['Cite', 'year', 'cash'])

data['book'] = ['001', '002', '003']

print(data['year'])

print(data.drop(columns='book'))

print((data['year']) ** (1 / 2))
print((data['year']) ** 2)
print((data['cash']) ** (1 / 2))
print((data['cash']) ** 2)
