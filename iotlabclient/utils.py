import sys

from coverage.annotate import os


def read_file(file_path, opt=''):
    """ Open and read a file """
    with open(os.path.expanduser(file_path), 'r' + opt) as _fd:  # expand '~'
        return _fd.read()


def read_custom_api_url():
    """ Return the customized api url from:
     * config file in <HOME_DIR>/.iotlab.api-url
     * or environment variable IOTLAB_API_URL
    """
    try:
        # try getting url from config file
        api_url = read_file('~/.iotlab.api-url').strip()
    except IOError:
        # try getting url from environment variable, None if undefined
        api_url = os.getenv('IOTLAB_API_URL')

    if api_url:
        sys.stderr.write("Using custom api_url: {}\n".format(api_url))
    return api_url
