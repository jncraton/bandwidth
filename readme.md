Bandwidth Calculator
====================

A Python module to provide bandwidth calculations

Features
--------

- `compute_effective_bandwidth` - Effective bandwidth for transported storage devices (e.g. [AWS Snowmobile](https://aws.amazon.com/snowmobile/))
- `get_levels_bandwidht` - Max digital bandwidth for channels with known numbers of discrete signal levels
- `get_snr_bandwidth` - Max digital bandwidth for channels with known SNR

Testing
-------

Once complete, this module should pass the following tests:

```sh
python3 -m doctest bandwidth.py
```

Tests can also be run using `make`.
