import pytest

import sys
import io

from measure import CloudWatchDriver, DESC, HAS_CANCEL, VERSION

measure_json_stdin = '''\
{
    "metrics": [
        "networkPacketsIn_ws2012_sandbox_asg",
        "networkPacketsIn_ws2012_sandbox_asg_PerInstance",
        "networkPacketsOut_ws2012_sandbox_asg",
        "networkPacketsOut_ws2012_sandbox_asg_PerInstance"
    ]
}
'''

def test_info(monkeypatch):
    with monkeypatch.context() as m:
        # replicate command line arguments fed in by servo
        m.setattr(sys, 'argv', ['', '--info', '1234'])
        driver = CloudWatchDriver(cli_desc=DESC, supports_cancel=HAS_CANCEL, version=VERSION)
        with pytest.raises(SystemExit) as exit_exception:
            driver.run()
        assert exit_exception.type == SystemExit
        assert exit_exception.value.code == 0

def test_describe(monkeypatch):
    with monkeypatch.context() as m:
        # replicate command line arguments fed in by servo
        m.setattr(sys, 'argv', ['', '--describe', '1234'])
        driver = CloudWatchDriver(cli_desc=DESC, supports_cancel=HAS_CANCEL, version=VERSION)
        with pytest.raises(SystemExit) as exit_exception:
            driver.run()
        assert exit_exception.type == SystemExit
        assert exit_exception.value.code == 0

def test_measure(monkeypatch):
    with monkeypatch.context() as m:
        # replicate command line arguments fed in by servo
        m.setattr(sys, 'argv', ['', '1234'])
        m.setattr(sys, 'stdin', io.StringIO(measure_json_stdin))
        driver = CloudWatchDriver(cli_desc=DESC, supports_cancel=HAS_CANCEL, version=VERSION)
        driver.run()
        assert True