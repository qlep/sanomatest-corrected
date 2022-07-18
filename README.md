# Monitor
Monitor runs in python 3 and requires modules from requirements.txt.

To execute monitor move to the project folder and run in command line:
```bash
$ python3 monitor.py pages.txt 10
```
Where "pages.txt" is a name of a file containing list of URLs and "10" is a time interval in seconds. If interval is not assigned, default time interval is 5 seconds. The conditional string to check is given in checkstring variable definition.

Logs are written in 'logs.txt'.