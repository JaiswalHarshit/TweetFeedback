# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import schedule
import time


def func():
    exec(open("./summarize.py").read())


def scheduletask():
    schedule.every(1).minutes.do(func)
    while True:
        schedule.run_pending()
        time.sleep(1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    scheduletask()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
