# file: geom2.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2018 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2018-11-14T18:40:19+0100
# Last modified: 2018-11-14T18:55:29+0100
"""2D geometry tools."""


def line(p, q):
    """Create the line function passing through points P and Q.
    By solving py = a·px + b and qy = a·qx + b.

    Arguments:
        p: Point coordinates as a 2-tuple.
        q: Point coordinates as a 2-tuple.

    Returns:
        A 2-tuple (a, b) representing the line y = ax + b
    """
    (px, py), (qx, qy) = p, q
    dx, dy = px - qx, py - qy
    if dx == 0:
        raise ValueError('y is not a function of x')
    a = dy / dx
    b = py - a * px
    return (a, b)


def intersect(p, q):
    """Solve the intersection between two lines p and q.

    Arguments:
        p: 2-tuple (a, b) representing the line y = ax + b.
        q: 2-tuple (c, d) representing the line y = cx + d.

    Returns:
        The intersection point as a 2-tuple (x, y).
    """
    (a, b), (c, d) = p, q
    if a == c:
        raise ValueError('parallel lines')
    x = (d - b) / (a - c)
    y = a*x + b
    return (x, y)
