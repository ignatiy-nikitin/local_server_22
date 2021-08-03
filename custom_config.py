from configparser import ConfigParser


class CustomConfigException(Exception):
    pass


class CustomConfig(ConfigParser):
    def __init__(self, config_file, config_settings):
        self.config_file = config_file
        self.config_settings = config_settings

        super(CustomConfig, self).__init__()
        self.read(self.config_file)
        self._validate_config()
        self._write_to_file()

    def _validate_config(self):
        self._check_sections_existence()
        self._check_keys_existence()
        self._check_keys_types()

    def _check_sections_existence(self):
        for section in self.config_settings:
            if section not in self:
                self.add_section(section)

    def _check_keys_existence(self):
        for section, keys in self.config_settings.items():
            for key, values in keys.items():
                if key not in self[section] or self[section][key] == '':
                    default_value = values.get('default')
                    if default_value is None:
                        raise CustomConfigException(
                            f'Missing value for {key} under section {section} in the config file and no default value')
                    self.set(section, key, str(default_value))

    def _check_keys_types(self):
        for section, keys in self.config_settings.items():
            for key, values in keys.items():
                type_ = values.get('type')
                if type_ is not None:
                    try:
                        type_(self[section][key])
                    except ValueError:
                        raise CustomConfigException(
                            f'Value for {key} under section {section} has invalid type. Should be {type_}')

    def _write_to_file(self):
        with open(self.config_file, 'w') as file_:
            self.write(file_)
