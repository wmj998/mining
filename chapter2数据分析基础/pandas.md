# pandas



1. ob = Series([2,3,5,7,3,1])，建立Series的时候指定索引

2. 根据下面给出信息创建Series

   ```
   dt = [1,2,3,4,5]
   
   id = ['a','b','c','d','e']
   ```

   

3. ```
   data1 = { 'subject_id': ['1', '2', '3', '4', '5'],
           'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
           'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}
   data2 = { 'subject_id': ['4', '5', '6', '7', '8'],
           'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
           'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}
   data3 = { 'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
           'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
   ```

   + 把上面3个字典分别生成为3个DataFrame，取名为df1，df2，df3，找出df3中'test_id'列的最大值
   + 把df1和df2两个DataFrame沿着X轴进行合并，命名为df12X
   + 把df1和df2两个DataFrame沿着Y轴进行合并，命名为df12Y
   + 查看df1的前三行数据

4. 创建由下所示的Dataframe，命名为data：

   ```
        Cite     year  cash
   0  Neijiang   20     6
   1  Chengdou   21     8
   2  Beijing    24     10
   ```

5. 对于上题所得到的Dataframe新增一列，列名为“book”，其值为“001，002，003”,如下所示：

   ```
       Cite     year cash  book
   0  Neijiang   20   6    001
   1  Chengdou   21   8    002
   2  Beijing    24   10   003
   ```

6. 访问上题数据框的’year’列，删除’book’列

7. 对’year’列和’cash’分别进行开方和平方的运算







