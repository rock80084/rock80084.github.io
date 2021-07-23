class outer:
    def __init__(self):
        self.inner=self.Inner()
        self._inner=self.Inner()
        self.innerinner = self.inner.InnerInner()     
        
    def show_classes(self):
        print("classes")
        print(inner)
        print(_inner)
    class Inner:
        def inner_display(self,msg):
            print("1")
            print(msg)
    class _Inner:
        def inner_display(self,msg):
            print("2")
            print(msg)
        class InnerInner:

            def inner_display(self, msg):
                print("This is multilevel InnerInner class")
                print(msg)

        def inner_display(self, msg):
            print("This is Inner class")
            print(msg)

            

pput=outer()
pput.Inner().inner_display("aaa")
pput._Inner().inner_display("bbb")
pput.show_classes()

