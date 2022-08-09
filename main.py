import rumps
import time
import datetime
# from pynput import keyboard

rumps.debug_mode(True)


pomodoro_minutes = 25
pomodoro_seconds = 0

long_break_minutes = 10
long_break_seconds = 0

short_break_minutes = 5
short_break_seconds = 0

time_hidden = False

m = 0
s = 0
total_seconds = m * 60 + s


def update_time(m, s):
    print("update time ")
    global total_seconds
    total_seconds = m * 60 + s


def timez():
    global total_seconds
    timer = time.strftime("%M:%S", time.gmtime(total_seconds))
    return timer


# @rumps.timer(pomodoro_timer)
def a(sender):
    global total_seconds

    print('%s %s' % (sender, timez()))
    if time_hidden:
        app.menu['Hide Time'].title = ('%s' % (timez()) + ' (hidden)')
    if not time_hidden:
        app.title = ('%s' % (timez()))
    if total_seconds == 0:
        end_timer()
    total_seconds -= 1


# @rumps.clicked('Change Timer')
# def changeit(_):
#     global pomodoro_timer
#     response = rumps.Window('Enter new interval').run()
#     if response.clicked:
#         print(int(response.text))
#         pomodoro_timer.interval = int(response.text)


def start_timer(_):
    pomodoro_timer.start()


def end_timer():
    pomodoro_timer.stop()
    app.title = "bzzz!"


@rumps.clicked('Pomodoro')
def start_pomodoro(_):
    update_time(pomodoro_minutes, pomodoro_seconds)
    start_timer(1)


@rumps.clicked('Short Pause')
def start_short_pause(_):
    update_time(short_break_minutes, short_break_seconds)
    start_timer(1)


@rumps.clicked('Long Pause')
def start_long_pause(_):
    update_time(long_break_minutes, long_break_seconds)
    start_timer(1)


@rumps.clicked('Pause Timer')
def stop_timer(_):
    print("pause timer")
    app.menu['Pause Timer'].title = "Resume Timer"
    app.menu['Pause Timer'].set_callback(resume_timer)
    pomodoro_timer.stop()


@rumps.clicked('Hide Time')
def change_timer_visibility(_):
    global time_hidden
    if not time_hidden:
        app.title = ''
    else:
        app.menu['Hide Time'].title = "Hide Time"
    time_hidden = not time_hidden

    app.menu['Hide Time'].state = not app.menu['Hide Time'].state


def resume_timer(_):
    app.menu['Pause Timer'].title = "Pause Timer"
    app.menu['Pause Timer'].set_callback(stop_timer)
    start_timer(1)


# def on_activate_p():
#     print('pomodoro')


# def on_activate_s():
#     print('short')


# def on_activate_l():
#     print('long')


if __name__ == "__main__":
    app = rumps.App('pom', menu=(  # 'Change Timer',
        'Pomodoro', 'Short Pause', 'Long Pause', 'Pause Timer', 'Hide Time'))
    pomodoro_timer = rumps.Timer(a, 1)

    app.icon = 'icon.png'
    app.run()
    # with keyboard.GlobalHotKeys({
    #     '<alt>': on_activate_p,
    #     '<alt>+s': on_activate_s,
    #     '<alt>+l': on_activate_l}) as hotkeys:
    #     hotkeys.join()
