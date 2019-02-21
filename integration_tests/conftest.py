import pytest


def pytest_addoption(parser):
    parser.addoption('--signup', action='store_true', dest="signup",
                     default=False, help="enable signup-activate tests")


def pytest_configure(config):
    if not config.option.signup:
        setattr(config.option, 'markexpr', 'not signup')
