from argparse import ArgumentParser
from pathlib import Path
from sys import stderr

from mido import MidiFile

parser = ArgumentParser(description="Turns music into a lot of TypeScript "
                                    "code for MakeCode Arcade!")
parser.add_argument("path", type=Path,
                    help="The path to the music file. ")
parser.add_argument("--output_path", type=Path,
                    default=None, help="The path to write the code to")
parser.add_argument("--stdout", action="store_const",
                    const=True, default=False,
                    help="Whether to output everything to standard output "
                         "instead of writing to a file")
args = parser.parse_args()

in_path = args.path.expanduser().resolve()
out_path = args.output_path
to_stdout = args.stdout
if out_path is None:
    # Put output file in the same directory as input file with same name
    # but with different extension
    out_path = in_path.parent / (in_path.stem + ".txt")


def log(msg: str):
    if not to_stdout:
        print(msg)


def err(msg: str):
    stderr.write(msg)


log(f"Parsing {in_path}")
midi = MidiFile(in_path)

if midi.type not in (0, 1):
    err(f"MIDI file not type 0 or type 1!")
    exit(1)

log(f"MIDI file type: {midi.type}")

for msg in midi:
    log(f"Message: {msg}")
