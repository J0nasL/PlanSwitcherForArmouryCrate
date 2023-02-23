import ctypes
import os
import subprocess
import os
import sys
from pathlib import Path

import main as lib


def get_fname(plan):
    while True:
        rel_path = "./power_plans/"
        fname = rel_path + input("Enter destination file for plan \"{0}\": ".format(plan.get_name()))
        if os.path.isfile(fname):
            print("File already exists!")
        elif os.path.isdir(fname):
            print("Directory with same name already exists!")
        else:
            ch = input("Export this plan? (y/n): ")
            if len(ch.strip()) == 0:
                pass
            elif (ch.strip().lower().startswith("y")):
                return (fname)
            else:
                print("Import aborted")
                exit()


def export(fname, plan):
    subprocess.run(['powercfg', '/export', fname, plan.get_id()], shell=True)

def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

def main():
    print("Windows Power Plan Exporter")
    if isAdmin():
        print("Running as administrator")
    else:
        print("\nNot running as administrator, relaunch as administrator to use!")
        input("Press enter to continue anyway ")

    print("\nPower plans:")
    plans, active_plan = lib.get_plans()
    lib.show_plans(plans, active_plan)
    plan = lib.choose_plan(plans, "Choose a plan to export, or press enter to quit: ")
    fname = get_fname(plan)
    export(fname, plan)


if __name__ == '__main__':
    main()
