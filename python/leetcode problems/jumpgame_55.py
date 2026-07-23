def jumpgame(steps:list[int]) -> bool:
    farthest = 0
    for i in range(len(steps)):
        if i>farthest:
            return False
        farthest = max(farthest, i+steps[i])
    return True

    

print(jumpgame([2,5,0,0]))