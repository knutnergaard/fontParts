.. highlight:: python
.. module:: fontParts.base

###
Lib
###

***********
Description
***********

The :class:`Lib <BaseLib>` object is a place to store arbitrary data for a :class:`Font <BaseFont>` or :class:`Glyph <BaseGlyph>` or :class:`Layer <BaseLayer>`. It behaves like a normal :class:`dict`, except that: 

- keys must be :class:`str` 
- values must be a :class:`~fontParts.base.annotations.LibValue`

The basic object libs are accessed through their respective :attr:`Font.lib <BaseFont.lib>`, :attr:`Glyph.lib <BaseGlyph.lib>` or :attr:`Layer.lib <BaseLayer.lib>` attributes. 

Additionally, a temporary :class:`Lib <BaseLib>` instance -- which is not saved with the font -- can be accessed with each object's ``tempLib`` attribute. 

.. note::
   
    The way lib data is stored or persisted depends on the backend. UFO-based backends typically serialize lib data into ``.plist`` files for fonts and glyphs.

********
Overview
********

.. autosummary::
    :nosignatures:

    BaseLib.copy
    BaseLib.glyph
    BaseLib.font
    BaseLib.__len__
    BaseLib.keys
    BaseLib.items
    BaseLib.values
    BaseLib.__contains__
    BaseLib.__setitem__
    BaseLib.__getitem__
    BaseLib.get
    BaseLib.__delitem__
    BaseLib.pop
    BaseLib.__iter__
    BaseLib.update
    BaseLib.clear
    BaseLib.naked
    BaseLib.changed


*********
Reference
*********

.. autoclass:: BaseLib

Copy
====

.. automethod:: BaseLib.copy

Parents
=======

.. autoattribute:: BaseLib.glyph
.. autoattribute:: BaseLib.font

Dictionary
==========

.. automethod:: BaseLib.__len__
.. automethod:: BaseLib.keys
.. automethod:: BaseLib.items
.. automethod:: BaseLib.values
.. automethod:: BaseLib.__contains__
.. automethod:: BaseLib.__setitem__
.. automethod:: BaseLib.__getitem__
.. automethod:: BaseLib.get
.. automethod:: BaseLib.__delitem__
.. automethod:: BaseLib.pop
.. automethod:: BaseLib.__iter__
.. automethod:: BaseLib.update
.. automethod:: BaseLib.clear

Environment
===========

.. automethod:: BaseLib.naked
.. automethod:: BaseLib.changed
