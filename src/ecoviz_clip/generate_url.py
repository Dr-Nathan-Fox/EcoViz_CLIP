def generateURL(license):
    """
    Generates a URL for the image's license based on a given license type.

    Args:
        license (str): The license type of the image.

    Returns:
        str: A URL string pointing to the license details. Returns None if the license type is unrecognized.
    """
    if not license:
        return None

    # Map for known license formats
    license_map = {
        'cc-by-sa-3.0': 'https://creativecommons.org/licenses/by-sa/3.0/',
        'cc-by-sa-2.5': 'https://creativecommons.org/licenses/by-sa/2.5/',
        'cc-by-sa-4.0': 'https://creativecommons.org/licenses/by-sa/4.0/',
        'pd': 'https://creativecommons.org/publicdomain/mark/1.0/',
        'cc-by-2.0': 'https://creativecommons.org/licenses/by/2.0/',
        'cc-by-3.0': 'https://creativecommons.org/licenses/by/3.0/',
        'cc-by-2.5': 'https://creativecommons.org/licenses/by/2.5/',
        'cc0': 'https://creativecommons.org/publicdomain/zero/1.0/',
        'cc-by-sa-2.0': 'https://creativecommons.org/licenses/by-sa/2.0/',
        'cc-by-sa-1.0': 'https://creativecommons.org/licenses/by-sa/1.0/'
    }

    return license_map.get(license, None)