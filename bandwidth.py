import math


def get_seconds(time: float, unit: str) -> float:
    """Converts a time represented as a number followed by a unit to seconds

    Feel free to use datetime.timedelta or code this yourself, but make sure
    that you understand how to perform these conversions.

    >>> get_seconds(1, "minute")
    60

    >>> get_seconds(5, "minutes")
    300

    >>> get_seconds(4, "days")
    345600

    >>> get_seconds(1, "week")
    604800

    >>> get_seconds(8.3, "seconds")
    8.3

    >>> get_seconds(.1, "hours")
    360.0

    >>> get_seconds(1, "ages")
    Traceback (most recent call last):
    ...
    ValueError: Unsupported unit: ages
    """

    return 0.0


def get_size_bits(size: float, unit: str) -> float:
    """Converts a number and unit representing stored size to a number of bits

    This function assumes that 1000 bytes = 1 KB.

    >>> get_size_bits(1, "KB")
    8000.0

    >>> get_size_bits(4, "MB")
    32000000.0

    >>> get_size_bits(3, "GB")
    24000000000.0

    >>> get_size_bits(1.5, "TB")
    12000000000000.0

    >>> get_size_bits(8.4, "PB")
    6.72e+16

    >>> get_size_bits(1, "words")
    Traceback (most recent call last):
    ...
    ValueError: Unsupported unit: words
    """

    return 0.0


def compute_effective_bandwidth(
    size: float, size_unit: str, time: float, time_unit: str
):
    """Computes the effective bandwidth of a storage device being transported

    Return value is always in Mb/s (megabits per second).

    Note that data a rest is typically measured in bytes, so be sure to
    convert accordingly.

    Examples:

    >>> round(compute_effective_bandwidth(6, "TB", 3, "days"), 3)
    185.185

    >>> round(compute_effective_bandwidth(1, "PB", 1, "week"), 3)
    13227.513

    >>> round(compute_effective_bandwidth(700, "MB", 1, "minute"), 3)
    93.333

    >>> round(compute_effective_bandwidth(100, "GB", 16, "hours"), 3)
    13.889
    """

    return 0.0


def convert_db_to_snr(db: float) -> float:
    """Converts a decibel value to a signal to noise ratio

    >>> convert_db_to_snr(10)
    10.0

    >>> convert_db_to_snr(20)
    100.0

    >>> convert_db_to_snr(30)
    1000.0

    >>> round(convert_db_to_snr(24.2), 3)
    263.027
    """

    return 0.0


def get_levels_bandwidth(analog_bandwidth: float, levels: float) -> float:
    """Computes the maximum digital bandwidth of an analog channel given signal level count

     - analog_bandwidth is the bandwidth of the channel in MHz
     - levels is the number of signal levels used

    Values are computed using theorems from Nyquist and Shannon. In particular:

    2 B \log_2{V}

    >>> get_levels_bandwidth(20, 2)
    40.0

    >>> get_levels_bandwidth(2, 1024)
    40.0

    >>> get_levels_bandwidth(1, 2)
    2.0

    >>> get_levels_bandwidth(0, 2)
    0.0

    >>> round(get_levels_bandwidth(.003, 8), 3)
    0.018
    """

    return 0.0


def get_snr_bandwidth(analog_bandwidth: float, snr: float, snr_in_db: bool) -> float:
    """Computes the maximum digital bandwidth of an analog channel given an SNR

     - analog_bandwidth is the bandwidth of the channel in MHz
     - snr is the signal to noise ratio
     - snr_in_db is true if the provided snr is measured in decibels

    Values are computed using theorems from Nyquist and Shannon. In particular:

    B \log_2(1 + {S \over N})

    Examples:

    >>> round(get_snr_bandwidth(1.5, 20, True), 3)
    9.966

    >>> int(get_snr_bandwidth(12, 30, True))
    119

    >>> int(get_snr_bandwidth(2200, 1000, False))
    21924
    """

    return 0.0
