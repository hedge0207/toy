import copy


# # for문 4 번 돌리는게 10배 빠르다.
def make_candi(d, i=0, lst = []):
    global all_candi

    if i==d:
        all_candi.append(copy.deepcopy(lst))
        return

    for n in range(10):
        if n in lst:
            continue
        else:
            lst.append(n)
            make_candi(d, i+1, lst)
            lst.pop()

N = 4
all_candi = []
make_candi(N)
CN = len(all_candi)

possible_candi = copy.deepcopy(all_candi)

fa = [2, 4, 6, 8]

s, b = [1, 1]


while True:
    pre_n = len(possible_candi)

    if s+b == 0:
        to_remove = []
        i = 0
        while i != len(possible_candi):
            for num in fa:
                if num in possible_candi[i]:
                    possible_candi.remove(possible_candi[i])
                    break
            else:
                i+=1
    else:
        i = 0
        while i != len(possible_candi):
            st, ba = 0, 0
            for j in range(N):
                if fa[j] == possible_candi[i][j]:
                    st += 1
                elif fa[j] in possible_candi[i]:
                    ba += 1
            
            if st!=s or ba!=b:
                possible_candi.remove(possible_candi[i])
                continue

            i += 1
    
    if pre_n == len(possible_candi):
        break

print(len(possible_candi))