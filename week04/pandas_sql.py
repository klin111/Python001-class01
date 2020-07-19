import pandas as pd 

'''
这里的df_data 就是data表所有数据，保存在一个Dataframe中
例如：

这里的df_table1 就是table1表所有数据，保存在一个Dataframe中
这里的df_table2 就是table2表所有数据，保存在一个Dataframe中
'''

df_data = pd.DataFrame({'id': [1, 2, 3, 4, 5],
                     'name': ['a', 'b', 'c', 'd','e'],
                     'age': [20, 25, 30, 35, 40]})

# SELECT * FROM data;
df_data

# SELECT * FROM data LIMIT 10;
df_data.head(10)

# SELECT id FROM data;
# 两种写法                      
df_data[['id']]


# SELECT COUNT(id) FROM data;
len(df_data.id)

# SELECT * FROM data WHERE id<1000 AND age>30;
df_data[(df_data['id'] < 1000) & (df_data['age'] > 30)]

# SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;    没有table1 数据
df_table1.groupby('id').aggregate({'order_id': 'count'})

# SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;   没有table1 and table2 数据
pd.merge(df_table1, df_table2, on='id')

# SELECT * FROM table1 UNION SELECT * FROM table2;         没有table1 and table2 数据
pd.concat([df_table1, df_table2])

# DELETE FROM table1 WHERE id=10;              没有table1 and table2 数据
df_table1[[df_table1.id != 10]                  


# ALTER TABLE table1 DROP COLUMN column_name;
df_table1.drop(['column_name'], axis=1)