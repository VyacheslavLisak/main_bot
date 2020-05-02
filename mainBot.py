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


""" Bots """
roleBot = None
loveBot = None


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
    global roleBot
    global loveBot

    """ Information about bot """
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----------')
    

    """ Information about server """
    pupki = client.get_guild(392581230891106306)
    print('Server: ' + pupki.name)
    print(pupki.id)
    print('-----------')


    """ Set '4atik' channel """
    chatik = client.get_channel(392581231407267841)
    

    """ Set 'bot_spam' channel """
    botSpam = client.get_channel(587554944681246730)


    """ Set 'bot_music' channel """
    botMusic = client.get_channel(403992935441498122)


    """ Set 'welcome' channel """
    welcome = client.get_channel(587644619995480065)


    """ Set server admins """
    slava = client.get_user(225667885240942592)
    vlad = client.get_user(315531935218794497)

    """ Set bots """
    roleBot = client.get_user(587562930892046338)
    loveBot = client.get_user(582161861647007745)


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
        
        if message.content == '.help':
            await message.channel.send('Пожалуйста, не пишите бот-команды в этом канале, для бот-команд есть каналлы ' + botSpam.mention + ' и ' + botMusic.mention)
            return
    

    if message.channel == botMusic:
        if message.content == '.help':
            await botMusic.send('''Этот канал предназначен для заказа музыки.
Команды для управления музыкальным ботом:

!play <Название песни/ссылка на песню в youtube> (сокращенно -!p) - заказывает музыку
!skip (сокращенно - !s) - прекращает играть текущий трек
!np - показывает какой сейчас трек играет бот 
!pause - ставит трек на паузу
!resume - снимает паузу''')
            return
    
    if message.channel == botSpam:
        if message.content == '.роль' or message.content == '.help':
            await botSpam.send ('''Используйте команду ".роль <название роли>" для получения общедоступных ролей.
Используйте команду ".удалить роль <название роли>" для удаления общедоступных ролей.

Доступные для получения/удаления роли:

Анимечъник - если вы любите аниме (нельзя получить если вы АнимуХейтер)
АнимуХейтер - если вы хейтите аниме (нельзя получить если вы Анимечъник)
Работяги - если вы считаете себя истиным работягой
АФКашник - если вы любите афкашить в дискорде
Знатоки - если вы считаете себя знатаком
Под Владиславом - специальная роль, если вы хотите оказаться под Владиславом

Для получения ролей, которые здесь не указаны - обратитесь к администраторам сервера

Пример команды для получения роли Работяги:
.роль Работяги

Пример команды для удаления роли Работяги:
.удалить роль Работяги''')
            return


""" BOT TOKEN """
client.run(botToken.DISCORD_BOT_TOKEN)
