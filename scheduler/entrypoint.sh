#!/bin/sh
# Start cron in foreground
cron && tail -f /var/log/job.log