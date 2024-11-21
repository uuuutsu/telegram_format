from __future__ import annotations

import dataclasses
import typing

from . import types, utils


class GlyphBase(types.GlyphType):
    identity: typing.ClassVar[str]
    __slots__: typing.ClassVar[tuple[str, ...]] = ()

    def __new__(cls, *args: typing.Any, **kwargs: typing.Any) -> GlyphBase:
        if cls is GlyphBase:
            raise TypeError(
                f"{cls.__name__} cannot be used directly. Use its concrete subclasses."
            )
        return object.__new__(cls, *args, **kwargs)

    def __init_subclass__(cls, *args: typing.Any, **kwargs: typing.Any) -> None:
        cls.identity = utils.camel_case_to_snake_case(cls.__name__)
        super().__init_subclass__()

    def get_attrs(self) -> dict[str, typing.Any]:
        return {attr: getattr(self, attr) for attr in type(self).__slots__}


glyph = dataclasses.dataclass(slots=True, frozen=True)


@glyph
class Bold(GlyphBase):
    content: types.GlyphType


@glyph
class Italic(GlyphBase):
    content: types.GlyphType


@glyph
class Underline(GlyphBase):
    content: types.GlyphType


@glyph
class Strike(GlyphBase):
    content: types.GlyphType


@glyph
class Spoiler(GlyphBase):
    content: types.GlyphType


@glyph
class InlineURL(GlyphBase):
    text: str
    url: str


@glyph
class Image(GlyphBase):
    title: str
    url: str


@glyph
class Code(GlyphBase):
    text: str


@glyph
class Pre(GlyphBase):
    text: str
    language: str


@glyph
class Quote(GlyphBase):
    content: types.GlyphType
    collapsed: bool = False
