import datetime
import logging
import random

import nextcord
from nextcord import User
from nextcord.ext import commands

# captcha helper to make photos of captcha codes
from captcha.image import ImageCaptcha
import asyncio


class Captcha(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(name="verify")
    async def verify(self, interaction):
        user = interaction.user
        if user.id == self.bot.user.id:
            return None
        if (user.has_role(1223)):
            await user.send("Already **verified**, You can enjoy texting to others!", ephemeral=True)
            return True
        image = ImageCaptcha(width=500, height=250)
        captcha_text: str = str(random.randint(1000000, 9999999))

        image.generate(captcha_text)

        await user.send(f"Sent *code* to **DMS**", ephemeral=True)
        await asyncio.to_thread(__func=image.write, chars=captcha_text, output="captcha/Captcha.png", format="png")
        print(captcha_text)
        while (True):
            embed = nextcord.Embed(title="Captcha verification",
                                   description="This captcha was sent to you because you need to get **verified**",
                                   color=nextcord.Color.red(),
                                   timestamp=datetime.datetime.now())

            def check(member: User):
                return member.id == interaction.user.id

            message = await self.bot.wait_for("message", check=check(user))
            embed.set_image(url="attachment://captcha/Captcha.png")
            if not message.guild:
                break
            await user.send(embed=embed)

        logging.info(message.content)
        if (message.content == captcha_text):
            await user.send("**Verified**", ephemeral=True)
            role = nextcord.utils.get(interaction.guild.roles, name="Verified")
            await user.add_roles(role)
        else:
            await user.send("Invalid **captcha code**", ephemeral=True)
        return


def setup(bot: commands.Bot):
    bot.add_cog(Captcha(bot))
