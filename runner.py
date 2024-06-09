import asyncio
from pywizlight import wizlight, PilotBuilder
from pattern import Pattern, PatternEntry, PatternState

RunParams = tuple[PilotBuilder, PatternEntry]

class WizRunner:

    def __init__(self, targets = tuple[wizlight]) -> None:
        self.__targets = targets
        # whether the patterns should be run on targets simultaneously
        self.parallel = False
    
    async def run(self, pattern: Pattern) -> None:
        # this is a proxy method to handle repeats, delimits, 
        # after state etc
        run_count = pattern.repeat_count + 1
        delimit = True if (run_count > 1 and pattern.delimit_seconds > 0) else False
        for _ in range(pattern.repeat_count + 1):
            await self._run(pattern=pattern)
            if delimit:
                await asyncio.sleep(pattern.delimit_seconds)

    async def _run(self, pattern: Pattern) -> None:
        # build run params beforehand
        run_params: list[RunParams] = []
        for item in pattern.entries:
            p = PilotBuilder(rgb = item.color, brightness=item.int8_brightness)
            run_params.append((p, item))

        # If parallel mode is active, generate coroutines and run them together
        # Each coroutine runs one pattern on one target
        tasks = []        
        if self.parallel:
            for target in self.__targets:
                tasks.append(self._run_params_on_target(target, run_params))
        # if not in parallel mode, run one pattern on one target, then on the next
        else:
            for t in self.__targets:
                await self._run_params_on_target(t, run_params)

        if self.parallel:
            await asyncio.gather(*tasks)

    async def _run_params_on_target(self, target: wizlight, params: list[RunParams]):
        for p, item in params:
            await target.turn_on(p)
            if item.duration:
                await asyncio.sleep(item.duration)
            # FIXME: moved .after to Pattern
            if item.after == PatternState.TURN_OFF:
                await target.turn_off()
