# steplogger
This project creates a logging process that automatically increments steps 

## How to use it

	import steplogger

	# Create the first StepLogger instance.
	logger1 = steplogger.StepLogger("test.log")
	logger1.logger.info("Beginning first process")
	logger1.step("The first step")
	logger1.step("The second step")
	logger1.logger.info("Beginning second process")
	logger1.reset_step_num()
	logger1.step("The first step")
	logger1.step("The second step")

	# Create a second StepLogger instance.
	# Won't work as can only have one handler assigned to a specific file at a time

	try:
		logger2 = steplogger.StepLogger("test.log")
		logger2.step("Message from second instance")
	except:
		print('An exception occured')

## [License]

This code is provided under the MIT License. See the  [LICENSE](https://github.com/Jeeemcol/steplogger/blob/main/LICENSE)  file for details.

## Author

-   Jeeemcol
