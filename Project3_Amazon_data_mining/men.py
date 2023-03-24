import pandas as pd

data = pd.read_csv('men.csv')
Name = []
Score = []
Boxers = 0
Boxer_Brief_score=0
Trunk_score=0
Briefs_score=0
Thermal_score=0
G_string_score=0
Boxer_Shorts_score = 0

Goods_list = ['Boxer Brief','Trunk','Briefs','Thermal','string','Boxer Short']
# Goods_list = ['Trunk','Briefs','Thermal','string']
Score_list =[Boxer_Brief_score,Trunk_score,Briefs_score,Thermal_score,G_string_score,Boxer_Shorts_score]
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

Boxers_number = 0

list1 = 0

number=0
for t in range(len(Goods_list)):
    for j in range(len(Name)):
        if 'Boxer' in Name[j] and 'Boxer Brief' not in Name[j]:
            if Name[j].count(Goods_list[t]) == 1:
                Score_list[t] = Score_list[t] + Score[j]
                number = number + 1

        # elif 'Briefs' in Name[j] and 'Boxer Brief' not in Name[j]:
        #     if Name[j].count(Goods_list[t]) == 1:
        #         Score_list[t] = Score_list[t] + Score[j]
        #         number = number + 1

        elif 'Boxer Short'not in Name[j]:
            if Name[j].count(Goods_list[t])==1:
                Score_list[t]=Score_list[t]+Score[j]
                number = number+1





print(number)
print(Score_list)

men=pd.DataFrame({'Name':Goods_list,'Score':Score_list})

res = men.sort_values(by='Score', ascending=False)

print(res)









