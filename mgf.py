import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

path = '/Users/James/Desktop/200922_Robyn_adhesion_assay2_for_millz.xlsx'
df = pd.read_excel(path)

# ============ Parsing wells =============
df2 = df.set_index(['Row', 'Column'])
lst = df2.index.drop_duplicates().to_list()
s_list = sorted(lst)

# ============ Average =============
first = True
for row, column in s_list:
    df3 = df2.loc[(row, column), 'Mean green fluorescence']
    df3 = df3.to_frame()
    df4 = df3.mean().to_frame().T
    index1 = pd.Series([row])
    index2 = pd.Series([column])
    df4 = df4.set_index([index1, index2])
    if first == True :
        df5 = df4
        first = False
    else :
        df5 = df5.append(df4)

# print(df5)
# df5 = df5.reset_index()
print(df5)

# ============ Plot =============
x_axis = df5.index.get_level_values(0).drop_duplicates().to_list()
# print(x_axis)

first = True
for well in list(range(1,7)):
    y_axis_cell = df5[df5.index.get_level_values(1).isin([well])]
    y_axis_cell = y_axis_cell['Mean green fluorescence'].to_list()
    if first == True:
        wells = {well:y_axis_cell}
        first = False
    else:
        wells[well] = y_axis_cell
# print(wells)

bar_1 = wells[1]
bar_2 = wells[2]
bar_3 = wells[3]
bar_4 = wells[4]
bar_5 = wells[5]
bar_6 = wells[6]

x = np.arange(len(x_axis))
width = 0.15
# print(x - width/2)
# print(x + width/2)

plt.style.use('Solarize_Light2')

fig, ax = plt.subplots()
set1 = ax.bar(x - width*2.5, bar_1, width, label = 'col 1')
set2 = ax.bar(x - width*1.5, bar_2, width, label = 'col 2')
set3 = ax.bar(x - width/2, bar_3, width, label = 'col 3')
set4 = ax.bar(x + width/2, bar_4, width, label = 'col 4')
set5 = ax.bar(x + width*1.5, bar_5, width, label = 'col 5')
set6 = ax.bar(x + width*2.5, bar_6, width, label = 'col 6')

ax.set_ylabel('Mean green fluorescence')
ax.set_title('Avg. Mean green fluorescence')
ax.set_xticks(x)
ax.set_xticklabels(x_axis)
ax.legend()

# autolabel(set1)
# autolabel(set2)

fig.tight_layout()

plt.savefig('bar2.jpeg')

plt.show()
