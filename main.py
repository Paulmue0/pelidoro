import rumps
import time

# TODO
# + Icon should be white for dark mode
# + unhide while paused should show time
# + clicking on notification should start new timer
# + custom time
# + show in which pomodoro your're in (long break resets)


rumps.debug_mode(True)

current_mode = ''

POMODORO_MINUTES = 25
POMODORO_SECONDS = 0

LONG_BREAK_MINUTES = 15
LONG_BREAK_SECONDS = 0

SHORT_BREAK_MINUTES = 5
SHORT_BREAK_SECONDS = 0

time_hidden = False
notification_enabled = False

m = 0
s = 0
total_seconds = m * 60 + s


def update_time(m, s):
    global total_seconds
    total_seconds = m * 60 + s


def timez():
    global total_seconds
    timer = time.strftime("%M:%S", time.gmtime(total_seconds))
    return timer


# @rumps.timer(pomodoro_timer)
def a(sender):
    global total_seconds
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
    app.title = ""


def end_timer():
    pomodoro_timer.stop()
    app.title = "bzzz!"
    if notification_enabled:
        if current_mode == 'pomodoro':
            rumps.notification("bzzz!", "Time for a break :)", "")
        else:
            rumps.notification("bzzz!", "", "")


@rumps.clicked('Pomodoro', key="p")
def start_pomodoro(_):
    global current_mode
    current_mode = 'pomodoro'
    update_time(POMODORO_MINUTES, POMODORO_SECONDS)
    start_timer(1)


@rumps.clicked('Short Pause', key='s')
def start_short_pause(_):
    global current_mode
    current_mode = 'short pause'
    update_time(SHORT_BREAK_MINUTES, SHORT_BREAK_SECONDS)
    start_timer(1)


@rumps.clicked('Long Pause', key='l')
def start_long_pause(_):
    global current_mode
    current_mode = 'long pause'
    update_time(LONG_BREAK_MINUTES, LONG_BREAK_SECONDS)
    start_timer(1)


@rumps.clicked('Stop Timer', key="b")
def stop_timer(_):
    app.menu['Stop Timer'].title = "Resume Timer"
    app.menu['Stop Timer'].set_callback(resume_timer)
    pomodoro_timer.stop()


@rumps.clicked('Hide Time', key="h")
def change_timer_visibility(_):
    global time_hidden
    if not time_hidden:
        app.title = ''
    else:
        app.menu['Hide Time'].title = "Hide Time"
    time_hidden = not time_hidden

    app.menu['Hide Time'].state = not app.menu['Hide Time'].state


@rumps.clicked('Reset Timer', key="r")
def change_timer_visibility(_):
    if current_mode == "pomodoro":
        start_pomodoro(1)
    elif current_mode == "short pause":
        start_short_pause(1)
    elif current_mode == "long pause":
        start_long_pause(1)


@rumps.clicked('Notifications', key="n")
def switch_notifications(_):
    global notification_enabled
    notification_enabled = not notification_enabled
    app.menu['Notifications'].state = not app.menu['Notifications'].state


def resume_timer(_):
    app.menu['Stop Timer'].title = "Stop Timer"
    app.menu['Stop Timer'].set_callback(stop_timer)
    start_timer(1)


if __name__ == "__main__":
    app = rumps.App('pom', menu=(  # 'Change Timer',
        'Pomodoro', 'Short Pause', 'Long Pause', None, 'Hide Time', "Notifications", None, 'Stop Timer', 'Reset Timer'))
    pomodoro_timer = rumps.Timer(a, 1)

    app.icon = 'icons/icon.png'
    app.run()
