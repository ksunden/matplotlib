from matplotlib.path import Path
from matplotlib.markers import MarkerStyle

from typing import Any, Union, Literal, Sequence

LineStyleType = Union[str, tuple[float, Sequence[float]]]
FillStyleType = Literal["full", "left", "right", "bottom", "top", "none"]
DrawStyleType = Literal["default", "steps", "steps-pre", "steps-mid", "steps-post"]
MarkerType = Union[str, Path, MarkerStyle]
MarkEveryType = Union[None, int, tuple[int, int], slice, list[int], float, tuple[float, float], list[bool]]
#TODO color
Color = Any
