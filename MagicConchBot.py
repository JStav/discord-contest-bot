
import discord
import random
from discord.ext import commands

token = ''
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')
    
@client.command(alias=['Magic Conch'])
async def magicConch(ctx, *, question):
    responses = ['Maybe someday',
                'Follow the seahorse.',
                'I dont think so.',
                'No.',
                'Yes.',
                'Try asking again.'
                ]

    if question == 'What do we do now?' or question == 'What do I do?' or question == 'What should I do now?' or question == 'Oh, Magic Conch Shell, what do we need to do to get out of the Kelp Forest?':
        await ctx.send('Nothing')
    elif question == 'Which one should I have?' or question== 'Which one of these delicious foods should I have?' or question == 'Uh, hello there. Magic Conch, uh, I was wondering... uh, should I have the spaghetti or the turkey?' or question == 'Should I have the spagetti or the turkey?':
        await ctx.send('Neither')
    elif question == 'Can I have something to eat?' or question == 'can I have something to eat?' or question == 'can I have something to eat' or question=='Magic Conch, could Squidward have some of this yummy, delicious, super-terrific sandwich?':
        await ctx.send('No')
    elif question == 'Oh. Then how about the soup?' or question == 'Can I have the soup?':
        await ctx.send('I dont think so')
    elif question == 'Magic Conch Shell, will I ever get married?' or question == 'Will I ever get married?':
        await ctx.send('Maybe someday')
    
    else:
        await ctx.send(f'{random.choice(responses)}')


client.run(token)
