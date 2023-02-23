import os
import subprocess
from pathlib import Path

from plan import Plan
from plan_lib import PlanLib

def main():
    print("Windows Power Plan Switcher")
    while True:
        plans = PlanLib.get_plans()
        print("Power plans:")
        PlanLib.print_plans(plans)
        choice = PlanLib.choose_plan(plans, "Choose a plan to switch to, or press enter to quit: ")
        switch_plan(choice)
        print()


def switch_plan(plan):
    print("Switching to plan \"{}\"".format(plan.get_name()))
    plan.set_is_active(True)
    subprocess.run(['powercfg', '/setactive', plan.get_id()])


if __name__ == '__main__':
    main()
