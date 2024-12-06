from datetime import datetime


def execute(self):
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"Current time is: {current_time}")

# if __name__ == "__main__":
#     run()
