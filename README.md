# steplogger
Steplogger creates a logging process that automatically increments steps and means you don't have to manually keep track for logging where you want to break down tasks into identifiable steps.

## How to use it

	2025-03-07 15:15:20,274 - INFO - Beginning first process
	2025-03-07 15:15:20,274 - INFO - ..... STEP 1: The first step
	2025-03-07 15:15:20,274 - INFO - ..... STEP 2: The second step
	2025-03-07 15:15:20,274 - INFO - Beginning second process
	2025-03-07 15:15:20,274 - INFO - ..... STEP 1: The first step
	2025-03-07 15:15:20,274 - INFO - ..... STEP 2: The second step


This is output from the following

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
