def binary(lower, upper, target):
	print(lower, upper, target)

	if lower >= upper:
		return

	mid = int((lower + upper) / 2)
	if target == mid:
		print(mid)
		return
	elif target < mid:
		binary(lower, mid - 1, target)
	else:
		binary(mid + 1, upper, target)

binary(1, 100, 100)
