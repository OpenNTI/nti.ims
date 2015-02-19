import codecs
from setuptools import setup, find_packages

VERSION = '0.0.0'

entry_points = {
}

TESTS_REQUIRE = [
    'fudge',
    'nose',
    'nose-timer',
    'nose-pudb',
    'nose-progressive',
    'nose2[coverage_plugin]',
    'pyhamcrest',
    'zope.testing',
    'nti.testing',
    'nti.nose_traceback_info',
]

setup(
    name='nti.ims',
    version=VERSION,
    author='Jason Madden',
    author_email='jason@nextthought.com',
    description="NTI IMS Integration",
    long_description=codecs.open('README.rst', encoding='utf-8').read(),
    license='Proprietary',
    keywords='IMS, LTI, QTI',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
		'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['nti'],
    tests_require=TESTS_REQUIRE,
    install_requires=[
        'setuptools',
        'dolmen.builtins',
        'lxml',
        'ims_lti_py',
        'nti.schema'
    ],
    extras_require={
        'test': TESTS_REQUIRE,
    },
    dependency_links=[
        'git+https://github.com/NextThought/nti.schema.git#egg=nti.schema',
        'git+https://github.com/NextThought/nti.nose_traceback_info.git#egg=nti.nose_traceback_info'
    ],
    entry_points=entry_points
)
