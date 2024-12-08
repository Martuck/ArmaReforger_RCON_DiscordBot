# Arma Reforger RCON Discord Bot

A Discord bot that connects to an **Arma Reforger server** via RCON to monitor server activity, player joins/leaves, and admin commands. It can send real-time updates to a specific Discord channel and provide server alerts, admin logs, and custom events.

---

## Features

- **Real-Time Player Monitoring**:
  - Detects player joins and disconnects.
- **Server Alerts**:
  - Alerts when the server goes offline or comes back online.
- **Admin Logs**:
  - Captures admin activities like restarts and other key RCON events.
- **Custom Event Detection**:
  - Alerts for keywords like `restart`, `admin`, or specific messages.
- **Server Status Updates**:
  - Displays the server name, map, and player count as the bot's presence in Discord.

---

## Prerequisites

Ensure you have the following:
1. **Ubuntu Server 22.04 LTS** (recommended for production use).
2. **Python 3.10 or higher** (default on Ubuntu 22.04).
3. An Arma Reforger server with **RCON enabled**.
4. A **Discord Bot Token**.
5. The **channel ID** for sending server updates.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Martuck/ArmaReforger_RCON_DiscordBot.git
cd arma-reforger-discord-bot
```

## 2. Set Up a Virtual Environment
```bash
python3 -m venv bot_env
source bot_env/bin/activate
```

## 3. Install Dependencies

Install the required Python libraries using pip3:

```bash
pip3 install -r requirements.txt
```

## 4. Configure the Bot

Open the bot.py file.
Replace the placeholders with your information:
```DISCORD_TOKEN: Your Discord bot token.```
```RCON_IP, RCON_PORT, RCON_PASSWORD: Your Arma Reforger RCON details.```
```CHANNEL_ID: The Discord channel ID where updates will be posted.```
Example snippet in bot.py:

```
DISCORD_TOKEN = "your_discord_bot_token"
RCON_IP = "your_server_ip"
RCON_PORT = 27015
RCON_PASSWORD = "your_rcon_password"
CHANNEL_ID = 123456789012345678  # Replace with your Discord channel ID
```

## Running the Bot

Start the bot using Python:

```bash
python3 bot.py
```

You should see output similar to:

```bash
Bot connected as ArmaReforgerBot#1234
```

The bot will now:

Monitor player activity and send updates to the specified Discord channel.
Update its presence with server status, map name, and player count.

## Bot Commands

You can interact with the bot using these commands in Discord:

Command	Description	Example Usage
```!status	Fetch the current server status.	!status```

Example Output

Player Joins/Leaves:
```
🟢 Player123 has joined the server.
🔴 Player456 has left the server.
```
Server Alerts:
```
⚠️ Server is OFFLINE!
✅ Server is back ONLINE!
```
Admin Logs:
```
⚙️ Admin Activity Detected: restart issued
```
Custom Events:
```
🔄 Server is RESTARTING!
```

## Running the Bot in the Background (Optional)

Use tmux or screen to keep the bot running after logging out of the server:

Using tmux:
Start a new session:
```bash
tmux new-session -s bot_session
```
Run the bot:
```bash
python3 bot.py
```
Detach from the session: Press Ctrl + B, then D.

To reattach:

```bash
tmux attach-session -t bot_session
```

## Troubleshooting

Bot not responding:
- Verify the Discord Token and Channel ID.
- Check if the bot is online in the server.

Server connection issues:
- Verify your RCON IP, port, and password.
- Ensure RCON is enabled on the Arma Reforger server.

Dependencies missing:
- Reinstall the requirements:

```bash
pip3 install -r requirements.txt
```

## Contact:
- Discord: YourDiscordName#1234
