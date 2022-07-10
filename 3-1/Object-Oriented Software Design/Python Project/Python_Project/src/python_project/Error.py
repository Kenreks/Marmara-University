class Error:
    def __init__(self, actor, course, reason):
        self.actor = actor
        self.course = course
        self.reason = reason

    def raise_error(self):
        return self.actor + " did not approve " + self.course.course_id + " because of " + self.reason + " error."
