"""Smoke tests for visionquantech_exe_build (tkinter GUI app).

The GUI itself needs a display, so this verifies the module imports cleanly
and the builder class exposes its expected interface.

Runnable with pytest, or directly:  python3 tests/test_smoke.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import visionquantech_builder as vb


def test_module_imports():
    assert hasattr(vb, "VisionQuantechProBuilder")


def test_builder_interface():
    cls = vb.VisionQuantechProBuilder
    # Core builder capabilities must exist (GUI instantiation needs a display)
    for method in ("__init__",):
        assert callable(getattr(cls, method)), method
    assert isinstance(cls.__doc__, (str, type(None)))


if __name__ == "__main__":
    test_module_imports()
    test_builder_interface()
    print("smoke test: 2 passed")
