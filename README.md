# rrt-demonstrations

### VS Code Notes:
- Open the **workspace file**, not the folder. Change the settings in this file if you wish to share the configuration with others; if not, override the settings in a local, untracked `.vscode/settings.json`. 
    - If you want the python virtual environment to be in a different location from the one specified in the workspace file, you must override this in the local `settings.json`, or linting and imports will not display properly in the IDE.
- Execute the code by running the default build task (Ctrl+Shift+B should do this). The task will run a script that should handle any necessary setup for you. 