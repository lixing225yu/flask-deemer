from blinker import Namespace

pharos_signals = Namespace()

initialized = pharos_signals.signal("deemer-initialized")

blueprint_loaded = pharos_signals.signal("deemer-blueprint-loaded")
