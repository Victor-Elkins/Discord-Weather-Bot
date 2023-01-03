import discord
import chess
from discord.ext import commands
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

games = {}  # a dictionary to store all the current games
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
@bot.command
async def challenge(message):
    if True:
        # parse the challenge command to get the opponent's mention
        opponent = message.mentions[0]
        if opponent.id in games:
            await message.channel.send(f"{opponent.mention} is already in a game!")
        else:
            # create a new chess board and store it in the games dictionary
            board = chess.Board()
            games[opponent.id] = {
                'board': board,
                'challenger': message.author,
                'opponent': opponent
            }
            await message.channel.send(f"{opponent.mention}, you have been challenged to a game of chess by {message.author.mention}! Use the `!accept` command to accept the challenge.")
    elif message.content.startswith('!accept'):
        
        game = games.get(message.author.id)
        if game:
            del games[game['opponent'].id]  # remove the game from the dictionary
            await message.channel.send(f"{message.author.mention} has accepted the challenge from {game['challenger'].mention}! The game has started.")
            # start the game loop
            while not game['board'].is_game_over():
                await message.channel.send(f"{game['challenger'].mention}'s turn. Make your move using chess notation (e.g. e2e4).")
                move = await bot.wait_for('message', check=lambda m: m.author == game['challenger'])
                try:
                    game['board'].push_uci(move.content)
                except ValueError:
                    await message.channel.send(f"{move.author.mention}: Invalid move!")
                    continue
                await message.channel.send(f"{game['opponent'].mention}'s turn. Make your move using chess notation (e.g. e2e4).")
                move = await bot.wait_for('message', check=lambda m: m.author == game['opponent'])
                try:
                    game['board'].push_uci(move.content)
                except ValueError:
                    await message.channel.send(f"{move.author.mention}: Invalid move!")
                    continue
            # game is over, announce the result and delete the game object
            result = game['board'].result()