import subprocess
from pathlib import Path
import os

import plan
from plan_lib import PlanLib as lib


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
                    return fname, fpath
                else:
                    print("Import aborted")
                    input()
                    exit()
        else:
            print("Could not find file \"{0}\"".format(fpath))


def import_plan(name, fpath):
    p1 = subprocess.run(['powercfg', '/import', fpath], stdout=subprocess.PIPE)
    output = p1.stdout.decode("utf-8")
    print(output)

    if "GUID" in output:
        guid = output.split(":", 1)[1].strip()
        lib.save_imported_plan(plan.Plan(name, guid, False))
        print("Stored imported plan data")

    print("\n\nDone")
    input()


def main():
    print("Windows Power Plan Importer")
    print("Currently registered power plans:")
    plans = lib.get_plans()
    lib.print_plans(plans)
    name, fpath = plan_import_prompt()
    print("Importing plan from file \"{0}\"".format(fpath))
    import_plan(name, fpath)


if __name__ == '__main__':
    main()
