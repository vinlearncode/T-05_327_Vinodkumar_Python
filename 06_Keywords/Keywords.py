# Keywords in Python are reserved words that can not be used as a variable name, function name, or any other identifier.

# List of all keywords in Python:-
# and	as	assert	break
# class	continue	def	del
# elif	else	except	False
# finally	for	from	global
# if	import	in	is
# lambda	None	nonlocal	not
# or	pass	raise	return
# True	try	while	with
# yield

# working of iskeyword()
# import keyword
#
# # printing all keywords at once using "kwlist()"
# print("The list of keywords is : ")
# print(keyword.kwlist)

# True, False, None
# print(False == 0)
# print(True == 1)
#
# print(True + True + True)
# print(True + False + False)
#
# print(None == None)
# print(None == 0)
# print(None == [])

# Conditional keywords – if, else, elif
# if : It is a control statement for decision making. Truth expression forces control to go in “if” statement block.
# else : It is a control statement for decision making. False expression forces control to go in “else” statement block.
# elif : It is a control statement for decision making. It is short for “else if“

# Iteration Keywords – for, while, break, continue
# for: This keyword is used to control flow and for looping.
# while: Has a similar working like “for”, used to control flow and for looping.
# break: “break” is used to control the flow of the loop. The statement is used to break out of the loop and passes the control to the statement following immediately after loop.
# continue: “continue” is also used to control the flow of code. The keyword skips the current iteration of the loop but does not end the loop.

# Return Keywords – Return, Yield
# return : This keyword is used to return from the function.
# yield : This keyword is used like return statement but is used to return a generator.

# Lambda
# Lambda keyword is used to make inline returning functions with no statements allowed internally.

# Exception Handling Keywords – try, except, raise, finally, and assert
# try : This keyword is used for exception handling, used to catch the errors in the code using the keyword except. Code in “try” block is checked, if there is any type of error, except block is executed.
# except : As explained above, this works together with “try” to catch exceptions.
# finally : No matter what is result of the “try” block, block termed “finally” is always executed.
# raise: We can raise an exception explicitly with the raise keyword
# assert: This function is used for debugging purposes. Usually used to check the correctness of code. If a statement is evaluated to be true, nothing happens, but when it is false, “AssertionError” is raised. One can also print a message with the error, separated by a comma.