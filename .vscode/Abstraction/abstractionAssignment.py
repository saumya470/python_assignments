# Create an abstract parent class or interface - TouchScreenLaptop with two abstract methods - scroll() and click(). This complete
# abstract class should be inherited or extended by HP and DELL which are also abstract classes which implement the scroll() method.
# Then create two more classes- HPNotebook and DELLNotebook which are the actual implementations of HP and DELL respectively and should
# implement the click methods(They can also override the scroll methods). Create objects of HPNotebook and DELLNotebook to access the two methods

from abc import abstractmethod, ABC

class TouchScreenLaptop(ABC):
    
    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass

class HP(TouchScreenLaptop):

    def scroll(self):
        print('Scrolling the HP model')

class DELL(TouchScreenLaptop):

    def scroll(self):
        print('Scrolling the DELL laptop')

class HPNotebook(HP):

    def click(self):
        print('Clicking the HPNotebook model')

class DELLNotebook(DELL):

    def click(self):
        print('Clicking the DELL Notebook')

hpNotebook = HPNotebook()
hpNotebook.click()
hpNotebook.scroll()

dellNotebook = DELLNotebook()
dellNotebook.click()
dellNotebook.scroll()


