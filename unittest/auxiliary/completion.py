import cmd

class FTWCore(cmd.Cmd):
    
    ftwmods = [ 'httpanalyzer', 'dnsmisconfig', 'metaextra', 'cms' ]
    
    def do_run(self, runopt):
        if runopt and runopt in self.ftwmods:
            modrun = '%s!' % runopt
        elif runopt:
            modrun = "mod to run, " + runopt
        else:
            modrun = 'mod to run'
        print modrun
    
    def complete_run(self, text, line, begidx, endidx):
        if not text:
            completions = self.ftwmods[:]
        else:
            completions = [ f
                            for f in self.ftwmods
                            if f.startswith(text)
                            ]
        return completions
    
    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    FTWCore().cmdloop()