#str='My daily routine. In the morning, I have breakfast with my family. After breakfast I feed my dogs. Then I watch a news on the Internet. After that, I take my dogs for a walk. Next, I do the gardening. Then I eat lunch with my family. After lunch, I spend some time with my girlfriend. Then we go to the park. I and my girlfriend meet our friends. Next, we go to the cafe and eat something taste. After that we return home. Next, I have afternoon tea. Then I do some work in my office. In the evening, I and my family watch TV. Before bed, I write in my diary. Finally, I go to the bed.'
str='My dream job. I do not want to work. If I have to work, I want work in IT. I want to be an information security. I want to be the best specialist. If I become an information security, I will earn a lot of money and buy a big house by the sea. I want work at home and see a sea from the window of my house. I will write different programs and drink water.'
n=0
str=str.split(' ')
for i in str:
    #if i.isalpha():

        n+=1
print(n)