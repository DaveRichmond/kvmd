# ========================================================================== #
#                                                                            #
#    KVMD - The main Pi-KVM daemon.                                          #
#                                                                            #
#    Copyright (C) 2018  Maxim Devaev <mdevaev@gmail.com>                    #
#                                                                            #
#    This program is free software: you can redistribute it and/or modify    #
#    it under the terms of the GNU General Public License as published by    #
#    the Free Software Foundation, either version 3 of the License, or       #
#    (at your option) any later version.                                     #
#                                                                            #
#    This program is distributed in the hope that it will be useful,         #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of          #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           #
#    GNU General Public License for more details.                            #
#                                                                            #
#    You should have received a copy of the GNU General Public License       #
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.  #
#                                                                            #
# ========================================================================== #


import operator
import functools

from typing import Tuple
from typing import List
from typing import Dict
from typing import Hashable
from typing import TypeVar


# =====
def merge(dest: Dict, src: Dict) -> None:
    for key in src:
        if key in dest:
            if isinstance(dest[key], dict) and isinstance(src[key], dict):
                merge(dest[key], src[key])
                continue
        dest[key] = src[key]


def rget(dct: Dict, *keys: Hashable) -> Dict:
    result = functools.reduce((lambda nxt, key: nxt.get(key, {})), keys, dct)
    if not isinstance(result, dict):
        raise TypeError(f"Not a dict as result: {result!r} from {dct!r} at {list(keys)}")
    return result


_DictKeyT = TypeVar("_DictKeyT")
_DictValueT = TypeVar("_DictValueT")


def sorted_kvs(dct: Dict[_DictKeyT, _DictValueT]) -> List[Tuple[_DictKeyT, _DictValueT]]:
    return sorted(dct.items(), key=operator.itemgetter(0))
