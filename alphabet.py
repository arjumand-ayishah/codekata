X = input("Enter an alphabet:")
if X in ('a','e','i','o','u'):
	print("Vowel")
elif X not in ('a','e','i','o','u','!','@','#','$','%','^','&','*','(',')','-','+','/'):
	print("Consonant")
elif X in ('!','@','#','$','%','^','&','*','(',')','-','+','/'):
	print("Invalid")
