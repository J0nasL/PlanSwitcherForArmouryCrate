class Plan:
    _id = None
    _name = None
    _active = False
    _hidden = False

    def __init__(self, plan_id, plan_name, active, hidden=False):
        self._id = plan_id
        self._name = plan_name
        self._active = active
        self._hidden = hidden

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def is_active(self):
        return self._active

    def is_hidden(self):
        return self._hidden

    def set_is_active(self, is_active):
        self._active = is_active