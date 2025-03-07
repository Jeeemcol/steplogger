import logging
import os

class StepLogger:
    '''Handles step-based logging with auto-incrementing step numbers.'''
    
    _log_files_in_use = set()  # Track log files already assigned

    def __init__(self, filename, log_level=logging.INFO, log_format=None):
        '''
        Initializes the StepLogger.

        Parameters:
            filename (str): The log file path.
            log_level (int): Logging level (default: logging.INFO).
            log_format (str): Custom logging format. 
                Defaults to '%(asctime)s - %(levelname)s - %(message)s'.
        '''
        # Prevent multiple loggers from writing to the same file
        if filename in StepLogger._log_files_in_use:
            raise RuntimeError(f"Log file '{filename}' is already in use by another StepLogger instance.")

        self.logger = logging.getLogger(f"{__name__}.{os.path.basename(filename)}")
        self.logger.setLevel(log_level)

        if log_format is None:
            log_format = '%(asctime)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(log_format)

        # File handler for writing to a log file with error handling.
        try:
            file_handler = logging.FileHandler(filename)
            file_handler.setLevel(log_level)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
            StepLogger._log_files_in_use.add(filename)  # Mark file as in use
        except Exception as e:
            self.logger.error("Error setting up file handler: %s", e)

        # Stream handler for console output.
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        self.i = 0

    def reset_step_num(self):
        '''Resets the step counter to 0.'''
        self.i = 0

    def step(self, msg):
        '''Logs the current step and increments the step counter.'''
        self.i += 1
        self.logger.info("..... STEP %d: %s", self.i, msg)
