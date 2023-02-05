from discord.ext import commands
from discord import app_commands

import discord

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
       
    @app_commands.command(name="help")
    @app_commands.checks.cooldown(1, 5.0, key=lambda i: (i.user.id))
    async def support(self, interaction: discord.Interaction):
        """Help command."""

        await interaction.edit_original_response(content='Help command')


async def setup(bot):
    await bot.add_cog(Help(bot))
