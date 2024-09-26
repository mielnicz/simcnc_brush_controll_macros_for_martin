#####################################################################
# NewerMind Mateusz Mielniczek, 26.08.2024 for EIGENSTETTER         #
#####################################################################

from settings import BRUSH, BRUSH_UP
from utils import ERROR, IN, OUT, TIMEOUT

print("Brush up...")
OUT(BRUSH, False)

print("Waiting for confirmation from brush...", end=" ")
if TIMEOUT(lambda: IN(BRUSH_UP), 1.5):
    ERROR("\nBRUSH NOT UP !!!\nCannot change tool.")
else:
    print("OK !")
