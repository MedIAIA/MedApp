from setuptools import setup

setup(
    name='Digiez',
    version='1.0',
    description='REST API implementation in flask framework',
    author='Moncif EL KASSIMI',
    packages=[
                'digiez_api',
                'digiez_api/models',
                'digiez_api/views',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy',
        'Flask-WTF',
        'requests',
        'flask-swagger',
    ]
)
