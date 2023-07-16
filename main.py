# EN: Import required modules
# RU: Импорт нужных модулей
from disnake import ApplicationCommandInteraction, Permissions
from disnake.utils import oauth_url
from disnake.ext import commands

# EN: Token and bot variable
# RU: Переменная токена и бота
TOKEN: str = "REPLACE_ME"
bot: commands.InteractionBot = commands.InteractionBot()

# EN: on_ready listener, prints bot username and invite link
# RU: Листенер on_ready, выводит имя пользователя бота и ссылку на приглашение
@bot.listen("on_ready")
async def on_ready():
    invite = oauth_url(
        bot.application_id,
        permissions=Permissions(8),
        scopes=["bot", "applications.commands"]
    )
    return print(f"Ready! {bot.user}\nInvite link: {invite}")

# EN: /hello slash command
# RU: Слеш-команда /hello
@bot.slash_command(name="hello", description="Says hello")
async def hello(inter: ApplicationCommandInteraction):
    return await inter.send("Hello!")

# EN: Checking if __name__ is __main__ (running file directly)
# RU: Проверка того, что __name__ является __main__ (файл запускается напрямую)
if __name__ == "__main__":
    bot.run(TOKEN)
