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

data1=pd.DataFrame({'Name':Goods_list,'Score':Score_list})

res = data1.sort_values(by='Score', ascending=False)

print(res)