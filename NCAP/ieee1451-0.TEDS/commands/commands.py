from message import MessageStructure

class QueryTEDS(MessageStructure):

    def __init__(self, vect):
        super().__init__(vect)

class SegmentTEDS(MessageStructure):

    def __init__(self, vect):
        super().__init__(vect)


class XdcrOperate(MessageStructure):
    
    '''
       Implements Status Transducer Operator
       
    '''
    def __init__(self, vect):
        super().__init__(vect)
        
        self.verify_message(vect)
    
   def  verify_message(self):
       
       '''
       Precisamos verificar se o conteudo da formado na messagem esta 
       cozidenente com padrao IEEE 1451
       como por exemp se o tamanho de messagem possuem o memso tamanho do
       corpo da messagem 
       '''

       _length = self.length()
       msg = self.commandDependent()
       
       if not _length == len(msg):
           raise Exception("Error Xdcr Message length dependent comand")
       
       
