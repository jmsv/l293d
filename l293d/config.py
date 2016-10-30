try:
    # Python 2
    from ConfigParser import (
        SafeConfigParser as ConfigParser,
        DEFAULTSECT,
        MissingSectionHeaderError,
        NoOptionError
    )
except ImportError:
    # Python 3
    from configparser import (
        # SafeConfigParser has been renamed ConfigParser since Python 3.2
        ConfigParser,
        DEFAULTSECT,
        MissingSectionHeaderError,
        NoOptionError
    )
import os


class L293DConfig(object):
    def __init__(self, config_filename='default_l293d_config.ini'):
        self.config_filename = config_filename
        if not os.path.exists(self.config_filename):
            # if config file doesn't exist, create a new one
            self.create_config_file()

        # load config variables from config file (new or old)
        self.pin_numbering, self.test_mode, self.verbose = self.parse_config()

        # print('Pin Numbering: {}\nTest Mode: {}\nVerbose: {}'.format(
        #     self.pin_numbering, self.test_mode, self.verbose
        # ))

    def create_config_file(self):
        """ Creates a new configuration file with the default settings

        pin_numbering = BOARD
        test_mode = False
        verbose = True

        :return: None
        """
        with open(self.config_filename, 'w') as config_file:
            config = ConfigParser(allow_no_value=True)
            config.set(DEFAULTSECT, (
                '; See README.md for more information about config options'))
            config.set(DEFAULTSECT, '\n; pin_numbering = (BOARD or BCM)')
            config.set(DEFAULTSECT, 'pin_numbering', 'BOARD')
            config.set(DEFAULTSECT, '\n; test_mode = (True or False)')
            config.set(DEFAULTSECT, 'test_mode', 'False')
            config.set(DEFAULTSECT, '\n; verbose = (True or False)')
            config.set(DEFAULTSECT, 'verbose', 'True')
            config.write(config_file)

    def parse_config(self):
        """ Parses the config file and returns a tuple of the three values

        :return: Tuple[str, bool, bool]
        """
        parser = ConfigParser()
        try:
            parser.read(self.config_filename)
        except MissingSectionHeaderError:
            # config file is missing DEFAULT section header
            # create new config file, overwrite broken one
            self.create_config_file()
            return self.parse_config()

        try:
            pin_numbering = parser.get(DEFAULTSECT, 'pin_numbering')
            if pin_numbering.upper() not in ('BCM', 'BOARD'):
                # if invalid option, reset to default: BOARD
                pin_numbering = 'BOARD'
        except NoOptionError:
            # pin_numbering option doesn't exist in config file
            pin_numbering = 'BOARD'

        try:
            test_mode = parser.getboolean(DEFAULTSECT, 'test_mode')
        except (NoOptionError, ValueError):
            # NoOptionError: test_mode option doesn't exist in config file
            # ValueError: test_mode value isn't a boolean
            test_mode = False

        try:
            verbose = parser.getboolean(DEFAULTSECT, 'verbose')
        except (NoOptionError, ValueError):
            # NoOptionError: verbose option doesn't exist in config file
            # ValueError: verbose value isn't a boolean
            verbose = True

        return pin_numbering, test_mode, verbose
