import platform
import os
import sys
import logging
logging.basicConfig(
    level=logging.INFO,
    format=' •\x1b[38;5;196m ×͜× \x1b[37m %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

global arc

def update_repository():
    exit_code = os.system('git pull --quiet')
    if exit_code != 0:
        logging.error('Failed to pull updates from repository.')
        sys.exit(1)
    logging.info('Repository is up to date.')

def check_python_architecture():
    global arc
    architecture = platform.architecture()[0]
    try:
        if architecture == '32bit':
            arc = "32BIT"
            import bo as Luffy
        else:
            arc = "INVALID"
            logging.error('Unsupported architecture detected.')
            sys.exit(1)
        os.system('clear')
        Luffy.menu()  # Updated from start to menu
    
    except ImportError as e:
        logging.error(f'Failed to import module: {e}')
        sys.exit(1)

if __name__ == "__main__":
    update_repository()
    check_python_architecture()
