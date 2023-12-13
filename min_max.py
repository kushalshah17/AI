import math

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    if curDepth == targetDepth:
        return scores[nodeIndex]
    choose_func = max if maxTurn else min
    return choose_func(
        minimax(curDepth + 1, nodeIndex * 2, not maxTurn, scores, targetDepth),
        minimax(curDepth + 1, nodeIndex * 2 + 1, not maxTurn, scores, targetDepth)
    )
scores = [3, -2, 1, 2, -3, -2, 4, 6]
treeDepth = math.log(len(scores), 2)

print("The optimal value is: ", end="")
print(minimax(0, 0, True, scores, treeDepth))
