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
	'nti.nose_traceback_info',
	'nti.testing'
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
		'Programming Language :: Python :: Implementation :: CPython'
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
        'zope.component',
        'zope.container',
        'zope.interface',
        'zope.proxy',
        'zope.schema',
        'zope.security',
        'nti.common',
        'nti.externalization',
		'nti.schema'
	],
	extras_require={
		'test': TESTS_REQUIRE,
	},
	entry_points=entry_points
)
