import cmd

class HelloWorld(cmd.Cmd):
    """simple commandline interpreator clss"""

    def do_greet(self, person):
        """greet [person]
        Greet the named person"""

        if person:
            print("hi", person)
        else:
            print("hi")

    def do_EOF(self, line):
        return True

    def postloop(self):
        print()

if '__name__' == '__main__':
    HelloWorld().cmdloop()
