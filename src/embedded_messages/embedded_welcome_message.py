import discord
import asyncio
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import botToken

#Channel
welcomeChannel = None

#Discord client object
client = discord.Client()

@client.event
async def on_ready():

    #Global variables
    global welcomeChannel

    #Set 'welcomeChannel' channel
    welcomeChannel = client.get_channel(587644619995480065)

    #Set embed message
    embedMessage = discord.Embed()
    embedMessage.color = 49151
    embedMessage.set_author(name="Сервер Пупки")
    embedMessage.title ="Администраторы и модераторы сервера"
    embedMessage.description = ("К этим людям можно обращаться практически по всем __вопросам и спорным моментам__.\n\n**Администраторы:**\n"
         + "<@!315531935218794497> - главный администратор и владелец данного сервера\n"
         + "<@!225667885240942592> - администратор сервера, создатель и владелец ботов\n\n"
         + "**Модераторы:**\n"
         + "<@!393369508963811328> - модератор от бога, для бога и вообще атеист\n"
         + "<@!321961105335255042> - модератор который с огромным удовольствием пошлет вас куда подальше, если обратиться к нему не по делу\n"
         + "<@!126029590362587136> - модератор-казах, ясуо-мейнер и просто сверхчеловек\n"
         + "\n\n**Роли**\n\n"
         + "Существуют 2 вида ролей, которые вы можете получить:\n"
         + "1. **Общедоступные роли** - получить такую роль может каждый. Данные роли изменяют __цвет вашего имени__ на данном сервере и появляются в списке ваших ролей\n"
         + "2. **Приватные роли** - получить можно только от владельца приватной роли. Данные роли дают доступ к __приватным комнатам__, изменяют __цвет вашего имени__ и появляются в списке ваших ролей\n"
         + "\n\n**Получение ролей**\n\n"
         + "Для получения общедоступных ролей перейдите в канал <#587554944681246730> и введите .роль или .help\n\n"
         + "Получить приватную роль можно только с согласия **владельцев** данных ролей:\n"
         + "<@&526373457320214548> - владельцы: <@!393369508963811328> и <@!311138094613266432>\n"
         + "<@&552235808891863040> - владелец: <@!126029590362587136>\n"
         + "<@&451026809761562626> - владелец: <@!321961105335255042>\n"
         + "<@&467378897819009045> - владелец: <@!225667885240942592>\n\n"
         + "Для получения информации по особым ролям необходимо написать личное сообщение <@!225667885240942592> или <@!315531935218794497>\n"
         + "\n\n**Текстовые каналы**\n"
         + "<#392581231407267841> - основной канал для общения\n"
         + "<#403992935441498122> -  канал для заказа музыки у бота (в других каналах заказать музыку не получится)\n"
         + "<#587554944681246730> -  канал для выполнения бот-команд (многие бот-команды не работают в иных каналах)\n")
    
    #Send embed message
    await welcomeChannel.send(embed=embedMessage)

#BOT TOKEN
client.run(botToken.DISCORD_BOT_TOKEN)
