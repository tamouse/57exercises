from random import choice
from ex04_mad_libs.version2.madlib import MadLib

TEMPLATE1 = """That's what makes {life} {fun}. That you can {make} these {decisions}. That you can {create} the {world} that you want. See how {easy} it is to {create} a {little} {tree} right in your {world}. {Trees} cover up a {multitude} of {sins}. This is {probably the greatest thing} to happen in my {life} - to be able to {share} this with you. You {create} the {dream} - then you {bring it} into your {world}."""

TEMPLATE2 = """This is a {happy place}, {little} {squirrels} live here and {play}. Maybe there's a {happy} {little} {waterfall} happening over here. It looks so good, I might as well not stop."""

TEMPLATE3 = """Anyone can {paint}. {Volunteering} your time; it pays you and your {whole community} fantastic {dividends}. Decide where your {cloud} lives. Maybe he lives right {in here}."""

TEMPLATE4 = """Here we're {limited} by the {time} we have. This is the {fun part}. Let's do that {again}. {Look around}, look at what we have. {Beauty} is {everywhere}, you only have to {look} to {see} it. I thought {today} we would make a {happy little stream} that's just {running through the woods} here."""

TEMPLATE5 = """And just {raise} {cain}. Very {easy} to {work} these to {death}. This is the {way} you {take} {out} your {frustrations}. I {guess} that would be {considered} a {UFO}. A {big} {cotton ball} in the {sky}."""

TEMPLATE6 = """{Nothing} {wrong} with {washing} your {brush}. This is probably the {greatest thing} that's ever happened {in my life}. We {start} with a {vision} in our {heart}, and we put it on {canvas}. {Little} {trees} and {bushes} grow however makes them {happy}. {Clouds} are free they come and go as they please. The {little} {tiny Tim easels} will let you {down}."""

TEMPLATE7 = """{You} want your {tree} to have some {character}. Make it {special}. The first {step} to doing {anything} is to believe you can do it. {See it finished} in your {mind} before you ever {start}. I'm a {water} {fanatic}. I love {water}. I was blessed with a very {steady hand}; and it comes in very {handy} when you're doing these {little} {delicate} {things}. The more we do this - the more it will do good things to our heart."""

TEMPLATES = [
    TEMPLATE1,
    TEMPLATE2,
    TEMPLATE3,
    TEMPLATE4,
    TEMPLATE5,
    TEMPLATE6,
    TEMPLATE7
]



template = choice(TEMPLATES)
madlib = MadLib(template)

words = {}
for prompt in madlib.prompts():
    words[prompt] = input("Give me a {prompt}: ".format(prompt=prompt))

print(madlib.render(words))
