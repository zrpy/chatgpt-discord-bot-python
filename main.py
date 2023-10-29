import openai,discord,os
openai.api_key=os.getenv("api")
openai.api_base="https://api.chatanywhere.cn/v1"
client=discord.Client(intents=discord.Intents.all())

@client.event
async def on_message(message):
    if message.content.startswith("!gpt "):
        async with message.channel.typing():
            await message.channel.send(openai.ChatCompletion.create(model='gpt-3.5-turbo',messages=[{'role': 'user', 'content': message.content.split("!gpt ")[1]}])["choices"][0]["message"]["content"])

client.run(os.getenv("token"))
