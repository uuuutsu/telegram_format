import abc
import typing


class GlyphType(typing.Protocol):
    identity: typing.ClassVar[str]

    @abc.abstractmethod
    def get_attrs(self) -> dict[str, typing.Any]:
        raise NotImplementedError
