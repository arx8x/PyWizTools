import asyncio
from pattern import PatternEntry, Pattern, PatternState
from runner import WizRunner
from pywizlight import wizlight
from colortools import random_hue
import sys

async def main() -> None:
    light = wizlight('192.168.1.3')
    light2 = wizlight('192.168.1.9')

    # generate some random hues
    hues = set([random_hue() for _ in range(20)])
    # create entries for pattern using the generated hues
    entries = [PatternEntry(color=hue, duration=0.1, brightness=100) for hue in hues]
    # create the pattern to be run
    pattern = Pattern(items=entries, repeat_count=100, delimit_seconds=0.5)
    runner = WizRunner(targets=[light, light2])
    runner.parallel = True
    await runner.run(pattern=pattern)
    sys.exit(0)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())

