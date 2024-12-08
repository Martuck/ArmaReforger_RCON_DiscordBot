import discord
from discord.ext import commands, tasks
from mcrcon import MCRcon

# RCON Configuration
RCON_IP = "127.0.0.1"  # Replace with your RCON server IP
RCON_PORT = 27015      # Replace with your RCON port
RCON_PASSWORD = "your_rcon_password"

# Discord Bot Configuration
DISCORD_TOKEN = "your_discord_bot_token"
COMMAND_PREFIX = "!"
CHANNEL_ID = 123456789012345678  # Replace with your Discord channel ID

# Intents and Bot Setup
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

# State Tracking
previous_players = set()
server_online = True

# Function to send RCON commands
def send_rcon_command(command):
    try:
        with MCRcon(RCON_IP, RCON_PASSWORD, RCON_PORT) as mcr:
            response = mcr.command(command)
            return response
    except Exception as e:
        return f"Error: {str(e)}"

# Task: Monitor Server Events
@tasks.loop(seconds=30)  # Check every 30 seconds
async def monitor_server():
    """Monitor server events, player activity, and custom events."""
    global previous_players, server_online

    channel = bot.get_channel(CHANNEL_ID)
    if not channel:
        print("Channel not found.")
        return

    try:
        # Fetch players
        response = send_rcon_command("players")
        if "Error" in response:
            # Server offline alert
            if server_online:
                server_online = False
                await channel.send("⚠️ **Server is OFFLINE!**")
            return
        else:
            # Server online alert
            if not server_online:
                server_online = True
                await channel.send("✅ **Server is back ONLINE!**")

        # Parse players
        current_players = set()
        lines = response.split("\n")
        for line in lines:
            if line.strip():
                current_players.add(line.strip())

        # Player join/leave events
        joined_players = current_players - previous_players
        left_players = previous_players - current_players

        for player in joined_players:
            await channel.send(f"🟢 **{player}** has joined the server.")

        for player in left_players:
            await channel.send(f"🔴 **{player}** has left the server.")

        previous_players = current_players

        # Custom Events: Check for Admin Commands
        logs = send_rcon_command("status")
        if logs:
            for line in logs.split("\n"):
                if "admin" in line.lower() or "restart" in line.lower():
                    await channel.send(f"⚙️ **Admin Activity Detected:** {line.strip()}")

                # Custom keyword detection
                if "restart" in line.lower():
                    await channel.send("🔄 **Server is RESTARTING!**")

    except Exception as e:
        print(f"Error monitoring server: {e}")

# Command: Manually Check Server Status
@bot.command(name="status")
async def status(ctx):
    """Get the server status."""
    response = send_rcon_command("status")
    await ctx.send(f"Server Status:\n```\n{response}\n```")

# Bot Event: On Ready
@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")
    monitor_server.start()  # Start monitoring the server

# Run the Bot
bot.run(DISCORD_TOKEN)
