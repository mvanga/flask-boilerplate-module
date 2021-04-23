# =============================================================================
# Utility Functions
# =============================================================================

def api_response(status, data=None, message=None, code=None, http_code=200):
    """Build and return a JSON API response in the JSend format"""
    ret = {'status': status}
    ret['data'] = data
    if message is not None:
        ret['message'] = message
    if code is not None:
        ret['code'] = code
    return ret, code


def api_success(data=None, http_code=200):
    """Returns a 'success' JSend response."""
    return api_response('success', data=data, http_code=http_code)


def api_fail(data, http_code=400):
    """Returns a 'fail' JSend response."""
    return api_response('fail', data=data, http_code=http_code)


def api_error(message, data=None, code=None, http_code=500):
    """Returns an 'error' JSend response."""
    return api_response('error', data, message, code, http_code)

# NOTE: SECTION:UTILITIES: Your utility functions go here...

