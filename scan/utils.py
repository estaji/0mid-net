import logging
import subprocess

import requests

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
        url = url.removesuffix("/")
    except AttributeError:
        url = url
    return url


def rm_after_slash(url):
    """Remove / and everything after / from url"""
    url = url.split("/", 1)[0]
    return url


def pinging(url):
    """Ping a given url"""
    url = rm_http_https(url)
    url = rm_after_slash(url)
    logger.info("pinging started {{{}}}".format(url))
    output = subprocess.run(["ping", "-c", "4", url])
    if output.returncode == 0:
        result = "Ping OK"
    else:
        result = "Ping Failed"
    logger.info("pinging finished {{{}}}".format(url))
    return result


def http_check(url):
    """Send http request and return status code of a given url"""
    logger.info("http_check started {{{}}}".format(url))
    threshold = 7
    try:
        r = requests.head(url, timeout=threshold)
        code = r.status_code
        if 300 < code < 400:
            location = r.headers.get("Location", url)
            if len(location) > 50:
                location = location[:50] + "..."
            result = "{} - OK but redirected to {}".format(str(code), location)
        elif code == 200:
            result = "{} - OK".format(str(code))
        elif code == 404:
            result = "{} - OK but not found".format(str(code))
        elif code == 403:
            result = "{} - OK but forbidden".format(str(code))
        elif code == 500:
            result = "{} - Internal Server Error".format(str(code))
        elif code == 503:
            result = "{} - Service Unavailable Error".format(str(code))
        else:
            result = code
        logger.info("http_check finished {{{}}}".format(url))
        # logger.debug("status_code is {}".format(code))
        # logger.debug("result is {}".format(result))
        return result
    except (requests.ConnectionError, requests.exceptions.ReadTimeout):
        result = "Failed to connect or time out > {} seconds".format(threshold)
        logger.info("http_check finished {{{}}}".format(url))
        return result


def ssl_check(url):
    """Send request and return SSl certificate status of a given url"""
    logger.info("ssl_check started {{{}}}".format(url))
    url = rm_http_https(url)
    url = "https://" + url

    try:
        requests.get(url, verify=True, allow_redirects=False)
        result = "OK, no ssl certificate issue detected"
        return result
    except Exception as error:
        error_message = str(error)
        if error_message.find("expired") != -1:
            result = "ERROR, the ssl certificate has expired or revoked"
            # logger.debug("ssl error_message is {}".format(error_message))
            logger.info("ssl_check finished {{{}}}".format(url))
            return result
        elif error_message.find("doesn't match") != -1:
            result = "ERROR, the ssl certificate common name has mismatched"
            # logger.debug("ssl error_message is {}".format(error_message))
            logger.info("ssl_check finished {{{}}}".format(url))
            return result
        elif error_message.find("chain") != -1:
            result = "ERROR, the ssl chain is NOT valid"
            # logger.debug("ssl error_message is {}".format(error_message))
            logger.info("ssl_check finished {{{}}}".format(url))
            return result
        elif error_message.find("self-signed") != -1:
            result = "ERROR, the ssl certificate is self signed"
            # logger.debug("ssl error_message is {}".format(error_message))
            logger.info("ssl_check finished {{{}}}".format(url))
            return result
        else:
            result = """ERROR, the ssl certificate is INVALID
             (or the url is unreachable)"""
            # logger.debug("ssl error_message is {}".format(error_message))
            logger.info("ssl_check finished {{{}}}".format(url))
            return result
