import discord
import responses
import random

facts = [
    "The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion",
    "A snail breathes through its foot", 
    "Australia is wider than the moon",
    "||your mom||",
    "Sunsets on Mars are blue",
    "A mix between a Chihuahua and a dachshund is called a “chiweenie”",
    "There are no seagulls in Hawaii",
    "Dragonflies have six legs but cannot walk",
    "Gummy bears were originally called “dancing bears”",
    "There is a McDonalds in every continent except Antarctica",
    "The shortest war in history was between Britain and Zanzibar on August 27, 1896. It lasted only 38 minutes",
    "The worlds largest snowflake on record measured 15 inches wide and 8 inches thick",
    "The longest wedding veil was the same length as 63.5 football fields",
    "The worlds largest grand piano was built by a 15-year-old in New Zealand. It is nine feet long and has 85 keys",
    "The worlds largest chocolate bar weighed over 12,000 pounds and was made in Armenia in 2010",
    "Honey never spoils and can last for thousands of years.",
    "Octopi have three hearts.",
    "Bananas are berries, but strawberries aren't.",
    "There are more possible iterations of a game of chess than there are atoms in the observable universe.",
    "Koalas have fingerprints similar to human fingerprints.",
    "The Great Wall of China is not visible from space with the naked eye.",
    "The unicorn is Scotland's national animal.",
    "The world's largest desert is Antarctica.",
    "A group of flamingos is called a 'flamboyance'.",
    "The name 'Bluetooth' comes from a 10th-century Danish king, King Harald 'Bluetooth' Gormsson.",
    "Cows have best friends.",
    "There is a species of jellyfish known as 'Turritopsis dohrnii' that is biologically immortal.",
    "The smell of freshly-cut grass is actually a plant distress call.",
    "The world's largest recorded snowflake was 15 inches wide.",
    "The shortest war in history was between Britain and Zanzibar on August 27, 1896, lasting only 38 minutes.",
    "The fear of long words is called 'hippopotomonstrosesquipedaliophobia'.",
    "The word 'nerd' was first coined by Dr. Seuss in his book 'If I Ran the Zoo.'",
    "The shortest war in history was between Britain and Zanzibar on August 27, 1896, lasting only 38 minutes.",
    "Bananas are berries, but strawberries aren't.",
    "Honey never spoils and can last for thousands of years.",
    "There are more possible iterations of a game of chess than there are atoms in the observable universe.",
    "The unicorn is Scotland's national animal.",
    "The Great Wall of China is not visible from space with the naked eye.",
]

insults = [
    "your mom",
    "You're so slow, it takes you two hours to watch '60 Minutes",
    "I'd roast you, but my mom told me not to burn trash",
    "You're like a human napkin because everyone uses you and throws you away",
    "your hair is like a solar panel for a personality that needs recharging",
    "They say everyone has a hidden talent, but I'm still waiting for you to find yours",
]

jokes = [
    "Q. How does a computer get drunk? ||A. It takes screenshots.||",
    "Why did the tomato turn red? ||it saw salad dressing||",
    "What do you call a fake noodle? ||an impasta||",
    "Why did the scarecrow win an award? ||because he was outstanding in his field||",
]

responses = [
    "omg look at this ^",
    "the person below me does not have W rizz",
    "L imagine",
    "dude what",
]

greetings = [
    "what do yuw awANT!!!",
    "wussup",
    "your mom",
    "hola",
    "hey there",
    "hi",
    "i like trains",
    "my name is actually Bobothy",
]

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTE1Nzg0NTIwMDEzNjMyMzExMg.Gl9kDZ.1mqr0Qw52SVSv3B1ZvYjepakGqImML_UAZF5UM'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        await client.change_presence(activity = discord.Game('Maintnence'))
        print(f'{client.user} is now running')


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if 'jeff' in message.content.lower():
            greeting = random.choice(greetings)
            await message.channel.send(greeting)
        if '.spam' in message.content.lower():
            for i in range(5):
                await message.channel.send('MUAHAHAHAHAHAHA')
        if '.info' in message.content.lower():
            await message.channel.send('Commands: \n.fact: gives you a random fact \n.insult: gives you a random insult \n.num: gives you a random number \n.joke: gives you a random joke \n.spam: spams an annoying message \nMore commands to come soon!')
        if '.num' in message.content.lower():
            await message.channel.send(str(random.randint(0, 10000000000000000000000)))
        if '.fact' in message.content.lower():
            fact = random.choice(facts)
            await message.channel.send(fact)
        if '.insult' in message.content.lower():
            insult = random.choice(insults)
            await message.channel.send(insult)
        if '.joke' in message.content.lower():
            joke = random.choice(jokes)
            await message.channel.send(joke)
        if random.randint(1, 10) == 1:
            resp = random.choice(responses)
            await message.channel.send(resp)

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
