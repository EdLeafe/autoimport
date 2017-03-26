from __future__ import print_function
import os_traits
print("dir(c1)", dir(os_traits.bb.cc.c1))
print("(c2)", dir(os_traits.bb.cc.c2))

print("os_traits.aa.a1.foo", os_traits.aa.a1.foo)
print("os_traits.bb.b1.foo", os_traits.bb.b1.foo)
print("os_traits.bb.cc.c1.foo", os_traits.bb.cc.c1.foo)
print("os_traits.bb.cc.dd.d1.foo", os_traits.bb.cc.dd.d1.foo)
print("os_traits.ee.e1.foo", os_traits.ee.e1.foo)
