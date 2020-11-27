import discord
import time
import sys
from dotenv import load_dotenv #Needs to be installed/added to requirements

client = discord.Client()

def time_print(event):
    current_time = time.ctime()
    log_text = current_time + ",            , event: " + event
    log = open("event_log.txt", "a")
    log.writelines(log_text + "\n")
    print(log_text)

first_connect = True

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
async def on_error():
    time_print("error       ; caught")

@client.event
async def on_disconnect():
    time_print("connections ; disconnect")
    statement = ("error       ; ") + str(sys.exc_info()[1])
    time_print(statement)

load_dotenv()
token = os.getenv("TOKEN")
client.run(token)

time_print("connections ; final close")