#####################################################################
# NewerMind Mateusz Mielniczek, 26.08.2024 for EIGENSTETTER         #
#####################################################################

from settings import BRUSH
from utils import OUT, sleep

print("Brush down...", end=" ")
OUT(BRUSH, True)
sleep(1)
print("OK !")
