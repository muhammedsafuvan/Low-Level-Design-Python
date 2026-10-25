'''
Singleton Pattern Implementation
use when you want to ensure that a class has only one instance and provide a global point of access to it.
Usecase: Implementing a logger class that ensures only one instance of the logger is created and used throughout the application using a singleton pattern.
'''
class Logger:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.log_count = 0 
        return cls.__instance

    def log(self, message: str):
        print(f"Log: {message}")
        self.log_count += 1

    def get_log_count(self) -> int:
        return self.log_count



log1 = Logger()
log1.log("First log message")
log2 = Logger()
log2.log("Second log message")

print(f"Log count from log1: {log1.get_log_count()}")
print(f"Log count from log2: {log2.get_log_count()}")