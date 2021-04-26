import discord
import asyncio
import logging
import logging.config
from os import path
import botToken
import helloMessage

LOGGING_CONFIG = path.join(path.dirname(path.abspath(__file__)), 'logger.conf') 
logging.config.fileConfig(LOGGING_CONFIG)
logger = logging.getLogger("mainBot")
logger.info('-------------------------------------------------------------')
logger.info("Bot has been started")

#Server
pupki = None

#Channels
chatik = None
ownersChannel = None
botSpam = None
botMusic = None
news = None

#Admins
vlad = None
slava = None

#Bots
roleBot = None

#Discord client object
client = discord.Client()


@client.event
async def on_ready():
    
    #Global variables
    global pupki
    global chatik
    global ownersChannel
    global botSpam
    global botMusic
    global news
    global vlad
    global slava
    global roleBot

    #Set server by ID
    pupki = client.get_guild(392581230891106306)

    #Set channels
    chatik = client.get_channel(392581231407267841)
    ownersChannel = client.get_channel(834936205119717397)
    botSpam = client.get_channel(836351762398052382)
    botMusic = client.get_channel(403992935441498122)
    news = client.get_channel(405447650062893056)

    #Set server admins
    slava = client.get_user(225667885240942592)
    vlad = client.get_user(315531935218794497)

    #Set bots
    roleBot = client.get_user(587562930892046338)

    #Information about bot
    logger.info('Logged in as:    ' + client.user.name)
    logger.info('On server:       ' + pupki.name)


@client.event
async def on_message(message):

    #Global variables
    global pupki
    global chatik
    global ownersChannel
    global botSpam
    global botMusic
    global news
    global vlad
    global slava
    global roleBot

    #If sender == bot -> do nothing
    if message.author == client.user:
        return

    if message.channel == chatik:
        #Respond to hello message
        if helloMessage.helloList.count(message.content) == 1:
            await message.channel.send('<:KonCha:471065550089355289>')
            return

        #Respond to :AYAA: emoji
        if message.content == '<:AYAA:478802282960519170>':
            await message.channel.send('<:AYAYA:478803483223523341>')
            return
        
    #Respond to bots' commands in general channels
    if message.channel != botSpam and message.channel != botMusic and message.channel != ownersChannel:
        botsPrefixes = ["!", ">", ";;", "."]
        if message.content.startswith(tuple(botsPrefixes)):
            await message.channel.send('Пожалуйста, не пишите бот-команды в этом канале, для бот-команд есть каналлы ' + botSpam.mention + ' и ' + botMusic.mention)
            return

#Start bot
client.run(botToken.DISCORD_BOT_TOKEN)
