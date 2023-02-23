import os
import subprocess

from plan import Plan


def get_plans():
    result = subprocess.run(['powercfg', '/LIST'], stdout=subprocess.PIPE)
    res_str = result.stdout.decode("utf-8")
    strlist = res_str.split("\n")

    assert (len(strlist) > 2)
    planstrs = strlist[3:]

    plans = []
    active_plan = None

    for planstr in planstrs:
        if len(planstr.strip()) == 0:
            continue

        planstr = planstr.replace("Power Scheme GUID: ", "")
        plan_parts = planstr.split(" ", 1)

        plan_id = plan_parts[0]
        plan_name = plan_parts[1]
        is_active = "*" in plan_name

        plan_name = plan_name[plan_name.find("(") + 1:plan_name.find(")")]

        # print("plan id={}, name={}".format(plan_id,plan_name))
        cur_plan = Plan(plan_id, plan_name)

        plans.append(cur_plan)

        if is_active:
            assert active_plan is None
            active_plan = cur_plan

    assert active_plan is not None

    return (plans, active_plan)


def show_plans(plans, active_plan):
    for index, value in enumerate(plans):
        print("{0}: {1}".format(index + 1, value.get_name()), end="")
        if (value == active_plan):
            print(" (active)", end="")
        print()


def choose_plan(plans, prompt):
    while True:
        try:
            choice = input(prompt)
            if choice == "":
                exit()
            else:
                num = int(choice)
                if 0 < num <= len(plans):
                    return plans[num - 1]
                else:
                    print("Invalid choice")
        except ValueError:
            print("Not a number")


def main():
    print("Windows Power Plan Switcher")
    plans, active_plan = get_plans()
    while True:
        print("Power plans:")
        show_plans(plans, active_plan)
        choice = choose_plan(plans, "Choose a plan to switch to, or press enter to quit: ")
        switch(choice)
        active_plan = choice
        print()

def switch(plan):
    print("Switching to plan \"{}\"".format(plan.get_name()))
    # print('powercfg /setactive {0}'.format(plan.get_id()))
    subprocess.run(['powercfg', '/setactive', plan.get_id()])



if __name__ == '__main__':
    main()
