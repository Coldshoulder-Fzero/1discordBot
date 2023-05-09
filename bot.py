import discord
import responses
from discord.ext import commands

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTEwNTE2MzkzMzY1ODEzNjY3Ng.GA354e.sADt54Bfks00Z77yKF9GVukHwa_p-W8tB0iqqc'
    intents = discord.Intents.default()
    intents.message_content = True
    intents.messages = True

    bot = commands.Bot(command_prefix='!', intents=intents)
    rage_counter = {}

    @bot.event
    async def on_ready():
        print(f'{bot.user.name} has connected to Discord!')

    @bot.command(name='raged')
    async def raged(ctx, user: discord.Member):
        if user.id not in rage_counter:
            rage_counter[user.id] = 1
        else:
            rage_counter[user.id] += 1

        await ctx.send(f"{user.mention} has raged {rage_counter[user.id]} times.")

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

        await bot.process_commands(message)

    bot.run(TOKEN)