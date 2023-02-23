import subprocess
from pathlib import Path

from plan import Plan


class PlanLib:
    plan_database = "store/planIDs.txt"  # Stores plan data to remember "hidden" imported plans
    plan_storage = "./power_plans/"  # File location to save/import power plans

    @classmethod
    def _get_visible_plans(cls):
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

            cur_plan = Plan(plan_id, plan_name, is_active, False)

            plans.append(cur_plan)

            if is_active:
                assert active_plan is None
                active_plan = cur_plan

        assert active_plan is not None
        return plans

    @classmethod
    def get_plans(cls):
        visible = cls._get_visible_plans()
        stored = cls._get_stored_plans()
        all_plans = visible
        # Add stored plans that are not visible to the list of plans
        for sto in stored:
            found = False
            for vis in visible:
                if sto.get_id() == vis.get_id():
                    found = True
            if not found:
                all_plans.append(sto)

        return all_plans

    @classmethod
    def print_plans(cls, plans):
        inform = False
        for p in plans:
            if p.is_hidden():
                inform = True
        if inform:
            print("Plans that were previously imported but no longer appear in powercfg list are marked as (hidden)\n")
        for index, value in enumerate(plans):
            print("{0}: {1}".format(index + 1, value.get_name()), end="")
            if value.is_active():
                print(" (active)", end="")
            if value.is_hidden():
                print(" (hidden)", end="")
            print()
        print()

    @classmethod
    def choose_plan(cls, plans, prompt):
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

    @classmethod
    def _get_stored_plans(cls):
        file = Path.open(Path.cwd().joinpath(cls.plan_database))
        plans = []
        for line in file:
            line = line.strip()
            if len(line) != 0 and not line.startswith("#"):
                #print("parse:"+line)
                parts = line.split("|")
                plan_name = parts[0]
                plan_id = parts[1]
                plan = Plan(plan_name, plan_id, False, True)
                plans.append(plan)
        file.close()
        #print(plans)
        return plans

    @classmethod
    def save_imported_plan(cls, plan):
        file = Path.open(Path.cwd().joinpath(cls.plan_database), "a")
        file.write("\n{0}|{1}".format(plan.get_name(), plan.get_id()))
        file.close()
