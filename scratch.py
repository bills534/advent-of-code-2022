
from pathlib import Path

myPath = 'root/abc/cbs'

fancyPath = Path(myPath)
upDir = fancyPath.parent

print(fancyPath)
fancyPath = fancyPath.parent
print(fancyPath)
fancyPath = fancyPath.joinpath('cheese')
print(fancyPath)

