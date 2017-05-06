from enum import Enum, unique

@unique
class FlowType(Enum):
	Request = 0
	Response = 1