import time
from functools import partial

import pytest
from _pytest.terminal import TerminalReporter

__all__ = ["pytest_terminal_summary"]


def _custom_short_summary(terminalreporter: TerminalReporter):
    total_count = 0
    for k, v in terminalreporter.stats.items():
        if k:
            total_count += len(v)
    deselected_cases = terminalreporter.stats.get("deselected", [])
    failed_cases = terminalreporter.stats.get("failed", [])
    passed_cases = terminalreporter.stats.get("passed", [])
    total_duration = time.time() - terminalreporter._sessionstarttime

    terminalreporter.write_sep(
        "=",
        "Short Report Summary",
        red=bool(failed_cases),
        green=(not bool(failed_cases)),
        bold=True,
    )

    terminalreporter.write(
        "Total Test Duration: {0:.2f} seconds".format(total_duration), bold=True
    )
    terminalreporter.write("\n")

    terminalreporter.write("Total Tests Collected: {}".format(total_count), bold=True)
    terminalreporter.write("\n")

    terminalreporter.write(
        "Deselected Tests: {}".format(len(deselected_cases)), bold=True
    )
    terminalreporter.write("\n")

    terminalreporter.write("Passed Count: {}".format(len(passed_cases)), bold=True)
    terminalreporter.write("\n")

    terminalreporter.write("Failed Count: {}".format(len(failed_cases)), bold=True)
    terminalreporter.write("\n")

    for failed in failed_cases:
        terminalreporter.write("\t")
        terminalreporter.write(failed.nodeid, yellow=True)
        terminalreporter.write("\n")

    terminalreporter.write_sep(
        "=",
        "End of Short Report Summary",
        red=bool(failed_cases),
        green=(not bool(failed_cases)),
        bold=True,
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_terminal_summary(terminalreporter: TerminalReporter):
    yield
    custom_short_summary = partial(_custom_short_summary, terminalreporter)

    terminalreporter.short_test_summary = custom_short_summary
