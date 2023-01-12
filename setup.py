from setuptools import setup

######################################################################################################
################ You May Remove All the Comments Once You Finish Modifying the Script ################
######################################################################################################

setup(
    name = 'ukbpatiming',
    version = '0.1.0',
    description = 'A python package for computing timing of device-measured physical activity from UKBiobank.',

    py_modules = ["timing"],
    package_dir = {'':'ukbpatiming'},
    long_description = open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
    long_description_content_type = "text/markdown",
    url='https://github.com/caiwet/PA-Timing-Package',
    include_package_data=True,
    install_requires = [

        'pandas ~= 1.3.5',
        'numpy ~= 1.19.5'

    ],
    keywords = ['UK Biobank', 'Physical Activity', 'Time'],
)
