class Plan:
    _id = None
    _name = None

    def __init__(self, plan_id, plan_name):
        self._id = plan_id
        self._name = plan_name

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name
