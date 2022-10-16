import subprocess
import logging


logger = logging.getLogger(__name__)


def rm_http_https(url):
    """Remove http or https from a given url"""
    url = url.replace("http://", "")
    url = url.replace("https://", "")
    return url


def rm_suffix_slash(url):
    """Remove / from end of a url"""
    try:
        # if url.endswith('/'):
        #    url = url[:-1]
        url = url.removesuffix('/')
    except AttributeError:
        url = url
    return url


def rm_after_slash(url):
    """Remove / and everything after / from url"""
    url = url.split('/', 1)[0]
    return url


def pinging(url):
    """Ping a given url"""
    url = rm_http_https(url)
    url = rm_after_slash(url)
    output = subprocess.run(["ping", "-c 4", url])
    if output.returncode == 0:
        result = 'Ping OK'
    else:
        result = 'Ping Failed'
    logger.info("pinging finished {{{}}}".format(url))
    return result
