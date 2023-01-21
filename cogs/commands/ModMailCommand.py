import nextcord
from nextcord import Member, TextChannel
from nextcord.ext import commands


# noinspection PyRedundantParentheses
async def lookForMessages(member: Member, thread: TextChannel):
    async for someMessage in thread.history(limit=None):
        await member.send(str(someMessage))


class ModMailCommand(commands.Cog):
    modMailStarted = False

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if (message.author == self.bot.user) or (message.guild):
            return
        modMailChannel = nextcord.utils.get(message.guild.categories, name="Mod-Mails")
        channel = await message.guild.create_category(name="Mod-Mails",
                                                      reason="No current \'Mod-Mails\' found") \
            if modMailChannel is None or False else modMailChannel
        thread = await channel.create_text_channel(name=f"{message.author.id}", category=channel)
        await thread.send(content=f"**{message.author.name}**: {message.content}")
        # run "lookForMessages" in a separate thread to handle messages received async-appropriately.
        await lookForMessages(member=message.author, thread=thread)


def setup(bot: commands.Bot):
    bot.add_cog(ModMailCommand(bot))
