class ARepository:
    def __init__(self, session_factory):
        self._session = session_factory
