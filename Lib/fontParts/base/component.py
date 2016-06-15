import weakref
from fontTools.misc import transform
from fontParts.base import validators
from fontParts.base.errors import FontPartsError
from fontParts.base.base import (
    BaseObject, TransformationMixin, dynamicProperty)


class BaseComponent(BaseObject, TransformationMixin):

    copyAttributes = (
        "baseGlyph",
        "transformation"
    )

    # -------
    # Parents
    # -------

    def getParent(self):
        """
        This is a backwards compatibility method.
        """
        return self.glyph

    # Glyph

    _glyph = None

    glyph = dynamicProperty("glyph", "The component's parent glyph.")

    def _get_glyph(self):
        if self._glyph is None:
            return None
        return self._glyph()

    def _set_glyph(self, glyph):
        assert self._glyph is None
        if glyph is not None:
            glyph = weakref.ref(glyph)
        self._glyph = glyph

    # Layer

    layer = dynamicProperty("layer", "The component's parent layer.")

    def _get_layer(self):
        if self._glyph is None:
            return None
        return self.glyph.layer

    # Font

    font = dynamicProperty("font", "The component's parent font.")

    def _get_font(self):
        if self._glyph is None:
            return None
        return self.glyph.font

    # ----------
    # Attributes
    # ----------

    # baseGlyph

    baseGlyph = dynamicProperty("base_baseGlyph", "The glyph the component references.")

    def _get_base_baseGlyph(self):
        value = self._get_baseGlyph()
        value = validators.validateGlyphName(value)
        return value

    def _set_base_baseGlyph(self, value):
        value = validators.validateGlyphName(value)
        self._set_baseGlyph(value)

    def _get_baseGlyph(self):
        """
        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def _set_baseGlyph(self, value):
        """
        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    # transformation

    transformation = dynamicProperty("base_transformation", "The component's transformation matrix.")

    def _get_base_transformation(self):
        value = self._get_transformation()
        value = validators.validateTransformationMatrix(value)
        return value

    def _set_base_transformation(self, value):
        value = validators.validateTransformationMatrix(value)
        self._set_transformation(value)

    def _get_transformation(self):
        """
        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def _set_transformation(self, value):
        """
        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    # offset

    offset = dynamicProperty("base_offset", "The component's offset.")

    def _get_base_offset(self):
        value = self._get_offset()
        value = validators.validateTransformationOffset(value)
        return value

    def _set_base_offset(self, value):
        value = validators.validateTransformationOffset(value)
        self._set_scale(value)

    def _get_offset(self):
        """
        Subclasses may override this method.
        """
        sx, sxy, syx, sy, ox, oy = self.transformation
        return ox, oy

    def _set_offset(self, value):
        """
        Subclasses may override this method.
        """
        sx, sxy, syx, sy, ox, oy = self.transformation
        ox, oy = value
        self.transformation = sx, sxy, syx, sy, ox, oy

    # scale

    scale = dynamicProperty("base_scale", "The component's scale.")

    def _get_base_scale(self):
        value = self._get_scale()
        value = validators.validateTransformationScale(value)
        return value

    def _set_base_scale(self, value):
        value = validators.validateTransformationScale(value)
        self._set_scale(value)

    def _get_scale(self):
        """
        Subclasses may override this method.
        """
        sx, sxy, syx, sy, ox, oy = self.transformation
        return sx, sy

    def _set_scale(self, value):
        """
        Subclasses may override this method.
        """
        sx, sxy, syx, sy, ox, oy = self.transformation
        sx, sy = value
        self.transformation = sx, sxy, syx, sy, ox, oy

    # --------------
    # Identification
    # --------------

    # index

    index = dynamicProperty("base_index", "The index of the component within the ordered list of the parent glyph's components..")

    def _get_base_index(self):
        glyph = self.glyph
        if glyph is None:
            return None
        value = self._get_index()
        value = validators.validateIndex(value)
        return value

    def _set_base_index(self, value):
        glyph = self.glyph
        if glyph is None:
            raise FontPartsError("The component does not belong to a glyph.")
        value = validators.validateIndex(value)
        componentCount = len(glyph.components)
        if value < 0:
            value = -(value % componentCount)
        if value >= componentCount:
            value = componentCount
        self._set_index(value)

    def _get_index(self):
        """
        Subclasses may override this method.
        """
        glyph = self.glyph
        return glyph.components.index(self)

    def _set_index(self, value):
        """
        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    # identifier

    identifier = dynamicProperty("base_identifier", "The unique identifier for the component.")

    def _get_base_identifier(self):
        value = self._get_identifier()
        if value is not None:
            value = validators.validateIdentifier(value)
        return value

    def _get_identifier(self):
        """
        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    # ----
    # Pens
    # ----

    def draw(self, pen):
        """
        Draw the component with the given Pen.
        """
        self._draw(pen)

    def _draw(self, pen, **kwargs):
        """
        Subclasses may override this method.
        """
        from ufoLib.pointPen import PointToSegmentPen
        adapter = PointToSegmentPen(pen)
        self.drawPoints(adapter)

    def drawPoints(self, pen):
        """
        Draw the contour with the given PointPen.
        """
        self._drawPoints(pen)

    def _drawPoints(self, pen, **kwargs):
        """
        Subclasses may override this method.
        """
        # The try: ... except TypeError: ...
        # handles backwards compatibility with
        # point pens that have not been upgraded
        # to point pen protocol 2.
        try:
            pen.addComponent(self.baseGlyph, self.transformation, identifier=self.identifier)
        except TypeError:
            pen.addComponent(self.baseGlyph, self.transformation)

    # --------------
    # Transformation
    # --------------

    def _transformBy(self, matrix, origin=None, originOffset=None, **kwargs):
        """
        Subclasses may override this method.
        """
        t = transform.Transform(*matrix)
        transformation = t.transform(self.transformation)
        self.transformation = tuple(transformation)
        if originOffset != (0, 0):
            self.moveBy(originOffset)

    # -------------
    # Normalization
    # -------------

    def round(self):
        """
        Round offset coordinates.
        """
        self._round()

    def _round(self):
        """
        Subclasses may override this method.
        """
        x, y = self.offset
        x = int(round(x))
        y = int(round(y))
        self.offset = (x, y)

    def decompose(self):
        """
        Decompose the component.
        """
        glyph = self.glyph
        if glyph is None:
            raise FontPartsError("The component does not belong to a glyph.")
        self._decompose()

    def _decompose(self):
        """
        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    # ------------
    # Data Queries
    # ------------

    def pointInside(self, point):
        """
        Determine if point is in the black or white of the component.

        point must be an (x, y) tuple.
        """
        point = validators.validateCoordinateTuple(point)
        return self._pointInside(point)

    def _pointInside(self, point):
        """
        Subclasses may override this method.
        """
        from fontTools.pens.pointInsidePen import PointInsidePen
        pen = PointInsidePen(glyphSet=None, testPoint=point, evenOdd=False)
        self.draw(pen)
        return pen.getResult()

    bounds = dynamicProperty("bounds", "The bounds of the component: (xMin, yMin, xMax, yMax) or None.")

    def _get_base_bounds(self):
        value = self._get_bounds()
        if value is not None:
            value = validators.validateBoundingBox(value)
        return value

    def _get_bounds(self):
        """
        Subclasses may override this method.
        """
        from fontTools.pens.boundsPen import BoundsPen
        pen = BoundsPen(self.layer)
        self.draw(pen)
        return pen.bounds