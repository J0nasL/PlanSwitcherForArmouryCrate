import subprocess
from pathlib import Path

import main as lib
import os


def plan_import_prompt():
    while True:
        fname = input("Enter filename of power plan to import from the power_plans directory: ")
        fpath = Path.cwd().joinpath("power_plans").joinpath(fname)
        if os.path.isfile(fpath):
            print("Found file \"{0}\"".format(fpath))
            while True:
                ch = input("Import this plan? (y/n): ")
                if len(ch.strip()) == 0:
                    pass
                elif (ch.strip().lower().startswith("y")):
                    return (fpath)
                else:
                    print("Import aborted")
                    input()
                    exit()
        else:
            print("Could not find file \"{0}\"".format(fpath))


def import_plan(fpath):
    subprocess.run(['powercfg', '/import', fpath])
    print("\n\nDone")
    input()


def main():
    print("Windows Power Plan Importer")
    print("Currently registered power plans:")
    plans, active_plan = lib.get_plans()
    lib.show_plans(plans, active_plan)
    fpath = plan_import_prompt()
    print("Importing plan from file \"{0}\"".format(fpath))
    import_plan(fpath)


if __name__ == '__main__':
    main()
