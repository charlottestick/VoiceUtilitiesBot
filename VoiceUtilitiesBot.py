import discord
import time

client = discord.Client()

def time_print(event):
    current_time = time.ctime()
    log_text = current_time + ",            , event: " + event
    log = open("event_log.txt", "a")
    log.writelines(log_text + "\n")
    print(log_text)

first_connect = True
notificationsChannelId = 780532234394009712
notificationsChannel = None

@client.event
async def on_connect():
    time_print("connections ; started")


@client.event
async def on_ready():
    global first_connect
    global notificationsChannel

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
    notificationsChannel = client.guilds[0].get_channel(notificationsChannelId)

@client.event
async def on_voice_state_update(member, before, after):
    if (member.bot == False):
        try :
            channelName = after.channel.name
        except AttributeError:
            response = ("Goodbye, ") + str(member.display_name) + ("!")
        else:
            if (channelName != "AFK") and  (before.channel != after.channel):
                response = str(member.display_name) + (" joined the voice channel ") + str(after.channel.name) + ("!")

        log_text = ("response    ; ") + response
        time_print(log_text)
        global notificationsChannel
        await notificationsChannel.send(response)

@client.event
async def on_error():
    time_print("error       ; caught")

@client.event
async def on_disconnect():
    time_print("error       ; disconnect")

f = open("token.txt")
token = f.readline()
f.close()
client.run(token)
token = None

time_print("connections ; final close")
