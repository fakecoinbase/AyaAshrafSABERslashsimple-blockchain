class PrePrepareMessage:
    def __init__(self, block):
        self.block = block


class PrepareMessage:
    def __init__(self, block):
        self.block = block


class CommitMessage:
    def __init__(self, commit=True):
        self.commit = commit
