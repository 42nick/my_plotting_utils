import sys

import pytest

# @pytest.fixture
# def capture_stdout(monkeypatch):
#     buffer = {"stdout": "", "write_calls": 0, "sprint": []}

#     def fake_write(s):
#         buffer["stdout"] += s
#         buffer["write_calls"] += 1
#         buffer["sprint"].append(s)


#     monkeypatch.setattr(sys.stdout, 'write', fake_write)
#     return buffer

@pytest.fixture
def capture_stdout(monkeypatch):

    string_buffer = {"stdout": "", "write_calls": 0, "sprint": []}

    def fake_stdout(s):
        string_buffer["stdout"] += s
        string_buffer["write_calls"] += 1
        string_buffer["sprint"].append(s)

    monkeypatch.setattr(sys.stdout, "write", fake_stdout)
    return string_buffer
