import discord
import asyncio
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import botToken

#Channel
rulesChannel = None

#Discord client object
client = discord.Client()

@client.event
async def on_ready():
    
    #Global variables
    global pupki
    global rulesChannel

    #Set 'rulesChannel' channel
    rulesChannel = client.get_channel(834935955919208459)

    #Set embed message
    embedMessage = discord.Embed()
    embedMessage.color = 49151
    embedMessage.title ="**Правила сервера**"
    embedMessage.description = ("Перед получением доступа к серверу, пожалуйста ознакомьтесь с правилами ниже\n\n"
        + "__**Правила:**__\n\n"
        + "\u00a0\u00a0  **Пользователи могут:**\n"
        + "\u00a0\u00a0\u00a0\u00a0    1. Общаться в текстовых и голосовых каналах\n"
        + "\u00a0\u00a0\u00a0\u00a0    2. Постить картинки, видео и вести стримы в любом доступном канале/чате сервера (если нет запрещающих правил для отдельного канала)\n"
        + '\u00a0\u00a0\u00a0\u00a0    3. Размещать NSFW материалы только в профильных каналах разделах "NSFW"\n'
        + "\u00a0\u00a0\u00a0\u00a0    4. Мат разрешается, но без злоупотребления в текстовых чатах\n\n"
        + "\u00a0\u00a0  **Пользователям запрещается:**\n"
        + "\u00a0\u00a0\u00a0\u00a0    1. Запрещается реклама без согласования с администрацией\n"
        + "\u00a0\u00a0\u00a0\u00a0    2. Запрещено злоупотребление Caps Lock\n"
        + "\u00a0\u00a0\u00a0\u00a0    3. Запрещается жесткий троллинг по расовой, национальной или гендерной принадлежности\n"
        + "\u00a0\u00a0\u00a0\u00a0    4. Не допускается спам-рассылка в личных сообщениях с другими пользователям\n"
        + "\u00a0\u00a0\u00a0\u00a0    5. Запрещено использование имен с оскорблением, религиозными названиями, рекламой\n"
        + "\u00a0\u00a0\u00a0\u00a0    6. В любом канале запрещена публикация ссылок на донат-сайты, площадки приема платежей, спонсорской помощи, пожертвований и других сервисов\n\n"
        + "\u00a0\u00a0  **Ответственность:\n**"
        + "\u00a0\u00a0\u00a0\u00a0    1. При нарушении правил сервера к нарушителю принимаются меры вплоть до ограничения доступа\n"
        + "\u00a0\u00a0\u00a0\u00a0    2. Обход бана путем входа под другим идентификатором или иными путями — бан\n"
        + "\u00a0\u00a0\u00a0\u00a0    3. Администраторы и модераторы вправе отказать в доступе любому участнику. Они не обязаны указывать причины или предупреждать об этом\n"
        + "\u00a0\u00a0\u00a0\u00a0    4. Администраторы и модераторы вправе требовать изменение ника и картинки, если считает, что они оскорбляют кого-либо\n"
        + "\u00a0\u00a0\u00a0\u00a0    5. Нарушение упомянутых выше норм — бан\n\n"
        + "Если вы согласны с данными правилами  и обязуетесь им следовать - нажмите на **эмодзи** под данным сообщением для получения доступа к серверу")
    embedMessage.set_image(url='https://sun9-61.userapi.com/impg/w_bS8t2i3VvBCza-KUFFrT9PbFhY00wz87qsTw/RksbeWiZfHg.jpg?size=600x200&quality=96&sign=4a9d7b202b5e4ed521459ae2dd82d7c4&type=album')
    
    #Send embed message
    await rulesChannel.send(embed=embedMessage)

#BOT TOKEN
client.run(botToken.DISCORD_BOT_TOKEN)
