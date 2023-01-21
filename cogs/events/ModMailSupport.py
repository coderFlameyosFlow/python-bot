import nextcord
from nextcord import Interaction
from nextcord.ext import commands


class ModMailSupport(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        if message.author is message.author.bot:
            return None

        user = await message.guild.fetch_member(int(message.channel.name))
        await user.send(f"**{message.author.name}**: {message.content}")

    @nextcord.slash_command(name="closethread", description="Closes a help thread")
    async def close_thread(self, interaction: Interaction):
        await interaction.channel.delete()
