#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# pylint: disable=protected-access,too-many-public-methods,inherit-non-class

from hamcrest import is_
from hamcrest import raises
from hamcrest import calling
from hamcrest import assert_that

from nti.testing.matchers import verifiably_provides

from zope import component
from zope import interface

from zope.component import getGlobalSiteManager

from zope.interface.interfaces import ComponentLookupError

from nti.ims.lti import adapt_accounting_for_consumer

import nti.testing.base


ZCML_STRING = u"""
<configure    xmlns="http://namespaces.zope.org/zope"
            xmlns:i18n="http://namespaces.zope.org/i18n"
            xmlns:zcml="http://namespaces.zope.org/zcml"
            xmlns:ims="http://nextthought.com/ntp/lti">

    <include package="zope.component" file="meta.zcml" />
    <include package="zope.security" file="meta.zcml" />
    <include package="zope.component" />

    <include package="." file="meta.zcml" />

    <configure>
        <adapter factory=".tests.test_adapters.TestAdapter"
                    for=".tests.test_adapters.TestRequest"
                    provides=".tests.test_adapters.ITestAdapter"
                    name="test" />
                    
        <adapter factory=".tests.test_adapters.TestMultiAdapter"
            for=".tests.test_adapters.TestRequest .tests.test_adapters.TestFactory"
            provides=".tests.test_adapters.ITestAdapter"
            name="test2" />
    </configure>
</configure>
"""


class TestRequest(object):

    params = {'tool_consumer_instance_guid': 'test',
              'tool_consumer_info_product_family_code': 'test2'}


class TestFactory(object):
    pass


class ITestAdapter(interface.Interface):
    pass


@interface.implementer(ITestAdapter)
@component.adapter(TestRequest)
@component.named('test')
class TestAdapter(object):

    def __init__(self, request):
        pass


@interface.implementer(ITestAdapter)
@component.adapter(TestRequest)
@component.adapter(TestFactory)
@component.named('test2')
class TestMultiAdapter(object):

    def __init__(self, request, other):
        pass


class TestAdaptAccountingForConsumer(nti.testing.base.ConfiguringTestBase):

    def test_single_adapter_match(self):
        self.configure_string(ZCML_STRING)
        request = TestRequest()
        factory = TestFactory()

        # Test single adapter query
        adapter = adapt_accounting_for_consumer(request, request,
                                                ITestAdapter, query=True)
        assert_that(adapter, verifiably_provides(ITestAdapter))

        # Test single adapter get
        adapter = adapt_accounting_for_consumer(request, request,
                                                ITestAdapter, query=False)
        assert_that(adapter, verifiably_provides(ITestAdapter))

        # Test single adapter tuple query
        adapter = adapt_accounting_for_consumer(request, (request, factory),
                                                ITestAdapter, query=True)
        assert_that(adapter, verifiably_provides(ITestAdapter))

        # Test single adapter tuple get
        adapter = adapt_accounting_for_consumer(request, request,
                                                ITestAdapter, query=False)
        assert_that(adapter, verifiably_provides(ITestAdapter))

    def test_single_adapter_no_match(self):
        self.configure_string(ZCML_STRING)
        request = TestRequest()
        factory = TestFactory()

        # Test no match
        request.params = {}

        # Test single adapter query
        adapter = adapt_accounting_for_consumer(request, request,
                                                ITestAdapter, query=True)
        assert_that(adapter, is_(None))

        # Test single adapter get
        assert_that(calling(adapt_accounting_for_consumer).with_args(request, request, ITestAdapter, query=False),
                    raises(ComponentLookupError))

        # Test single adapter tuple query
        adapter = adapt_accounting_for_consumer(request, (request, factory),
                                                ITestAdapter, query=True)
        assert_that(adapter, is_(None))

        # Test single adapter tuple get
        assert_that(calling(adapt_accounting_for_consumer).with_args(request, request,
                                                                     ITestAdapter, query=False),
                    raises(ComponentLookupError))

    def test_multi_adapter_match(self):
        self.configure_string(ZCML_STRING)
        request = TestRequest()
        factory = TestFactory()

        # Test multi adapter query
        adapter = adapt_accounting_for_consumer(request, (request, factory), ITestAdapter, query=True,
                                                multi_adapter_for_tuple=True)
        assert_that(adapter, verifiably_provides(ITestAdapter))

        # Test multi adapter get
        adapter = adapt_accounting_for_consumer(request, request, ITestAdapter, query=False,
                                                multi_adapter_for_tuple=True)
        assert_that(adapter, verifiably_provides(ITestAdapter))

    def test_multi_adapter_no_match(self):

        self.configure_string(ZCML_STRING)
        request = TestRequest()
        factory = TestFactory()

        # Test no match
        request.params = {}

        # Test multi adapter query
        adapter = adapt_accounting_for_consumer(request, (request, factory), ITestAdapter, query=True,
                                                multi_adapter_for_tuple=True)
        assert_that(adapter, is_(None))

        # Test multi adapter tuple query
        assert_that(calling(adapt_accounting_for_consumer).with_args(request, request, ITestAdapter, query=False,
                                                                     multi_adapter_for_tuple=True),
                    raises(ComponentLookupError))

    def test_default(self):

        self.configure_string(ZCML_STRING)
        request = TestRequest()
        factory = TestFactory()
        request.params = {}

        gsm = getGlobalSiteManager()
        gsm.registerAdapter(TestAdapter, (TestRequest,),
                            ITestAdapter, "default")
        gsm.registerAdapter(TestMultiAdapter, (TestRequest,
                                               TestFactory), ITestAdapter, "default")

        # Test single adapter query
        adapter = adapt_accounting_for_consumer(request, request,
                                                ITestAdapter, query=True)
        assert_that(adapter, verifiably_provides(ITestAdapter))

        # Test single adapter get
        adapter = adapt_accounting_for_consumer(request, request,
                                                ITestAdapter, query=False)
        assert_that(adapter, verifiably_provides(ITestAdapter))

        # Test single adapter tuple query
        adapter = adapt_accounting_for_consumer(request, (request, factory),
                                                ITestAdapter, query=True)
        assert_that(adapter, verifiably_provides(ITestAdapter))

        # Test single adapter tuple get
        adapter = adapt_accounting_for_consumer(request, request,
                                                ITestAdapter, query=False)
        assert_that(adapter, verifiably_provides(ITestAdapter))

        # Test multi adapter query
        adapter = adapt_accounting_for_consumer(request, (request, factory), ITestAdapter, query=True,
                                                multi_adapter_for_tuple=True)
        assert_that(adapter, verifiably_provides(ITestAdapter))

        # Test multi adapter get
        adapter = adapt_accounting_for_consumer(request, request, ITestAdapter, query=False,
                                                multi_adapter_for_tuple=True)
        assert_that(adapter, verifiably_provides(ITestAdapter))

        gsm.unregisterAdapter(TestAdapter, (TestRequest,),
                              ITestAdapter, "default")
        gsm.unregisterAdapter(TestMultiAdapter, (TestRequest, TestFactory),
                              ITestAdapter, "default")
