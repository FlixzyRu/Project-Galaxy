import discord
import random

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

TOKEN = 'MTI0NDIyODY1NTk5NjA3NjA2Mg.GBYUOP.7i4VGW5OL0p4mV5mUYJqjXiR-obNOh9L9CMIWk'
WELCOME_CHANNEL_ID = 1243861727582359636

welcome_messages = [
    "➡️ Let's all give a warm welcome to **{username}**!",
    "➡️ Hello and welcome, **{username}**!",
    "➡️ Hey **{username}**, glad to have you here!",
    "➡️ Welcome aboard, **{username}**!",
    "➡️ We're thrilled to welcome you, **{username}**!",
    "➡️ Hi **{username}**, welcome to our community!",
    "➡️ Greetings **{username}**! Great to see you here!",
    "➡️ **{username}**, we're excited to have you!",
    "➡️ Hello **{username}**, thanks for joining us!",
    "➡️ Hi **{username}**, we're happy you're here!",
    "➡️ Welcome **{username}**, enjoy your stay!",
    "➡️ Hi **{username}**, great to have you with us!"
]

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_member_join(member):
    channel = client.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        welcome_message = random.choice(welcome_messages).format(username=member.name)
        await channel.send(welcome_message)

client.run(TOKEN)
