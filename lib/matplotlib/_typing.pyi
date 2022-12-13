from matplotlib.path import Path
from matplotlib.markers import MarkerStyle

from typing import Union, TypeAlias, Literal

LineStyleType: TypeAlias = Union[str, tuple[float, Sequence[float]]]
FillStyleType: TypeAlias = Literal["full", "left", "right", "bottom", "top", "none"]
DrawStyleType: TypeAlias = Literal["default", "steps", "steps-pre", "steps-mid", "steps-post"]
MarkerType: TypeAlias = Union[str, Path, MarkerStyle]
MarkEveryType: TypeAlias = Union[None, int, tuple[int, int], slice, list[int], float, tuple[float, float], list[bool]]
#TODO color
Color: TypeAlias = Any

