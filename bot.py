#READ THIS!!!!
#Check for fields that need customization
#Have fun!
import discord
import random

facts = [
    "This is an example of a data table",
    "Insert information here",
]

insults = [
    "This is another data table",
]

jokes = [
    "This is ALSO another data table!",
]

responses = [
    "Replace all these data tables with whatever you want",
]

greetings = [
    "Or you can delete them and start fresh!",
]

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'INSERT YOUR TOKEN HERE!!!!'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        await client.change_presence(activity = discord.Game('INSERT YOUR STATUS HERE'))
        print(f'{client.user} is now running')


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if 'INSERT COMMAND HERE' in message.content.lower():
            await message.channel.send('INSERT RESPONSE HERE')

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)


    client.run(TOKEN)
