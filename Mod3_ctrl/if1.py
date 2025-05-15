def isQrty(x,y):
    if x > 0 and y > 0:
        return "First quarter"
    elif x > 0 and y < 0:
        return "The fourth quarter"
    elif (y > 0):
        return "The second quarter"
    else:
        return "The third quarter"


if __name__ == "__main__":
	x = 2
	y = 5
	print(isQrty(x,y))