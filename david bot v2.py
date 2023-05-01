import discord
import asyncio
from discord.ext import commands
from discord.utils import get
from itertools import cycle


# davids user id 687685540346331195


TOKEN = 'MTA5ODkzMjkzOTY2NTk4NTYxOA.GtI5FN.HStyxM6r63BBaCj5bOhs6U06Y_wjYQuA5oJf-E'

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)


async def rainbow_role(member):
    guild = member.guild
    red = discord.utils.get(guild.roles, name='red')
    orange = discord.utils.get(guild.roles, name='orange')
    yellow = discord.utils.get(guild.roles, name='yellow')
    green = discord.utils.get(guild.roles, name='green')
    light_blue = discord.utils.get(guild.roles, name='light_blue')
    dark_blue = discord.utils.get(guild.roles, name='dark_blue')
    purple = discord.utils.get(guild.roles, name='purple')

    while True:
        rainbow_roles = [red, orange, yellow, green, light_blue, purple]
        names = ['.........', '....I am', '.I am Gay', '.am Gay...', 'Gay......', '..........']
        old_role = None

        for i in range(len(rainbow_roles)):
            await member.edit(nick=names[i])
            new_role = rainbow_roles[i]

            if old_role:
                await member.add_roles(new_role)
                await member.remove_roles(old_role)
            else:
                await member.add_roles(new_role)

            old_role = new_role
            await asyncio.sleep(1)

        await member.remove_roles(old_role)

@bot.event
async def on_ready():
    user_id = 1100523120827318272
    guild = bot.get_guild(1058791543252734044)
    user = guild.get_member(user_id)
    await rainbow_role(user)

@bot.event
async def on_member_join(member):
    if member.id == 1100523120827318272:
        await rainbow_role(member)

@bot.command()
async def david(message):
    ctx = await bot.get_context(message)
    embed = discord.Embed(
        colour=discord.Colour.dark_blue(),
        description="Davids silly billy",
        title="🤫"
    )

    embed.set_image(url="https://cdn.discordapp.com/attachments/1060890325238939668/1099780120467750922/OTAweDkwMA.png")

    messages_to_delete = []
    counter = 0
    while counter < 3:
        print("asd")
        sent_message = await ctx.send(embed=embed)
        messages_to_delete.append(sent_message)
        counter += 1
        await asyncio.sleep(1)

    await asyncio.sleep(5)
    for message in messages_to_delete:
        await message.delete()

    await asyncio.sleep(30)

    for message in messages_to_delete:
        await message.delete()



@bot.event
async def on_message(message):

    david_name = ['<@687685540346331195>', 'david', 'davids', 'davdis', 'dvadis', 'davide', '@david', '@scorpion']

    if "!david" in message.content:
        await message.delete()

    if message.content.startswith('!david'):
        await david(message)

    else:
        for name in david_name:
            if name.lower() in message.content.lower():
                embed = discord.Embed(title='David Detected')
                embed.set_image(url='https://cdn.discordapp.com/attachments/1100030470235902013/1100469600531005491/nerd-emoji-nerd_1.gif')
                sent_message = await message.channel.send(embed=embed)
                await asyncio.sleep(6)
                await sent_message.delete()
                break

    if message.content == '!goofy':
        user_id = 687685540346331195
        guild = message.guild
        user = guild.get_member(user_id)
        role = discord.utils.get(guild.roles, name='Goofy')
        await user.add_roles(role)
        await asyncio.sleep(30)  # 30 sec
        await user.remove_roles(role)

    if message.content.startswith('!delete_last_20'):
        channel = message.channel
        messages = []
        async for msg in channel.history(limit=20):
            if msg.author == bot.user:
                messages.append(msg)
        await channel.delete_messages(messages)

    if message.content.startswith('!send'):
        user_id = 262037900571574272
        user = await bot.fetch_user(user_id)
        await user.send('niger')




bot.run(TOKEN)