# PyWizTools
## Patterns
A `Pattern` is a sequence of colors. A single pattern is represented by a `PatternEntry` object. Multiple of these make up a sequence.

### Create entries
```python
red = PatternEntry(color=(255, 0, 0), duration=1.5, brightness=100, after=PatternState.DO_NOTHING)

green = PatternEntry(color=(0, 255, 0), duration=1.5, brightness=100, after=PatternState.DO_NOTHING)
```
`duration`: how many seconds the target light should be lit up in this state  
`brightness`: percentage of brightness for the state  
`after`: what to do after the state is executed

### Add them to a pattern
After a `PatternEntry` is created, add them to a pattern
```python
pattern = Pattern(entries=[red, green], repeat_count=1, delimit_seconds=0.5)
```
`entries`: a collection containing `PatternEntry` objects  
`repeat_count`: number of times the whole pattern should be re-run  
`delimit_seconds`: duration of off state on targets between repetition of the pattern  
`after`: similar to `Pattern`'s `after`

### Run the pattern
A pattern will be run using a `WizRunner` instance. It's initialized using `wizlight` instances.
```python
light1 = wizlight('192.168.1.2')
light2 = wizlight('192.168.1.3')

runner = WizRunner(targets=[light, light2])
runner.parallel = True
await runner.run(pattern=pattern)
```

`parallel` property allows you to run the same pattern in multiple bulbs simultaneously. If set to `False`. The pattern is run on one light first and then on the next. 