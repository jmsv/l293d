import StringIO

import pkg_resources
resource_package = 'l293d'
resource_path = 'l293d-config.ini'
raw_config = pkg_resources.resource_string(resource_package, resource_path)


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


class L293DConfig(object):
    def __init__(self):
        import pkg_resources
        resource_package = 'l293d'
        resource_path = 'l293d-config.ini'
        raw_config = pkg_resources.resource_string(
            resource_package, resource_path)

        parsed_config = self.parse_config(raw_config)
        self.pin_numbering = parsed_config[0]
        self.test_mode = parsed_config[1]
        self.verbose = parsed_config[2]

#     def edit_default_config(self,
#             pin_numbering=True, test_mode=False, verbose=True):
#         """ Edits the configuration file.

#         pin_numbering = BOARD
#         test_mode = False
#         verbose = True

#         :return: None
#         """
#         with open(self.config_filename, 'w') as config_file:
#             config = ConfigParser(allow_no_value=True)
#             config.set(DEFAULTSECT, (
#                 '; See README.md for more information about config options'))
#             config.set(DEFAULTSECT, '\n; pin_numbering = (BOARD or BCM)')
#             config.set(DEFAULTSECT, 'pin_numbering', 'BOARD')
#             config.set(DEFAULTSECT, '\n; test_mode = (True or False)')
#             config.set(DEFAULTSECT, 'test_mode', 'False')
#             config.set(DEFAULTSECT, '\n; verbose = (True or False)')
#             config.set(DEFAULTSECT, 'verbose', 'True')
#             config.write(config_file)

    def parse_config(self, raw_config):
        """ Parses the config string and returns a tuple of the three values

        :return: Tuple[str, bool, bool]
        """

        buffer = StringIO.StringIO(raw_config)
        parser = ConfigParser()

        try:
            parser.readfp(buffer)
        except MissingSectionHeaderError:
            # config file is missing DEFAULT section header
            # create new config file, overwrite broken one
            raise MissingSectionHeaderError(
                'Config file broken. Try reinstalling.')

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
