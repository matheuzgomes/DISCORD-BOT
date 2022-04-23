from ast import arg
import discord
import os
import dotenv
import random
from discord.ext import commands
from googletrans import Translator, constants
import asyncio
from moedas import tipo_moeda

dotenv.load_dotenv()

DISCORD_TOKEN = os.getenv("TOKEN")


class Myclient(discord.Client, commands.Context):
    async def on_ready(self):
        server_count = 0

        for server in self.guilds:
            # Printar o id do server e o nome
            print(f" - {server.id} (name: {server.name})")
            server_count = server_count + 1


        print(f"TRF is in {str(server_count)} server.")  
    
    async def on_message(self, message : discord.message.Message):
        if message.author.id == self.user.id:
            return

        responses_ = ('!ola', "!olá", "!Ola","!Olá")

        if message.content.startswith(responses_):
            # Mandar uma mensagem de volta.
            await message.channel.send("Fala meu chefe!\nComo usar? Use '!' para me chamar.\nComandos: #adivinha\nEm construção...!!!")

        if message.content.startswith('!adivinha'):        
            await message.channel.send("Adivinhe um número entre 1 e 10.")

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)
            
            try:
                value = await self.wait_for('message', check = is_correct, timeout = 5.0)
            except:
                return await message.channel.send(f"Ai tu demorou em amigão, vamos pensar rápido? a resposta era {answer}")
            r_emoji1 = '\N{WHITE HEAVY CHECK MARK}'
            r_emoji2 = '\N{CROSS MARK}'
            if int(value.content) == answer:
                await value.add_reaction(r_emoji1)
                await message.channel.send("Boa garoto! Acertou!")

            else:
                await value.add_reaction(r_emoji2)
                await message.channel.send(f"Opa, errou feio em a resposta era {answer}.")

        trad_msg = ('!t', '!T', '!Tradutor', '!Traduzir', '!tradutor', '!traduzir')
        
        def check(msg : discord.message.Message):
                return msg.author == message.author
            
        if message.content.startswith(trad_msg):
            await message.channel.send("Digita ai o que tu quer que eu traduza logo, RÁPIDO...")
            
            try:
                msg = await self.wait_for('message', check=check, timeout = 15.0)
            except asyncio.TimeoutError:
                return await message.channel.send("Lento demais, hoje não vai ter tradução pra tu 👍")
            translator = Translator()
            trans_en = translator.translate(msg.content, dest= 'ja')
            await message.channel.send(f"{trans_en.text}")
            
        if message.content.startswith("!detect"):
            await message.channel.send("Quer ver eu descobrir em qual lingua ta a palavra que tu escrever ai ?")

            try:
                msg_d = await self.wait_for('message', check = check, timeout = 15)
            except asyncio.TimeoutError:
                return await message.channel.send("Tenho tua vida não amigão, demorando demais ai po tem como assim não.")
            
            detect = Translator().detect(msg_d.content)
            await message.channel.send(f"Essa língua é: {constants.LANGUAGES[detect.lang]}", mention_author = True)

        if message.content.startswith("!coin"):
            value = [message.content.split("!coin ",1)[1]]
            await message.channel.send(tipo_moeda(value))
            

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Seja bem vindo {member.mention} ao {guild.name}'
            await guild.system_channel.send(to_send)


intents = discord.Intents.default()
intents.members = True
intents.messages = True

client = Myclient(intents=intents)
client.run(DISCORD_TOKEN)