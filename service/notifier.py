from win10toast import ToastNotifier

notifier = ToastNotifier()

def notify(title, message):
    notifier.show_toast(title, message, duration=5, threaded=True)
