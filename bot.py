import discord
import responses
import os

intents = discord.Intents.all()


def run_discord_bot():
    # Change your token here
    TOKEN = os.getenv("DISCORD_BOT_TOKEN")
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        user_message = message.content
        channel = message.channel
        is_private = isinstance(channel, discord.abc.PrivateChannel)
        author = message.author

        print(f"{author} said: '{user_message}' in {channel}")

        response = await responses.get_response(user_message, channel, client)

        if response:
            if is_private:
                await channel.send(response)
            else:
                await channel.send(f"{author.name}, {response}")

    client.run(TOKEN)
