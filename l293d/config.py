import os
import yaml

config_path = ''  # Custom config filepath
# ^ For example: '/home/arthurdent/configs/l293d.yaml'

# If no custom path, user's home directory is used
if not config_path:
    # Get user home location and append filename.extension
    config_path = os.path.expanduser('~') + '/l293d-config.yaml'

config_path_exists = os.path.exists(config_path)
if (not config_path_exists):
    # Load default config
    default_file_path = str(os.path.realpath(__file__))
    # Get path of this file, and remove filename
    while default_file_path[-1] != '/':
        default_file_path = default_file_path[:-1]
    # Add default config filename
    default_file_path += 'default_l293d-config.yaml'
    # Open default config file
    default_file = open(default_file_path, 'r')
    # Read file to config contents, then close
    config_contents = default_file.read()
    default_file.close()

    # Write to user config at config path
    new_file = open(config_path, 'w')
    new_file.write(config_contents)
    new_file.close()

# https://martin-thoma.com/configuration-files-in-python/#yaml
# Open and load YAML config file
try:
    # Open config file and load as YAML
    with open(config_path, 'r') as ymlfile:
        config = yaml.load(ymlfile)
except:
    raise IOError('Error loading config from: {}. Check config exists.'.format(
        config_path))

# Assign loaded YAML to config variables
# These are loaded outside of config.py as, e.g. config.verbose
verbose = config['verbose']
test_mode = config['test_mode']
pin_numbering = config['pin_numbering']
