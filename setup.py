from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='mqtt_wrapper',
      version='0.1',
      description='wrapper for paho mqtt client',
      long_description=readme(),
      url='https://github.com/EmaroLab/mqtt_wrapper.git',
      author='Alessandro Carfi',
      author_email='carfi.alessandro@gmail.com',
      license='MIT',
      packages=['mqtt_wrapper'],
      zip_safe=False)
