import discord
import asyncio
import botToken
import helloMessage


""" Server """
pupki = None

""" Channels """
chatik = None
botSpam = None
botMusic = None
welcome = None

""" Admins """
vlad = None
slava = None


""" Discord client object """
client = discord.Client()


@client.event
async def on_ready():
    
    """ Global variables """
    global pupki
    global chatik
    global botSpam
    global botMusic
    global welcome
    global slava
    global vlad

    """ Information about bot """
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----------')
    

    """ Information about server """
    for guild in client.guilds:
        if guild.id == 392581230891106306:
            pupki = guild
    print('Server: ' + pupki.name)
    print(pupki.id)
    print('-----------')


    """ Set '4atik' channel """
    for guild in client.guilds:
        for chat in guild.channels:
            if chat.id == 392581231407267841:
                chatik = chat
    

    """ Set 'bot_spam' channel """
    for guild in client.guilds:
        for chat in guild.channels:
            if chat.id == 587554944681246730:
                botSpam = chat


    """ Set 'bot_music' channel """
    for guild in client.guilds:
        for chat in guild.channels:
            if chat.id == 403992935441498122:
                botMusic = chat


    """ Set 'welcome' channel """
    for guild in client.guilds:
        for chat in guild.channels:
            if chat.id == 587644619995480065:
                welcome = chat


    """ Set server admins """
    for guild in client.guilds:
        for member in guild.members:
            if (member.name + member.discriminator) == 'RainbowDash8952':
                slava = member
            if (member.name + member.discriminator) == 'Магрипахарипулаевна0612':
                vlad = member


@client.event
async def on_member_join(member):

    """ Send message to new member """
    await chatik.send('Привет, ' + member.mention + ''', и добро пожаловать на сервер.
Первым делом прочти ''' + welcome.mention + ''' там указана вся необходимая информация о данном сервере.
Для получения справки по командам введи в любом из этих каналов: ''' + botSpam.mention + ' ' + botMusic.mention + ''' команду ".help"
Если есть какие-либо вопросы, обратись к ''' + slava.mention + ' или ' + vlad.mention + '\nУдачи тебе')
    return


@client.event
async def on_message(message):

    """ If sender == bot -> do nothing """
    if message.author == client.user:
        return

    if message.channel == chatik:

        """ Hello message """
        if helloMessage.helloList.count(message.content) == 1:
            await message.channel.send('<:KonCha:471065550089355289>')
            return

        """ Respond to :AYAA: emoji """
        if message.content == '<:AYAA:478802282960519170>':
            await message.channel.send('<:AYAYA:478803483223523341>')
            return


""" BOT TOKEN """
client.run(botToken.DICORD_BOT_TOKEN)