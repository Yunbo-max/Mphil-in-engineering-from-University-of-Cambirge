import pandas as pd

data = pd.read_csv('men.csv')
Name = []
Score = []
Boxer_score=0
Trunk_score=0
Briefs_score=0
Thermal_score=0
G_string_score=0

Goods_list = ['Boxer','Trunk','Briefs','Thermal','G-string']
Score_list =[Boxer_score,Trunk_score,Briefs_score,Thermal_score,G_string_score]
number = 0

for i in range(len(data['Name'])):
    Name.append(data['Name'][i])

for i in range(len(data['Score'])):
    Score.append(data['Score'][i])

print(Name)
print(len(Name))

print(Score)
print(len(Score))

# for j in range(len(Name)):
#     if Name[j].count('Push')==1:
#         Push_up_score=Push_up_score+Score[j]
#         number = number+1
#
# Push_up_score = Push_up_score
# print(number)
# print(Push_up_score)
#
#
# number=0
# for j in range(len(Name)):
#     if Name[j].count('Sticky')==1:
#         Sticky_score=Sticky_score+Score[j]
#         number = number+1
#
# Sticky_score = Sticky_score
# print(number)
# print(Sticky_score)
#
#
# number=0
# for j in range(len(Name)):
#     if Name[j].count('Strapless')==1:
#         Strapless_score=Strapless_score+Score[j]
#         number = number+1
#
# Strapless_score = Strapless_score
# print(number)
# print(Strapless_score)



number=0
for t in range(len(Goods_list)):
    for j in range(len(Name)):
        if Name[j].count(Goods_list[t])==1:
            Score_list[t]=Score_list[t]+Score[j]
            number = number+1

print(number)
print(Score_list)

men=pd.DataFrame({'Name':Goods_list,'Score':Score_list})

men = men.sort_values(by='Score', ascending=False)

print(men)






import pandas as pd

data = pd.read_csv('bra.csv')
Name = []
Score = []
Push_up_score = 0
Sticky_score =0
Strapless_score = 0
Maternity_score = 0
Minimizers_score =0
Sports_score = 0
Padded_score = 0
Bandeau_score =0
Bralette_score = 0
Plunge_score = 0
Racerback_score = 0
Seamless_score =0

Goods_list = ['Push','Sticky','Strapless','Maternity','Minimizer','Sports','Padded','Bandeau','Bralette','Plunge','Racerback','Seamless']
Score_list =[Push_up_score,Sticky_score,Strapless_score,Maternity_score,Minimizers_score,Sports_score,Padded_score,Bandeau_score,Bralette_score,Plunge_score,Racerback_score,Seamless_score]
number = 0

for i in range(len(data['Name'])):
    Name.append(data['Name'][i])

for i in range(len(data['Score'])):
    Score.append(data['Score'][i])

print(Name)
print(len(Name))

print(Score)
print(len(Score))

# for j in range(len(Name)):
#     if Name[j].count('Push')==1:
#         Push_up_score=Push_up_score+Score[j]
#         number = number+1
#
# Push_up_score = Push_up_score
# print(number)
# print(Push_up_score)
#
#
# number=0
# for j in range(len(Name)):
#     if Name[j].count('Sticky')==1:
#         Sticky_score=Sticky_score+Score[j]
#         number = number+1
#
# Sticky_score = Sticky_score
# print(number)
# print(Sticky_score)
#
#
# number=0
# for j in range(len(Name)):
#     if Name[j].count('Strapless')==1:
#         Strapless_score=Strapless_score+Score[j]
#         number = number+1
#
# Strapless_score = Strapless_score
# print(number)
# print(Strapless_score)

number=0
for t in range(len(Goods_list)):
    for j in range(len(Name)):
        if Name[j].count(Goods_list[t])==1:
            Score_list[t]=Score_list[t]+Score[j]
            number = number+1

print(number)
print(Score_list)

bra=pd.DataFrame({'Name':Goods_list,'Score':Score_list})

bra = bra.sort_values(by='Score', ascending=False)





import pandas as pd

data = pd.read_csv('womenunderwear.csv')
Name = []
Score = []
Briefs_score =0
Bikini_score=0
Thong_score=0
G_string_score=0
Tangas_score=0
Hipster_score =0
Shorts_score =0


Goods_list = ['Briefs','Bikini','Thong','G-string','Tangas','Hipster','Shorts']
Score_list =[Briefs_score,Bikini_score,Thong_score,G_string_score,Tangas_score,Hipster_score,Shorts_score]
number = 0

for i in range(len(data['Name'])):
    Name.append(data['Name'][i])

for i in range(len(data['Score'])):
    Score.append(data['Score'][i])

print(Name)
print(len(Name))

print(Score)
print(len(Score))

# for j in range(len(Name)):
#     if Name[j].count('Push')==1:
#         Push_up_score=Push_up_score+Score[j]
#         number = number+1
#
# Push_up_score = Push_up_score
# print(number)
# print(Push_up_score)
#
#
# number=0
# for j in range(len(Name)):
#     if Name[j].count('Sticky')==1:
#         Sticky_score=Sticky_score+Score[j]
#         number = number+1
#
# Sticky_score = Sticky_score
# print(number)
# print(Sticky_score)
#
#
# number=0
# for j in range(len(Name)):
#     if Name[j].count('Strapless')==1:
#         Strapless_score=Strapless_score+Score[j]
#         number = number+1
#
# Strapless_score = Strapless_score
# print(number)
# print(Strapless_score)

number=0
for t in range(len(Goods_list)):
    for j in range(len(Name)):
        if Name[j].count(Goods_list[t])==1:
            Score_list[t]=Score_list[t]+Score[j]
            number = number+1

print(number)
print(Score_list)

women=pd.DataFrame({'Name':Goods_list,'Score':Score_list})

women = women.sort_values(by='Score', ascending=False)





men['Name']=['Boxer Briefs', 'Trunks', 'Briefs', 'Long Underwear', 'G-String']
women['Name'][0:5]=['Briefs', 'Hipster', 'Bikini', 'Shorts', 'Thong']
bra['Name'][:5]=['Seamless Bra', 'Padded Bra', 'Sports Bra', 'Push-up Bra', 'Strapless Bra']


men = men[:5]
women = women[:5]
bra = bra[:5]


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import MaxNLocator






import seaborn as sns
from matplotlib import pyplot as plt

fig, axes = plt.subplots(figsize=(15, 10))

# ax1 = sns.barplot(x='Name', y='Score', data = men, color='steelblue')
# ax1 = sns.barplot(x='Name',y='Score', data = men, color='steelblue',label='Men''s style ')
#
# ax1.set_xticklabels(labels = ['Boxer Briefs', 'Trunks', 'Briefs', 'Long Underwear', 'G-String'], fontsize = 16)
# ax1.set(xlabel=None)
#
# ax1.set(ylabel=None)

ax2 = sns.barplot(x='Name',y='Score', data = women, color='steelblue')
ax2.set_xticklabels(labels = ['Briefs', 'Hipster', 'Bikini', 'Shorts', 'Thong'], fontsize = 16)
ax2.set(xlabel=None)
ax2.set(ylabel=None)

# ax3 = sns.barplot(x='Name',y='Score', data = bra, color='steelblue',ax=axes[2])
# ax3.set(xlabel=None)
# ax3.set(ylabel=None)

# ax3.set_xlabel('Styles', fontsize=12, labelpad=10)

# ax1.set_ylabel('Score', fontsize=16, labelpad=10)
ax2.set_ylabel('Score', fontsize=16, labelpad=10)
# ax3.set_ylabel('Score', fontsize=12, labelpad=10)

# ax1.legend(loc="best", ncol=1, bbox_to_anchor=[1, 1.07], borderaxespad=0, frameon=False, fontsize=16)


# Create the grid
# ax1.grid(which="major", axis='x', color='#DAD8D7', alpha=0.5, zorder=1)
# ax1.grid(which="major", axis='y', color='#DAD8D7', alpha=0.5, zorder=1)


ax2.grid(which="major", axis='x', color='#DAD8D7', alpha=0.5, zorder=1)
ax2.grid(which="major", axis='y', color='#DAD8D7', alpha=0.5, zorder=1)
#
#
# ax3.grid(which="major", axis='x', color='#DAD8D7', alpha=0.5, zorder=1)
# ax3.grid(which="major", axis='y', color='#DAD8D7', alpha=0.5, zorder=1)




# Remove the spines
# ax1.spines[['top','left','bottom']].set_visible(False)
ax2.spines[['top','left','bottom']].set_visible(False)
# ax3.spines[['top','left','bottom']].set_visible(False)

# Make the left spine thicker
# ax1.spines['right'].set_linewidth(1.1)
ax2.spines['right'].set_linewidth(1.1)
# ax3.spines['right'].set_linewidth(1.1)

# Add in red line and rectangle on top
ax2.plot([0.12, .9], [.98, .98], transform=fig.transFigure, clip_on=False, color='#E3120B', linewidth=.6)
ax2.add_patch(plt.Rectangle((0.12,.98), 0.04, -0.02, facecolor='#E3120B', transform=fig.transFigure, clip_on=False, linewidth = 0))

# Add in title and subtitle
ax2.text(x=0.12, y=.93, s="Top Five Selling Styles of Women's underwear in UK", transform=fig.transFigure, ha='left', fontsize=26, weight='bold', alpha=.8)
ax2.text(x=0.12, y=.90, s="Based on Amazon sales data for women's underwear", transform=fig.transFigure, ha='left', fontsize=20, alpha=.8)

# # Set source text
# ax1.text(x=0.1, y=0.12, s="Source: Kaggle - Airlines Delay - https://www.kaggle.com/datasets/giovamata/airlinedelaycauses", transform=fig.transFigure, ha='left', fontsize=10, alpha=.7)

# Adjust the margins around the plot area
plt.subplots_adjust(left=None, bottom=0.2, right=None, top=0.85, wspace=None, hspace=None)

# Set a white background
fig.patch.set_facecolor('white')





# Colours - Choose the extreme colours of the colour map
colours = ["#2196f3", "#bbdefb"]

# Colormap - Build the colour maps
cmap = mpl.colors.LinearSegmentedColormap.from_list("colour_map", colours, N=256)
norm = mpl.colors.Normalize(men['Score'].min(), men['Score'].max()) # linearly normalizes data into the [0.0, 1.0] interval

# Plot bars
bar1 = ax2.bar(women['Name'], women['Score'], color=cmap(norm(men['Score'])), width=0.8, zorder=2)


# colours = ["#2196f3","#bbdefb"]
# # Colormap - Build the colour maps
# cmap = mpl.colors.LinearSegmentedColormap.from_list("colour_map", colours, N=256)
# norm = mpl.colors.Normalize(women['Score'].min(), women['Score'].max()) # linearly normalizes data into the [0.0, 1.0] interval
# # Plot bars
# # bar2 = ax2.bar(women['Name'], women['Score'], color=cmap(norm(women['Score'])), width=0.8, zorder=2)
#
#
# colours = ["#2196f3","#bbdefb"]
# # Colormap - Build the colour maps
# cmap = mpl.colors.LinearSegmentedColormap.from_list("colour_map", colours, N=256)
# norm = mpl.colors.Normalize(bra['Score'].min(), bra['Score'].max()) # linearly normalizes data into the [0.0, 1.0] interval
# # Plot bars
# bar3 = ax3.bar(bra['Name'], bra['Score'], color=cmap(norm(bra['Score'])), width=0.8, zorder=2)



plt.savefig("men.png",dpi=300)
plt.show()