import subprocess

def launch_steam_game(app_id=2399830):
    command = f'start steam://rungameid/{app_id}'
    subprocess.run(command, shell=True)

launch_steam_game()

# Just testing if this worked and it does (Launches ASA)