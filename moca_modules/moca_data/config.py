# If __PROCESS_NAME__ is not null, moca_modules will set the value of __PROCESS_NAME__ as the process name.

__PROCESS_NAME__ = None

# debug mode. None or True or False

__DEBUG_MODE__ = None

# if the following flag is False, the module will be not loaded by init.py.

__LOAD_CACHE__ = True
__LOAD_CONFIG__ = True
__LOAD_COUNTER__ = True
__LOAD_DEV__ = True
__LOAD_ENCRYPT__ = True
__LOAD_FILE__ = True
__LOAD_LOG__ = True
__LOAD_MAIL__ = True
__LOAD_MEMORY__ = True
__LOAD_MYSQL__ = True
__LOAD_PYTHON__ = True
__LOAD_REDIS__ = True
__LOAD_SCHEDULE__ = True
__LOAD_SHARE__ = True
__LOAD_SHORTCUTS__ = True
__LOAD_UTILS__ = True
__LOAD_WORD_FILTER__ = True
__LOAD_EL_PARSER__ = True
__LOAD_CONSOLE__ = True
__LOAD_SMS__ = True
__LOAD_LEVELDB__ = True
__LOAD_SANIC__ = True
__LOAD_MMAPQ__ = True
__LOAD_TWITTER__ = True
__LOAD_MOCA_BOT__ = True

# this dictionary will be loaded by moca_modules.core
# Usage
# -----
# >>> import moca_modules as mzk
# >>> print(mzk.CONFIG['sample'])
# >>> This dictionary can access from moca_modules.

CONFIG = {
    'sample': 'This dictionary can access from moca_modules.'
}
