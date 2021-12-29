import io

from setuptools import setup, find_packages

with io.open("README.md", "rt", encoding="utf8") as f:
    long_description = f.read()
setup(
    name="flask-deemer",
    version="0.1.0",
    keywords=("python framework", "xxx"),
    description="A Simple python framework implemented by flask",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT Licence",
    url="https://github.com/lixing225yu/flask-deemer",
    author="xingyu.li",
    author_email="lxy2325@126.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    platforms="any",
    install_requires=[
        'addict>=2.4.0',
        'blinker>=1.4',
        # 'casbin==1.15.2',
        'celery==5.2.3',
        'flask>=2.0.2',
        'flask_sqlalchemy==2.5.1',
        'pyaml>=21.10.1',
        'pydantic==1.8.2',
        'pymysql>=1.0.2',
        'redis-py-cluster>=2.1.3',
        'simplejson>=3.17.5',
        'sqlalchemy==1.4.29',
    ],
    extras_require={},
    scripts=[],
    entry_points={}
)
