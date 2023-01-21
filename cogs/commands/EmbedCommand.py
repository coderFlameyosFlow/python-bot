import nextcord
from nextcord import Interaction, SlashOption, Colour, Attachment

from nextcord.ext import commands


class EmbedCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(name="createembed", description="Create an embed and send it!")
    async def createEmbed(
            self, interaction: Interaction,
            title: str = SlashOption(name="title", description="Title for the Embed", required=True),
            description: str = SlashOption(name="description", description="Description for the Embed", required=True),
            color1: int = SlashOption(name="rgbcolour1", description="Color for the Embed", required=False),
            color2: int = SlashOption(name="rgbcolour2", description="Color for the Embed", required=False),
            color3: int = SlashOption(name="rgbcolour3", description="Color for the Embed", required=False),
            thumbnail: Attachment = SlashOption(name="thumbnail", description="Thumbnail for the Embed",
                                                required=False),
            image: Attachment = SlashOption(name="image", description="Image for the Embed", required=False),
            fieldsinline: bool = SlashOption(name="inline", description="If all fields should be inline or not",
                                             required=False),
            fieldonetitle: str = SlashOption(name="fieldonetitle", description="First Field Title for the Embed",
                                             required=False),
            fieldonedesc: str = SlashOption(name="fieldonedesc", description="Second Field Description for the Embed",
                                            required=False),
            fieldtwotitle: str = SlashOption(name="fieldtwotitle", description="Second Field Title for the Embed",
                                             required=False),
            fieldtwodesc: str = SlashOption(name="fieldtwodesc", description="Second Field Description for the Embed",
                                            required=False)
    ):
        thumbnail = thumbnail or None
        image = image or None
        if (color1 is not None and color2 is not None and color3 is not None):
            color = Colour.from_rgb(color1, color2, color3)
        else:
            color = None
        embed = nextcord.Embed(title=title, description=description, colour=color)
        embed.set_image(url=image)
        embed.set_thumbnail(url=thumbnail)
        if (fieldonedesc is not None and fieldonetitle is not None):
            embed.add_field(name=fieldonetitle, value=fieldonedesc, inline=fieldsinline)
        if (fieldtwodesc is not None and fieldtwotitle is not None):
            embed.add_field(name=fieldtwotitle, value=fieldtwodesc, inline=fieldsinline)
        await interaction.channel.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(EmbedCommand(bot))
