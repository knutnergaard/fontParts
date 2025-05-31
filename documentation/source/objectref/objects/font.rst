.. highlight:: python
.. module:: fontParts.base

####
Font
####

.. note::

	This section needs to contain the following:

	* description of what this is ✓
	* sub-object with basic usage ✓
	* bridge to default layer for glyphs for backwards compatibility ✗
	* glyph interaction with basic usage ✗

***********
Description
***********

The :class:`Font <BaseFont>` object is the central part that connects all glyphs with font information like names, key dimensions etc.

A :class:`Font <BaseFont>` contains one or more :class:`Layer <BaseLayer>` instances, each of which represents a collection of glyphs in a specific drawing or editing context. By default, most operations interact with the font's default layer.

:class:`Font <BaseFont>` instances behave like dictionaries mapping glyph names to :class:`Glyph <BaseGlyph>` instances — specifically those in the default layer. If the glyph does not exist, the font will raise an :class:`IndexError`.

In addition to glyphs and layers, the font has several important sub-objects:

- A :class:`Kerning <BaseKerning>` object for managing kerning pairs, accessible through
  the :attr:`~BaseFont.kerning` attribute.
- An :class:`Info <BaseInfo>` object storing font-wide metadata like font names, key dimensions, and flags, accessible through the :attr:`~BaseFont.info` attribute. 
- A :class:`Lib <BaseLib>` object that stores arbitrary metadata, behaving like a :class:`dict`, accessible through the :attr:`~BaseFont.lib` attribute.

********
Overview
********

Copy
====

.. autosummary::
    :nosignatures:

    BaseFont.copy

File Operations
===============

.. autosummary::
    :nosignatures:

    BaseFont.path
    BaseFont.save
    BaseFont.generate

Sub-Objects
===========

.. autosummary::
    :nosignatures:

    BaseFont.info
    BaseFont.groups
    BaseFont.kerning
    BaseFont.features
    BaseFont.lib
    BaseFont.tempLib

Layers
======

.. autosummary::
    :nosignatures:

    BaseFont.layers
    BaseFont.layerOrder
    BaseFont.defaultLayer
    BaseFont.getLayer
    BaseFont.newLayer
    BaseFont.removeLayer
    BaseFont.insertLayer
    BaseFont.duplicateLayer

Glyphs
======

.. autosummary::
    :nosignatures:

    BaseFont.__len__
    BaseFont.keys
    BaseFont.glyphOrder
    BaseFont.__iter__
    BaseFont.__contains__
    BaseFont.__getitem__
    BaseFont.newGlyph
    BaseFont.insertGlyph
    BaseFont.removeGlyph

Guidelines
==========

.. autosummary::
    :nosignatures:

    BaseFont.guidelines
    BaseFont.appendGuideline
    BaseFont.removeGuideline
    BaseFont.clearGuidelines

Interpolation
=============

.. autosummary::
    :nosignatures:

    BaseFont.isCompatible
    BaseFont.interpolate

Kerning
=======

.. autosummary::
    :nosignatures:

    BaseFont.getFlatKerning

Mapping
=======

.. autosummary::
    :nosignatures:

    BaseFont.getCharacterMapping
    BaseFont.getReverseComponentMapping

Selection
=========

.. autosummary::
    :nosignatures:

    BaseFont.selectedLayers
    BaseFont.selectedLayerNames
    BaseFont.selectedGuidelines

Normalization
=============

.. autosummary::
    :nosignatures:

    BaseFont.round
    BaseFont.autoUnicodes

Environment
===========

.. autosummary::
    :nosignatures:

    BaseFont.naked
    BaseFont.changed

*********
Reference
*********

.. autoclass:: BaseFont

Copy
====

.. automethod:: BaseFont.copy

File Operations
===============

.. autoattribute:: BaseFont.path
.. automethod:: BaseFont.save
.. automethod:: BaseFont.close
.. automethod:: BaseFont.generate

Sub-Objects
===========

.. autoattribute:: BaseFont.info
.. autoattribute:: BaseFont.groups
.. autoattribute:: BaseFont.kerning
.. autoattribute:: BaseFont.features
.. autoattribute:: BaseFont.lib
.. autoattribute:: BaseFont.tempLib

Layers
======

.. autoattribute:: BaseFont.layers
.. autoattribute:: BaseFont.layerOrder
.. autoattribute:: BaseFont.defaultLayer
.. autoattribute:: BaseFont.defaultLayerName
.. automethod:: BaseFont.getLayer
.. automethod:: BaseFont.newLayer
.. automethod:: BaseFont.removeLayer
.. automethod:: BaseFont.insertLayer
.. automethod:: BaseFont.duplicateLayer
.. automethod:: BaseFont.swapLayerNames

Glyphs
======

Interacting with glyphs at the font level is a shortcut for interacting with glyphs in the default layer. ::

	>>> glyph = font.newGlyph("A")

Does the same thing as::

	>>> glyph = font.getLayer(font.defaultLayerName).newGlyph("A")

.. automethod:: BaseFont.__len__
.. automethod:: BaseFont.keys
.. autoattribute:: BaseFont.glyphOrder
.. automethod:: BaseFont.__iter__
.. automethod:: BaseFont.__contains__
.. automethod:: BaseFont.__getitem__
.. automethod:: BaseFont.newGlyph
.. automethod:: BaseFont.insertGlyph
.. automethod:: BaseFont.removeGlyph

Guidelines
==========

.. autoattribute:: BaseFont.guidelines
.. automethod:: BaseFont.appendGuideline
.. automethod:: BaseFont.removeGuideline
.. automethod:: BaseFont.clearGuidelines

Interpolation
=============

.. automethod:: BaseFont.isCompatible
.. automethod:: BaseFont.interpolate

Kerning
=======

.. automethod:: BaseFont.getFlatKerning

Mapping
=======

.. automethod:: BaseFont.getCharacterMapping
.. automethod:: BaseFont.getReverseComponentMapping

Selection
=========

.. autoattribute:: BaseFont.selectedLayers
.. autoattribute:: BaseFont.selectedLayerNames
.. autoattribute:: BaseFont.selectedGuidelines

Normalization
=============

.. automethod:: BaseFont.round
.. automethod:: BaseFont.autoUnicodes

Environment
===========

.. automethod:: BaseFont.naked
.. automethod:: BaseFont.changed
