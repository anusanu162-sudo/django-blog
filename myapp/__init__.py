"""Project package.

PyMySQL is a pure-Python MySQL driver that works on Windows and in CI.
Django expects a ``MySQLdb`` module, so this shim exposes PyMySQL under that
name. If mysqlclient is installed instead, remove PyMySQL from requirements.txt
and this file can stay as a harmless no-op.
"""

try:
    import pymysql

    # Django's MySQL backend checks for mysqlclient 2.2.1 or newer.
    pymysql.version_info = (2, 2, 1, "final", 0)
    pymysql.install_as_MySQLdb()
except ImportError:  # pragma: no cover - only hit when MySQL support is absent
    pass
