# Script to fire notificationto system once it run indicating Battery percentage

from plyer import notification
import psutil

battery = psutil.sensors_battery()
percentage = battery.percent
print(percentage)
notification.notify(title="Battery Percentage", message=(str(
    percentage)+"%Percent Remaining"))
