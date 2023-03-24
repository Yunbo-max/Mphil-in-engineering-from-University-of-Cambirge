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

data1=pd.DataFrame({'Name':Goods_list,'Score':Score_list})

res = data1.sort_values(by='Score', ascending=False)

print(res)