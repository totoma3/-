#대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
#각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.
n=int(input())
for i in range(n):
    nums=list(map(int,input().split()))
    avg=sum(nums[1:])/nums[0]
    cnt=0
    for score in nums[1:]:
        if score >avg:
            cnt+=1
    rate =cnt/nums[0]*100
    print(f'{rate:.3f}%')
