"""
LolMatchmakingMatchmakingReadyCheckResource{
declinerIds	[...]
dodgeWarning	LolMatchmakingMatchmakingDodgeWarningstring
Enum:
Array [ 3 ]
playerResponse	LolMatchmakingMatchmakingReadyCheckResponsestring
Enum:
Array [ 3 ]
state	LolMatchmakingMatchmakingReadyCheckStatestring
Enum:
Array [ 6 ]
suppressUx	boolean
timer	number($float)
}
"""
from dataclasses import dataclass
from enum import Enum
from typing import List


class LolMatchmakingMatchmakingDodgeWarning(Enum):
    NONE = 'None'
    WARNING = 'Warning'
    PENALTY = 'Penalty'


class LolMatchmakingMatchmakingReadyCheckResponse(Enum):
    NONE = 'None'
    ACCEPTED = 'Accepted'
    DECLINED = 'Declined'


class LolMatchmakingMatchmakingReadyCheckState(Enum):
    INVALID = 'Invalid'
    IN_PROGRESS = 'InProgress'
    EVERYONE_READY = 'EveryoneReady'
    STRANGER_NOT_READY = 'StrangerNotReady'
    PARTNER_NOT_READY = 'PartyNotReady'
    ERROR = 'Error'


@dataclass
class LolMatchmakingMatchmakingReadyCheckResource:
    declinerIds: List[int]
    dodgeWarning: LolMatchmakingMatchmakingDodgeWarning
    playerResponse: LolMatchmakingMatchmakingReadyCheckResponse
    state: LolMatchmakingMatchmakingReadyCheckState
    suppressUx: bool
    timer: float
    # dodgeWarning2: Union[Literal['None'], Literal['Warning'], Literal['Penalty']]
