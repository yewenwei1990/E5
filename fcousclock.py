import time

def focus_timer(minutes):
    seconds = minutes * 60
    print("Focus timer started.")

    while seconds > 0:
        minutes, sec = divmod(seconds, 60)
        print(f"{minutes:02d}:{sec:02d}", end="\r")
        time.sleep(1)
        seconds -= 1

    print("Focus timer ended. Time to take a break!")

# 设置专注时长为 25 分钟，即 Pomodoro Technique 的一个时间段
focus_timer(25)
