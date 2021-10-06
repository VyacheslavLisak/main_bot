import asyncio
import logging
import logging.config
from os import path

import discord

import bot_token
import hello_messages
from embedded_messages import embedded_messages_templates

LOGGING_CONFIG = path.join(path.dirname(path.abspath(__file__)), 'logger.conf') 
logging.config.fileConfig(LOGGING_CONFIG)
logger = logging.getLogger("mainBot")
logger.info('-------------------------------------------------------------')
logger.info("Bot has been started")

# Server
pupki = None

# Channels
chatik = None
ownersChannel = None
botSpam = None
botMusic = None
news = None
msgFromBot = None
new_world_new = None

# Admins
vlad = None
slava = None

# Bots
roleBot = None

# Roles
new_world_role = None

# Discord client object
client = discord.Client()


@client.event
async def on_ready():
    
    # Global variables
    global pupki
    global chatik
    global ownersChannel
    global botSpam
    global botMusic
    global news
    global vlad
    global slava
    global roleBot
    global msgFromBot
    global new_world_new
    global new_world_role

    # Set server by ID
    pupki = client.get_guild(392581230891106306)

    # Set channels
    chatik = client.get_channel(392581231407267841)
    ownersChannel = client.get_channel(834936205119717397)
    botSpam = client.get_channel(836351762398052382)
    botMusic = client.get_channel(403992935441498122)
    news = client.get_channel(405447650062893056)
    msgFromBot = client.get_channel(845006038884810763)
    new_world_new = client.get_channel(895417275182645288)

    # Set server admins
    slava = client.get_user(225667885240942592)
    vlad = client.get_user(315531935218794497)

    # Set roles
    new_world_role = pupki.get_role(895020890352390234)

    # Set bots
    roleBot = client.get_user(587562930892046338)

    # Information about bot
    logger.info('Logged in as:    ' + client.user.name)
    logger.info('On server:       ' + pupki.name)


@client.event
async def on_raw_reaction_add(payload):

    # User added reaction to rules message -> give access to the server
    if payload.channel_id == new_world_new.id:
        user = await pupki.fetch_member(payload.user_id)
        logger.info(
            'Reaction has been added by ' 
            + user.name + '#' + user.discriminator)
        try:
            await user.add_roles(new_world_role)
            logger.info(
                'Access was granted to ' 
                + user.name + '#' + user.discriminator)
            logger.info(
                '------------------------------------------------------------')
        except:
            logger.error(
                "Access wasn't granted to " 
                + user.name + '#' + user.discriminator)
            logger.info(
                '------------------------------------------------------------')
        return


@client.event
async def on_raw_reaction_remove(payload):

    # User removed reaction from rules message -> revoke access to the server
    if payload.channel_id == new_world_new.id:
        user = await pupki.fetch_member(payload.user_id)
        logger.info(
            'Reaction has been deleted by ' 
            + user.name + '#' + user.discriminator)
        try:
            await user.remove_roles(new_world_role)
            logger.info(
                'Access was canceled to ' 
                + user.name + '#' + user.discriminator)
            logger.info(
                '------------------------------------------------------------')
        except:
            logger.error(
                "Access wasn't canceled to" 
                + user.name + '#' + user.discriminator)
            logger.info(
                '------------------------------------------------------------')
        return


@client.event
async def on_message(message):

    # If sender == bot -> do nothing
    if message.author == client.user:
        return

    if message.channel == chatik:
        # Respond to hello message
        if hello_messages.helloList.count(message.content) == 1:
            await message.channel.send('<:KonCha:471065550089355289>')
            return

        # Respond to :AYAA: emoji
        if message.content == '<:AYAA:478802282960519170>':
            await message.channel.send('<:AYAYA:478803483223523341>')
            return

    # Send message via main bot
    if message.channel == msgFromBot:
        if message.content.startswith('.info'):
            info = embedded_messages_templates.set_information_embed(
                message.content.split(' ', 1)[1])
            await chatik.send(embed=info)
            return
        
        elif message.content.startswith('.notification'):
            notification = embedded_messages_templates.set_notification_embed(
                message.content.split(' ', 1)[1])
            await chatik.send(embed=notification)
            return
        
        elif message.content.startswith('.msg'):
            msg = discord.Embed()
            msg.color = 49151
            msg.description = message.content.split(' ', 1)[1]
            await chatik.send(embed=msg)
            return

    # Respond to bots' commands in general channels
    if (message.channel != botSpam and message.channel != botMusic and
            message.channel != ownersChannel and
            message.channel != msgFromBot):
        botsPrefixes = ["!", ">", ";;", "."]
        if message.content.startswith(tuple(botsPrefixes)):
            await message.channel.send(
                'Пожалуйста, не пишите бот-команды в этом канале,'
                + 'для бот-команд есть каналлы ' + botSpam.mention
                + ' и ' + botMusic.mention)
            return


# Start bot
client.run(bot_token.DISCORD_BOT_TOKEN)
