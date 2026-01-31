#!/usr/bin/env python3
"""Module that defines mixins and Dragon class."""


class SwimMixin:
    """Mixin that adds swimming ability."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying ability."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that can swim and fly."""

    def roar(self):
        print("The dragon roars!")
