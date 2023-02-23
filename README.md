# Plan Switcher for Armoury Crate
Armoury Crate is a bloated, buggy ASUS app that eats up system resources and causes crashes.
Its main feature is the ability to switch "operating modes" users can select to provide high performance or reduce noise.
Under the hood, these modes are controlled using Windows Power Plans.

This repository provides functionality to allow users to easily switch their current power plan, as well as import and export power plans.
The plans that Armoury Crate uses are provided in /power_plans and can be imported using import.py.

To export power plans, right click export-runner.py > run as administrator.
This file launches export.py with administrator privileges, which are required to run the export command.

For Windows use only!
