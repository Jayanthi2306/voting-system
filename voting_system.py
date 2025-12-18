from voter import Voter
from candidate import Candidate

class VotingSystem:
    def __init__(self):
        self.voters = {}      # voter_id -> Voter
        self.candidates = {}  # candidate_id -> Candidate

    def register_voter(self, voter_id, name):
        if voter_id in self.voters:
            return False
        self.voters[voter_id] = Voter(voter_id, name)
        return True

    def add_candidate(self, candidate_id, name):
        if candidate_id in self.candidates:
            return False
        self.candidates[candidate_id] = Candidate(candidate_id, name)
        return True

    def cast_vote(self, voter_id, candidate_id):
        if voter_id not in self.voters or candidate_id not in self.candidates:
            return False

        voter = self.voters[voter_id]
        if voter.has_voted:
            return False

        self.candidates[candidate_id].add_vote()
        voter.has_voted = True
        return True

    def get_results(self):
        return sorted(
            [(c.name, c.votes) for c in self.candidates.values()],
            key=lambda x: x[1],
            reverse=True
        )
