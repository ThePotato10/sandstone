# Sandstone
A Lightweight and Fast Terminal-based Todo App :rocket:

## Installation

I'm assuming that if you plan on using a terminal-based app you at least have basic familiarity with a CLI

1. Git clone this repository to wherever you want to install it (`git clone https://github.com/ThePotato10/sandstone.git`)
2. cd into sandstone/src (`cd sandstone/src`)
3. pip install the requirements (these ship with most OSes by default but just in case) by running `pip3 install os sqlite3 click`
4. Setup your Sandstone alias (add `alias sandstone="python3 {INSTALLATION_LOCATION}/src/sandstone_cli.py"` to your .bashrc or .zshrc)
5. Run the command `sandstone init`
6. Enjoy! :heart:

## How to Use

**Before using Sandstone you must run** `sandstone init`

  ### Creating Todos
  
  Run the command `sandstone add -t [your todo]`. The `-t` flag is required. Add the flag `-d` if you want the newly-created todo to be marked as complete
  
  ### Displaying Todos
  
  Run the command `sandstone list` to see all your todos. To only see the uncomplete ones, add the flag `-u`
  
  ### Completing/Uncompleting Todos
  
  Run the command `sandstone complete -i [todo id]` to complete a todo. The `-i` flag is required
  
  Run the command `sandstone uncomplete -i [todo id]` to uncomplete a todo. Like above, the `-i` flag is required
  
  ### Deleting Todos
  
  Run the command `sandstone delete -i [todo id]` to delete a todo. The `-i` flag is required
  
  **The todo ids are listed in the first column of the output from** `sandstone list`
  
  ## Contributing
  
  All contributions are welcome. Just fork and PR :blue_heart:
