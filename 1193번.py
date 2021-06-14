#이와 같이 나열된 분수들을 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
#X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.
X=int(input())
stage, key_X =1,1
while key_X +stage<=X:
    key_X += stage
    stage+=1
step =X-key_X
x, y =step+1, stage-step
if stage %2 ==0:
    print('{}/{}'.format(x,y))
else:
    print('{}/{}'.format(y,x))
