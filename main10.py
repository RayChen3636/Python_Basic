lasttwo = 0
lastone = 0
times = 0
while times < 10:
    if times == 0:
        lasttwo = 0
        ans = 0
    elif times == 1:
        lastone = 1
        ans = 1
    else:
        ans = lasttwo + lastone
        lasttwo = lastone
        lastone = ans
    print("第",times+1,"項",ans)
    times = times+1