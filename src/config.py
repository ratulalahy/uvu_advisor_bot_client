import configparser

class Config:
    """Configuration management class with static method."""

    @staticmethod
    def load_config(config_file: str = 'config.ini'):
        """Load and parse the configuration file as a static method."""
        config = configparser.ConfigParser()
        config.read(config_file)
        return config['DEFAULT']  # Directly return the 'DEFAULT' section or adapt as needed



if __name__ == "__main__":
    print(Config.load_config())