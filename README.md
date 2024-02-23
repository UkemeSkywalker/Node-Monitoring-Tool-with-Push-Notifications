![node monitor](./images/image.JPG)
# Node-Monitoring-Tool-with-Push-Notifications
Python application for monitoring nodes, collecting alerts, notifications, and logs, and analyzing them to provide notifications in the console.

This tool has 2 versions respectively
- [version 1.0](./v1.0/) - Original, No email alerts
- [version 1.2](./v1.2/) - Email push notifications enabled
### Implementation V1.0

```
cd v1.0
python node_monitor.py
```

### Implementation V1.2

- To activate email notifications feature, you need to signup [resend](https://resend.com/) and create an api key.

- Navigate to version directory

```
    cd ./v1.2/
```
- Then you need to install the python-dotenv  and resend package if you haven't already:

```
    pip install python-dotenv resend 
```
- Create a .env file in your project directory and add your API key and recipient email like this:

```
    RESEND_API_KEY=re_123456789
    RECIPIENT_EMAIL=example@gmail.com
```
- run the script 

```
    python node_monitor_v1.2.py 
```


![node monitor](./images/image2.JPG)
