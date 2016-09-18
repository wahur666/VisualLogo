import ConfigParser

def parse_config():
    config = ConfigParser.RawConfigParser()
    config.read('settings.ini')
    config_dict = {}
    for section in config.sections():
        dict1 = {}
        options = config.options(section)
        for option in options:
            try:
                dict1[option] = config.get(section, option)
                if dict1[option] == -1:
                    print("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        config_dict[section] = dict1
    return  config_dict