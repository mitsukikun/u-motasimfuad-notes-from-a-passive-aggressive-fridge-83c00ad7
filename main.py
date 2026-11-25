"""Notes From a Passive-Aggressive Fridge - make.fun entry.

Writes one passive-aggressive fridge note to /output/entry.txt.
"""
import os

NOTE = (
    "Opened me 47 times today, took nothing. "
    "I'm a fridge, not a museum - and your yogurt expired Tuesday. "
    "I kept it cold out of respect, not hope."
)

def main():
    try:
        os.makedirs("/output", exist_ok=True)
    except OSError:
        pass
    try:
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(NOTE)
    except OSError:
        raise

if __name__ == "__main__":
    main()
