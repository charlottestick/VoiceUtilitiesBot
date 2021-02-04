import discord
import time
import sys

client = discord.Client()

def time_print(event):
    current_time = time.ctime()
    log_text = current_time + ",            , event: " + event
    log = open("event_log.txt", "a")
    log.writelines(log_text + "\n")
    print(log_text)

first_connect = True

channels = client.get_all_channels()
for i in channels:
    print(i)
    if (i.name == "voice-channel-notifications"):
        notificationChannel = i

@client.event
async def on_connect():
	time_print("connections ; started")

@client.event
async def on_ready():
    global first_connect
    if first_connect == True:
        log_text = ("connections ; ")
        i = 0
        while i < len(client.guilds):
            if i > 0:
                log_text = log_text + (", ")
            log_text = log_text + str(client.guilds[i])
            i += 1
        time_print(log_text)
        first_connect = False
    else:
        time_print("connections ; reconnect")

@client.event
async def on_voice_state_update(member, before, after):
    if (member.bot == False):
        try :
            channelName = after.channel.name
        except AttributeError:
            response = ("Goodbye, ") + str(member.nick) + ("!")
        else:
            if (channelName != "AFK") and  (before.channel != after.channel):
                response = str(member.nick) + (" joined the voice channel ") + str(after.channel.name) + ("!")
        #notificationChannel.send(response)
        log_text = ("response    ; ") + response
        time_print(log_text)

@client.event
async def on_error():
    time_print("error       ; caught")

@client.event
async def on_disconnect():
    time_print("connections ; disconnect")
    statement = ("error       ; ") + str(sys.exc_info()[1])
    time_print(statement)

f = open("token.txt")
token = f.readline()
f.close()
client.run(token)
token = None

time_print("connections ; final close")
