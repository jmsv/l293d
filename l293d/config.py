config_path = '' # Custom config filepath
#^ For example: '/home/arthurdent/configs/l293d.yaml'

if not config_path:
    import os
    config_path = os.path.expanduser('~') + '/l293d-config.yaml'
    if not os.path.exists(config_path):
        config_contents = '''
# The configuration file for the l293d driver module
# --------------------------------------------------

verbose: true
#^ Prints stuff to the terminal

test_mode: false
#^ Disables GPIO calls when called

pin_numbering: BOARD
#^ BOARD or BCM mode - see README


''' # This string acts as the default configuration
        file = open(config_path, 'w')
        file.write(config_contents)
        file.close()

import yaml
# https://martin-thoma.com/configuration-files-in-python/#yaml
with open(config_path, 'r') as ymlfile:
    config = yaml.load(ymlfile)

verbose = config['verbose']
test_mode = config['test_mode']
pin_numbering = config['pin_numbering']
>>>>>>> 8419ecb8496eb0aacee3ec3fb3286fa013a3d73f
