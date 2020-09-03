from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

base = 'Console'

executables = [
    Executable('LoadScreenDetector.py', base=base)
]

packages = ["os", "numpy", "numpy.core._methods", "matplotlib", "random", "opencv", "mpl_toolkits"]

setup(name='LoadScreenDetector',
      version = '1.0',
      description = 'test',
      options = dict(build_exe = buildOptions),
      executables = executables)
