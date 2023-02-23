import subprocess

import main as lib
import os


def plan_import_prompt():
    while True:
        fname = input("Enter filename of power plan to import: ")
        if os.path.isfile(fname):
            print("Found file \"{0}\"".format(fname))
            while True:
                ch = input("Import this plan? (y/n): ")
                if len(ch.strip()) == 0:
                    pass
                elif (ch.strip().lower().startswith("y")):
                    return (fname)
                else:
                    print("Import aborted")
                    exit()
        else:
            print("Could not find file \"{0}\"".format(fname))


def import_plan(fname):
    subprocess.run(['powercfg', '/import', fname])


def main():
    print("Windows Power Plan Importer")
    print("Currently registered power plans:")
    plans, active_plan = lib.get_plans()
    lib.show_plans(plans, active_plan)
    fname = plan_import_prompt()
    print("Importing plan from file \"{0}\"".format(fname))
    import_plan(fname)


if __name__ == '__main__':
    main()
