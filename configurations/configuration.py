import yaml
from shutil import copyfile
import os


def load_configuration_variables_from_file(config):
    # loading application configuration variables from a file
    print("Injecting config variables from :%s" % app_config.INSTANCE_CONFIG)
    with open(app_config.INSTANCE_CONFIG) as f:
        cofg = yaml.load(f)
    for x, y in cofg.items():
        setattr(config, x, y)

def set_database_connection_variables(config):
    '''
    set the databases attributes using configuration class
    i.e. databases name, password and uri
    :param database: databse name
    :return:
    '''
    if hasattr(config, 'DATABASE_PORT'):
        address = config.DATABASE_SERVER_URI + ':%s' % app_config.DATABASE_PORT
    else:
        address = config.DATABASE_SERVER_URI
    app_config.database_connector=''
    app_config.DATABASE_URI = 'postgresql://%s:%s@%s/%s' \
                                                  % (config.DATABASE_USER, \
                                            config.DATABASE_PASSWORD, \
                                            address, config.DATABAS_NAME)


class app_config (object):
    # the configuration can be loadd from yml file later
    SECRET_KEY= "sdljhfd123ssdxckfgsdvbfl342fvsdfafgdf"
    home_folder = os.path.expanduser('~')
    print (home_folder)
    INSTANCE_CONFIG = os.path.join(home_folder, '.app_config.yml')
    if not os.path.isfile(INSTANCE_CONFIG):
        LOCAL_CONFIG_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                         '.app_config.yml')
        copyfile(LOCAL_CONFIG_FILE, INSTANCE_CONFIG)
        print (LOCAL_CONFIG_FILE, INSTANCE_CONFIG)

class development_app_config(app_config):
    DEBUG = False
    VERIFY = False

class production_app_config(app_config):
    pass

class test_app_config(app_config):
    pass

configLooader = {
    'development': development_app_config,
    'testing': test_app_config,
    'production': production_app_config
}