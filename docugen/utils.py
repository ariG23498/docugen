"""Utility functions."""

import importlib
import logging
import pkgutil


def _onerror(name):
  logging.exception('Failed to load package: %r', name)


def recursive_import(root, strict=False):
  """Recursively imports all the modules under a root package.

  Args:
    root: A python package.
    strict: Bool, if `True` raise exceptions, else just log them.

  Returns:
    A list of all imported modules.
  """

  modules = []

  kwargs = {}
  # If strict=False, ignore errors during `pkgutil.walk_packages`.
  if not strict:
    kwargs = {'onerror': _onerror}

  for _, name, _ in pkgutil.walk_packages(
      root.__path__, prefix=root.__name__ + '.', **kwargs):
    try:
      modules.append(importlib.import_module(name))
    # And ignore the same set of errors if import_module fails, these are not
    # triggered by walk_packages.
    except Exception:  # pylint: disable=broad-except
      if strict:
        raise
      else:
        logging.exception('Failed to load module: %r', name)

  return modules
