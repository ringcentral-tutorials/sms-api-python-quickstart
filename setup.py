from setuptools import setup

setup(name='sms-api-python-quickstart',
      version='0.1.0',
      description='A quickstart tutorial to teach users to use RingCentral SMS API.',
      license='MIT',
      packages=['sms-api-python-quickstart'],
      install_requires=[
          'ringcentral',
          'python-dotenv'
      ],
      zip_safe=False)
