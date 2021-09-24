# Accept a string and print all possible set of anagrams.
# input: below the car is a rat drinking cider and bending its elbow while this thing is an arc that can act like a cat which cried during the night caused by pain in its bowel
# output: {bowel below elbow}, {arc car}, {night thing}, {cried cider}, {act cat}

#Time complexity :O(n2k log k) in the worst case

sentence = input().split()
ans={}
for word in sentence:
    string  = "".join(sorted(word))
    # print(string)
    if string in ans:
        ans[string].append(word)
    else:
        ans[string] = [word]
# print(ans)
solution=[]
for i in ans.values():
    solution.append(i)
# print(solution)
for i in solution:
    if len(i)>1:
        print(i)
