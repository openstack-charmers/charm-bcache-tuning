# Overview

This charm performs best-practice performance tuning of bcache devices on
SD/NVMe based installations.

## Cache Devices

Disable performance based congestion behaviour - the SSD or NVMe will in
all likelyhood always be faster than the underlying spindle:

    congested_read_threshold_us: 0
    congested_write_threshold_us: 0

## Bcache Devices

Disable writethrough of sequential data writes:

    sequential_cutoff: 0

Increase the amount of dirty data the cache device will hold before
starting to persist to the backing device:

    writeback_percent: 30

# Usage

To use this charm, simple deploy and relation to principle services:

    juju deploy bcache-tuning
    juju add-relation bcache-tuning ceph-osd
    juju add-relation bcache-tuning nova-compute

This charm presents no configuration options.
