from typing import Any, Iterable, List, Optional, Tuple, Union, overload

from pygame.bufferproxy import BufferProxy
from pygame.color import Color
from pygame.rect import FRect, Rect

from ._common import (
    ColorValue,
    Coordinate,
    Literal,
    RectValue,
    RGBAOutput,
    Sequence,
)

_ViewKind = Literal[
    "0",
    "1",
    "2",
    "3",
    b"0",
    b"1",
    b"2",
    b"3",
    "r",
    "g",
    "b",
    "a",
    "R",
    "G",
    "B",
    "A",
    b"r",
    b"g",
    b"b",
    b"a",
    b"R",
    b"G",
    b"B",
    b"A",
]

class Surface:
    _pixels_address: int
    @overload
    def __init__(
        self,
        size: Coordinate,
        flags: int = 0,
        depth: int = 0,
        masks: Optional[ColorValue] = None,
    ) -> None: ...
    @overload
    def __init__(
        self,
        size: Coordinate,
        flags: int = 0,
        surface: Surface = ...,
    ) -> None: ...
    def __copy__(self) -> Surface: ...
    def __deepcopy__(self, memo) -> Surface: ...
    copy = __copy__
    def blit(
        self,
        source: Surface,
        dest: Union[Coordinate, RectValue],
        area: Optional[RectValue] = None,
        special_flags: int = 0,
    ) -> Rect: ...
    def blits(
        self,
        blit_sequence: Iterable[
            Union[
                Tuple[Surface, Union[Coordinate, RectValue]],
                Tuple[Surface, Union[Coordinate, RectValue], Union[RectValue, int]],
                Tuple[Surface, Union[Coordinate, RectValue], RectValue, int],
            ]
        ],
        doreturn: Union[int, bool] = 1,
    ) -> Union[List[Rect], None]: ...
    def fblits(
        self,
        blit_sequence: Iterable[Tuple[Surface, Union[Coordinate, RectValue]]],
        special_flags: int = 0,
    ) -> None: ...
    @overload
    def convert(self, surface: Surface) -> Surface: ...
    @overload
    def convert(self, depth: int, flags: int = 0) -> Surface: ...
    @overload
    def convert(self, masks: ColorValue, flags: int = 0) -> Surface: ...
    @overload
    def convert(self) -> Surface: ...
    def convert_alpha(self) -> Surface: ...
    def fill(
        self,
        color: ColorValue,
        rect: Optional[RectValue] = None,
        special_flags: int = 0,
    ) -> Rect: ...
    def scroll(self, dx: int = 0, dy: int = 0) -> None: ...
    @overload
    def set_colorkey(self, color: ColorValue, flags: int = 0) -> None: ...
    @overload
    def set_colorkey(self, color: None) -> None: ...
    def get_colorkey(self) -> Optional[RGBAOutput]: ...
    @overload
    def set_alpha(self, value: int, flags: int = 0) -> None: ...
    @overload
    def set_alpha(self, value: None) -> None: ...
    def get_alpha(self) -> Optional[int]: ...
    def lock(self) -> None: ...
    def unlock(self) -> None: ...
    def mustlock(self) -> bool: ...
    def get_locked(self) -> bool: ...
    def get_locks(self) -> Tuple[Any, ...]: ...
    def get_at(self, x_y: Coordinate) -> Color: ...
    def set_at(self, x_y: Coordinate, color: ColorValue) -> None: ...
    def get_at_mapped(self, x_y: Coordinate) -> int: ...
    def get_palette(self) -> List[Color]: ...
    def get_palette_at(self, index: int) -> Color: ...
    def set_palette(self, palette: Sequence[ColorValue]) -> None: ...
    def set_palette_at(self, index: int, color: ColorValue) -> None: ...
    def map_rgb(self, color: ColorValue) -> int: ...
    def unmap_rgb(self, mapped_int: int) -> Color: ...
    def set_clip(self, rect: Optional[RectValue]) -> None: ...
    def get_clip(self) -> Rect: ...
    @overload
    def subsurface(self, rect: RectValue) -> Surface: ...
    @overload
    def subsurface(self, left_top: Coordinate, width_height: Coordinate) -> Surface: ...
    @overload
    def subsurface(
        self, left: float, top: float, width: float, height: float
    ) -> Surface: ...
    def get_parent(self) -> Surface: ...
    def get_abs_parent(self) -> Surface: ...
    def get_offset(self) -> Tuple[int, int]: ...
    def get_abs_offset(self) -> Tuple[int, int]: ...
    def get_size(self) -> Tuple[int, int]: ...
    def get_width(self) -> int: ...
    def get_height(self) -> int: ...
    def get_rect(self, **kwargs: Any) -> Rect: ...
    def get_frect(self, **kwargs: Any) -> FRect: ...
    def get_bitsize(self) -> int: ...
    def get_bytesize(self) -> int: ...
    def get_flags(self) -> int: ...
    def get_pitch(self) -> int: ...
    def get_masks(self) -> RGBAOutput: ...
    def set_masks(self, color: ColorValue) -> None: ...
    def get_shifts(self) -> RGBAOutput: ...
    def set_shifts(self, color: ColorValue) -> None: ...
    def get_losses(self) -> RGBAOutput: ...
    def get_bounding_rect(self, min_alpha: int = 1) -> Rect: ...
    def get_view(self, kind: _ViewKind = "2") -> BufferProxy: ...
    def get_buffer(self) -> BufferProxy: ...
    def get_blendmode(self) -> int: ...
    def premul_alpha(self) -> Surface: ...

SurfaceType = Surface
