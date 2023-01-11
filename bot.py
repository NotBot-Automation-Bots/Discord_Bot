import discord
import responses


async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)
        await message.channel.send('Sorry, but I can\'t send you a message. Please check your privacy settings.')


async def create_channel(message, user_message):
    try:
        response = responses.create_channel(user_message)
        await message.channel.send(response)

    except Exception as e:
        print(e)
        await message.channel.send('Sorry, but I can\'t create a channel. Please check your privacy settings.')


def run_discord_bot():
    TOKEN = 'MTA1NjE2MjMyOTg4NjIwODAwMA.G4aZHI._gcLmwrNMy_zq4eCwEOZGXn9ukSJe_Y8s-h87E'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        elif user_message[0] == '!':
            user_message = user_message[8:]
            guild = message.guild
            channel = await guild.create_text_channel(user_message)
            await create_channel(message, user_message)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
