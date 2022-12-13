# Advent of Code

This repo contains my solutions to the advent of code problems.

## Requirements

- A `bash` or `zsh` terminal
- Python 3.5 or newer
- Chrome or Firefox

## Setup

1. Run `./setup.sh $(date +%Y)` script to create the directory for the current year.
2. In the terminal navigate to the directory you just created (e.g. `cd $(date +%Y)`).
3. Activate the venv by running `source ${HOME}/.virtualenvs/${PWD##*/}/bin/activate`.
4. Sign in on the advent of code website in either Chrome or Firefox
5. Save your authentication token by running `aocd-token > ~/.config/aocd/token`.
6. Run `./get_data.sh` to get all the available inputs for your current directory.

## Troubleshooting

### Invalid token

If you sign out of Advent of Code your token will no longer be valid.
Rerun steps 4 and 5 of the setup to refresh your token.

### Empty or incorrect input file

Delete the incorrect input file and re-run `./get_data.sh`
