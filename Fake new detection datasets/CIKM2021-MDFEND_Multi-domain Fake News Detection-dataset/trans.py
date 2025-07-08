import pandas as pd
import os

# 获取当前工作目录
cwd = os.getcwd()

# 读取pkl文件
df = pd.read_pickle(os.path.join(cwd, 'val.pkl'))
df2 = pd.read_pickle(os.path.join(cwd, 'test.pkl'))
df3 = pd.read_pickle(os.path.join(cwd, 'train.pkl'))
print(df)
print(df2)
print(df3)

# 将DataFrame保存为csv文件
df.to_csv(os.path.join(cwd, 'val.csv'), index=False, encoding='utf_8_sig')
df2.to_csv(os.path.join(cwd, 'test.csv'), index=False, encoding='utf_8_sig')
df3.to_csv(os.path.join(cwd, 'train.csv'), index=False, encoding='utf_8_sig')
