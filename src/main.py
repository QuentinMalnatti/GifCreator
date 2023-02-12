# Internal libs
from run.run_with_pattern import RunWithPattern
from run.run_with_image import RunWithImage

# External libs
import argparse


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', "--input", type=str, default="tennis_court.json", help="file input name (str)")
    parser.add_argument('-e', "--effect", type=str, default="cover", help="effect name to apply (str)")
    parser.add_argument('-s', "--save", type=bool, default=True, help="save the result or not (bool)")
    args = parser.parse_args()

    if ".json" in args.input:
        RunWithPattern(args.input, args.effect, args.save)
    else:
        RunWithImage(args.input, args.effect, args.save)
