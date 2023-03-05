# Internal libs
from run.abstract_run import AbstractRun
from run.run_with_pattern import RunWithPattern
from run.run_with_image import RunWithImage

# External libs
import argparse


def get_effect() -> str:
    effects_name = list(AbstractRun.EFFECTS.keys())
    effects_mapping = {f"{i}": effects_name[i] for i in range(0, len(effects_name))}
    chosen_effect = None
    while not chosen_effect:
        print(str(effects_mapping).replace('{', '\t').replace('}', '').replace(', ', '\n\t'))
        effect_idx = str(input("Choose the effect you want to apply: "))
        chosen_effect = effects_mapping.get(effect_idx, None)

        if not chosen_effect:
            print("Please choose another one")
            print()

    return chosen_effect


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', "--input", type=str, default="tennis_court.json", help="file input name (str)")
    parser.add_argument('-s', "--save", type=bool, default=True, help="save the result or not (bool)")
    parser.add_argument('-l', "--local", type=bool, default=True, help="local execution or not (bool)")
    args = parser.parse_args()

    if args.local:
        effect = get_effect()
    else:
        effect = "cover_line"

    if ".json" in args.input:
        RunWithPattern(args.input, effect, args.save)
    else:
        RunWithImage(args.input, effect, args.save)
