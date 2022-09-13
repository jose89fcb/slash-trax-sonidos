import discord
from discord.ext import commands
import random
import os
import json
###
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_choice, create_option
from discord_slash import SlashCommand, SlashContext



with open("configuracion.json") as f: #Creamos un archivo de configuracion para el bot
    config = json.load(f)

bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help


slash = SlashCommand(bot, sync_commands=True)
@slash.slash(
    name="sonido", description="Sonidos trax Habbo Hotel",
    options=[
                create_option(
                  name="numero",
                  description="Escribe un numero del 1 al 648",
                  option_type=3,
                  required=True
                )
             
                
               
                  
                
             ])


async def _sonido(ctx:SlashContext, numero:str):
    
   
    
   
    
   
    


      
   

    try:

     await ctx.send(hidden=True,file=discord.File(f"trax/{numero}.mp3"))
    except FileNotFoundError:
        await ctx.send(f"el archivo {numero}.mp3 no existe.") 



######


@slash.slash(
    name="sonidorandom", description="Sonido Random trax Habbo Hotel",
    options=[
                
                
               
                  
                
             ])


async def _sonidorandom(ctx:SlashContext):
    
    sonido = random.choice(os.listdir('trax'))
    

   
      
   

    

    await ctx.send(hidden=True,file=discord.File(f"trax/{sonido}"))
  

   ##########################
   #Programado Por Jose89fcb#
   #   Trax Habbo Hotel     #
   #    2022©               #
   ##########################


@bot.event
async def on_ready():
    print(f"BOT listo! {bot.user}")
    
    
    
    
bot.run(config["tokendiscord"])
