class Candidate:
    def __init__(self, candidate_id, name):
        self.candidate_id = candidate_id
        self.name = name
        self.votes = 0

    def add_vote(self):
        self.votes += 1
