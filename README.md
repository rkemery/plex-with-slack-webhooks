# Plex to Slack Notification Service

This Python script provides a bridge between Plex's webhook feature and Slack's incoming webhooks. When certain events occur in Plex (like media playback, pausing, etc.), a notification is sent to a specified Slack channel.

For more details on Plex's webhook feature, refer to their [official documentation](https://support.plex.tv/articles/115002267687-webhooks/).

## Prerequisites

- Python 3
- pip3
- A Plex server with webhooks enabled
- A Slack workspace with incoming webhooks enabled

## Installation

### 1. Install Python 3 and pip3

#### On Ubuntu/Debian:

\```
sudo apt update
sudo apt install python3 python3-pip
\```

#### On CentOS:

\```
sudo yum install python3 python3-pip
\```

### 2. Clone the Repository

\```
git clone https://github.com/YOUR_GITHUB_USERNAME/plex-to-slack.git
cd plex-to-slack
\```

Replace `YOUR_GITHUB_USERNAME` with your actual GitHub username.

### 3. Install Required Libraries

\```
pip3 install flask requests
\```

### 4. Configure the Script

Edit the script to set your Slack incoming webhook URL:

\```python
SLACK_WEBHOOK_URL = 'YOUR_SLACK_WEBHOOK_URL'
\```

### 5. Run the Script

\```
python3 your_script_name.py
\```

## Setting up as a Systemd Service

1. Create a service file:

\```
sudo nano /etc/systemd/system/plex_to_slack.service
\```

2. Add the following content to the service file:

\```
[Unit]
Description=Plex to Slack Notification Service
After=network.target

[Service]
Type=simple
User=YOUR_USERNAME
WorkingDirectory=/path/to/script/directory
ExecStart=/usr/bin/python3 /path/to/your/script.py
Restart=always

[Install]
WantedBy=multi-user.target
\```

Replace `YOUR_USERNAME` with your Linux username and adjust the paths accordingly.

3. Reload `systemd` and start the service:

\```
sudo systemctl daemon-reload
sudo systemctl start plex_to_slack
\```

4. To make the service start on boot:

\```
sudo systemctl enable plex_to_slack
\```

## Debugging and Verbose Mode

To run the script in verbose mode and see detailed logs, use the `-verbose` flag:

\```
python3 your_script_name.py -verbose
\```

## License

This project is licensed under the MIT License and is free open source software.
