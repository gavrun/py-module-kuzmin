def isQrty(x,y):
    if x > 0:
        if y > 0:     # x > 0, y > 0
            return "First quarter"
        else:         # x > 0, y < 0
            return "The fourth quarter"
    else:
        if y > 0:     # x < 0, y > 0
            return "The second quarter"
        else:         # x < 0, y < 0
            return "The third quarter"


if __name__ == "__main__":
	x = 2
	y = 4    
	print(isQrty(x,y))