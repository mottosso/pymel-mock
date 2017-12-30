"""pymel mock

This accelerates Maya start-up time by 10+ seconds

"""

import sys
import types

core = types.ModuleType("core")

sys.modules["pymel.core"] = core
