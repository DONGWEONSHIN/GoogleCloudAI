# Python : 3.9.18
# Numpy : 1.26.0
# Pandas : 2.1.1
# Matplotlib : 3.7.2
# Seaborn : 0.12.2
# Scikit-learn : 1.3.0
# Created: OCT. 18. 2023
# Author: D.W. SHIN
# factCheck py file version

import platform
import os
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

sysOS = platform.system()

if sysOS == 'Windows':
    # Windows 일 경우
    plt.rcParams['font.family'] ='Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] = False
elif sysOS == 'Darwin':
    # Mac일 경우
    plt.rcParams['font.family'] ='AppleGothic'
    plt.rcParams['axes.unicode_minus'] = False
else:
    print('Please check your Korean font!!')
    os.system('sudo apt-get install -y fonts-nanum')
    os.system('sudo fc-cache -fv')
    os.system('rm ~/.cache/matplotlib -rf')
    print('#' * 30)
    print('#' * 30)
    print('런타임을 다시 시작해 주세요~~~')
    print('#' * 30)
    print('#' * 30)


# %%
try:
    sysOS
except NameError:
    import platform
    import pandas as pd
    import matplotlib.pyplot as plt
    # %matplotlib inline
else:
    print("Keep going~!")

sysOS = platform.system()

cvsPath =''

if sysOS == 'Linux':
    plt.rc('font', family='NanumBarunGothic')
    from google.colab import drive
    drive.mount('/content/drive')
    cvsPath = '/content/drive/MyDrive/구글클라우드인공지능개발자과정1기/데이터분석_미니프로젝트/Industry_Employed_Immigrants_10th_20231018150816.csv'
else:
    # ipython 과 python 의 상대 경로가 다름!!
    print(os.getcwd())
    # cvsPath = '../data/Industry_Employed_Immigrants_10th_20231018150816.csv'
    cvsPath = 'project/mini_project/data/Industry_Employed_Immigrants_10th_20231018150816.csv'

df1 = pd.read_csv(cvsPath, encoding='euc-kr', header=[0,1], skipinitialspace=True)

# %%
df1.info()

# %%
df1.head()

# %%
# Multi Header 선택하기
df1[("2017", "합계 (천명)")]

# %%
# 한번 더 복습~!
df1[("2017", "농림어업 (천명)")]

# %%
df1.loc[3, :]

# %%
ps = df1.iloc[3, :]

# %%
ps.info()

# %%
df2 = pd.DataFrame(ps)
df2

# %%
df2.info()

# %%
df2.index

# %%
df2.columns

# %%
df2.drop(
    [("대상별(1)", "대상별(1)"), ("특성별(1)", "특성별(1)"), ("특성별(2)", "특성별(2)")],
    axis=0,
    inplace=True,
)

# %%
df2.head(10)

# %%
df2.info()

# %%
df2 = df2.reset_index()

# %%
df2.head()

# %%
df2.columns = ["연도", "목록", "외국인근로총합계"]

# %%
# df2['외국인근로총합계'].astype(float)
df2["외국인근로총합계"] = pd.to_numeric(df2["외국인근로총합계"], errors="coerce")

# %%
df2.info()

# %%
df2.head()

# %%
pivot_df = df2.pivot(index="연도", columns="목록", values="외국인근로총합계")
pivot_df

# %%
pivot_df = pivot_df.reset_index()

# %%
pivot_df.index

# %%
pivot_df.columns

# %%
chart_base = pivot_df.drop("- 제조업 (천명)", axis=1)
chart_base

# %%
ps2 = pivot_df["합계 (천명)"]
chart2 = pd.DataFrame(ps2)
chart2

# %%
chart_base["total"] = chart_base.iloc[:, 1:7].sum(axis=1)

# %%
chart_base["건설업 (천명)P"] = round(
    chart_base["건설업 (천명)"] / chart_base["total"] * 100, 2)
chart_base["광업·제조업 (천명)P"] = round(
    chart_base["광업·제조업 (천명)"] / chart_base["total"] * 100, 2
)
chart_base["농림어업 (천명)P"] = round(
    chart_base["농림어업 (천명)"] / chart_base["total"] * 100, 2)
chart_base["도소매·음식·숙박 (천명)P"] = round(
    chart_base["도소매·음식·숙박 (천명)"] / chart_base["total"] * 100, 2
)
chart_base["사업·개인·공공서비스 (천명)P"] = round(
    chart_base["사업·개인·공공서비스 (천명)"] / chart_base["total"] * 100, 2
)
chart_base["전기·운수·통신·금융 (천명)P"] = round(
    chart_base["전기·운수·통신·금융 (천명)"] / chart_base["total"] * 100, 2
)

# %%
chart_base

# %%
chart_base["total_p"] = chart_base.iloc[:, 9:15].sum(axis=1)

# %%
chart_base

# %%
chart_base.head()

# %%
my_df = chart_base.iloc[:, [0, 9, 10, 11, 12, 13, 14]]

my_df.set_index(my_df["연도"], inplace=True)

my_df.drop("연도", axis=1)

# %%
plt.figure(figsize=(7, 7))

my_df.plot(kind="bar", stacked=True)

plt.xlabel("연도", fontsize=10)
plt.ylabel("목록", fontsize=10)

plt.legend(loc="upper right", bbox_to_anchor=(1.5, 1.0))
plt.show()


