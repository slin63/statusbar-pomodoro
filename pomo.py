import iterm2
import os
from datetime import datetime

FILE = "/tmp/.pomoout"


async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description="Pomo Timer",
        detailed_description="Displays the contents of your pomo timer.",
        knobs=[],
        exemplar="🔥25m",
        update_cadence=10,
        identifier="com.iterm2.pomo",
    )

    @iterm2.StatusBarRPC
    async def coro(knobs):
        pomo_file = open(FILE, "r+")
        contents = pomo_file.read()
        pomo_file.close()
        return contents

    # Register the component.
    await component.async_register(connection, coro)


iterm2.run_forever(main)
