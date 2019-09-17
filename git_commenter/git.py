from subprocess import Popen


class GitError(Exception):
    pass


class GitClient:
    def run(self, cmd, *args):
        if isinstance(args[0], tuple):
            command = ("git", cmd) + tuple([arg for arg in args[0]])
        else:
            command = ("git", cmd) + args

        proc = Popen(command, stdin=-1, stdout=-1, stderr=-1)
        out, err = proc.communicate()

        if not err:
            return out.strip()
        else:
            raise GitError(err.strip())

    def add(self, path):
        self.run("add", path)

    def commit(self, commit_msg):
        self.run("commit", "-m", commit_msg)
