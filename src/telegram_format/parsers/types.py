import abc
import typing

from src.telegram_format import ir

TIn = typing.TypeVar("TIn", contravariant=True)


class ParserType(typing.Protocol[TIn]):
    @abc.abstractmethod
    def parse(self, __data: TIn) -> ir.GlyphType:
        raise NotImplementedError
