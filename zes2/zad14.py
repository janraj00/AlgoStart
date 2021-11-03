
import prime


def permute_unique(nums):
    ans = [[]]
    for n in nums:
        new_ans = []
        for l in ans:
            for i in range(len(l) + 1):
                new_ans.append(l[:i] + [n] + l[i:])
                if i < len(l) and l[i] == n:
                    break  # handles duplication
        ans = new_ans
    return ans


def find_all_num(num1, num2):
    str_num1 = str(num1)
    str_num2 = str(num2)
    zeros_and_ones = [0]*len(str_num1) + [1]*len(str_num2)
    all_perm = permute_unique(zeros_and_ones)
    for perm in all_perm:
        i, j = 0, 0
        curr_res = ""
        for sign in perm:
            if sign == 0:
                curr_res += str_num1[i]
                i+=1
            else:
                curr_res += str_num2[j]
                j+=1
        curr_res = int(curr_res)
        #print(curr_res)
        if prime.prime_test(curr_res):
            print(curr_res)


if __name__ == '__main__':
    find_all_num(1234, 6789)
