#alphabetical diamond pattern
"print an alphabetical diamond"
[print(f"{''.join(chr(x) for x in range(65 + (0, 32 + 2*(12 - i))[j], 64 + (2*i, 32)[j], (1, -1)[j])):^40}")
 for j in (0, 1) for i in range(15)]