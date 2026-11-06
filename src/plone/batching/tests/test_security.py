from AccessControl import Unauthorized
from AccessControl.ZopeGuards import guarded_getattr
from AccessControl.ZopeGuards import guarded_import

import unittest


class TestModuleSecurity(unittest.TestCase):
    def test_batch_is_public(self):
        from plone.batching import Batch

        module = guarded_import("plone.batching", fromlist=["Batch"])
        self.assertIs(guarded_getattr(module, "Batch"), Batch)
        batch = Batch(range(10), 3)
        self.assertEqual(guarded_getattr(batch, "pagesize"), 3)

    def test_other_names_are_not_public(self):
        import plone.batching

        # Make sure the submodules are attributes of the package.
        import plone.batching.batch  # noqa: F401
        import plone.batching.browser  # noqa: F401
        import plone.batching.utils  # noqa: F401

        for name in (
            "allow_class",
            "allow_module",
            "ModuleSecurityInfo",
            "batch",
            "browser",
            "utils",
        ):
            if not hasattr(plone.batching, name):
                continue
            with self.subTest(name=name):
                self.assertRaises(Unauthorized, guarded_getattr, plone.batching, name)
                self.assertRaises(
                    Unauthorized,
                    guarded_import,
                    "plone.batching",
                    fromlist=[name],
                )

    def test_submodules_not_importable(self):
        # guarded_import may raise the Unauthorized from zExceptions instead.
        for name in ("plone.batching.batch", "plone.batching.utils"):
            with self.subTest(name=name):
                with self.assertRaises(Exception) as cm:
                    guarded_import(name)
                self.assertEqual(type(cm.exception).__name__, "Unauthorized")
