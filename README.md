# slack-integrations
Custom slack integrations. Will expand over time

# notify_slack.py
1. Copy the file to your server (clone, wget, etc)
2. Set the script variables to match your server and slack info
3. set a crontab (crontab -e) for your desired frequency that calls your script. I suggest `1 */1 * * *` as rate limiting is not yet implemented
