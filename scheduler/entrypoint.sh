#!/bin/sh
# Start cron in foreground
touch /var/log/job.log
cron
tail -f /var/log/job.log
