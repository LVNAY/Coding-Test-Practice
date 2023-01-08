def solution(nums):
    answer = 0
    als = 0
    for i in range(0, len(nums)-2) :
        for j in range(i+1, len(nums)-1) :
            for k in range(j+1, len(nums)) :
                als = nums[i] + nums[j] + nums[k]

                for l in range(2, (int(als**0.5) + 1)):
                    count = 0
                    if als % l == 0 :
                        break
                    else :
                        count += 1
                if count > 0 :
                    answer += 1
    return answer