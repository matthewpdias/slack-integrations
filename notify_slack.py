#! /usr/bin/python

import subprocess
from slackclient import SlackClient

#User defined slack settings. Fix these to match your server information

slack_token = "your_token"
device_name = "/dev/xvda1" #or something like that
hostname = "your.server.com" #or your_ip
slack_channel = "your_channel"
threshold = 80 #can set to any percent

sc = SlackClient(slack_token)

percent = subprocess.check_output("df -h | grep /dev/xvda1 | awk '{print $5}'", shell=True)
percent = percent.replace('%\n', '')


if (int(percent) > threshold) :
    sc.api_call(
      "chat.postMessage",
      channel=slack_channel,
      attachments = [
         {
           "fallback": "Disk space over {}% {}".format(str(threshhold), hostname),
           "color": "#CF1318",
           "title": "Disk usage above {}% on {}".format(str(threshhold), hostname)
         }
      ]
    )
