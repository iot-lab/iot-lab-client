# This file is a part of IoT-LAB client
# Copyright (C) 2019 INRIA (Contact: admin@iot-lab.info)
# Contributor(s) : see AUTHORS file
#
# This software is governed by the CeCILL license under French law
# and abiding by the rules of distribution of free software.  You can  use,
# modify and/ or redistribute the software under the terms of the CeCILL
# license as circulated by CEA, CNRS and INRIA at the following URL
# http://www.cecill.info.
#
# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.

import pytest  # noqa: F401


def pytest_addoption(parser):
    parser.addoption('--signup', action='store_true', dest="signup",
                     default=False, help="enable signup-activate tests")


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "signup: mark test as requiring a signup flow"
                   "(access to an email account)")


def pytest_collection_modifyitems(config, items):
    if config.getoption("--signup"):
        # --signup given in cli: do not skip signup tests
        return
    skip_signup = pytest.mark.skip(reason="need --signup option to run")
    for item in items:
        if "signup" in item.keywords:
            item.add_marker(skip_signup)
