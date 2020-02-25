from message import MessageStructure

class QueryTEDS(MessageStructure):

    def __init__(self, vect):
        super().__init__(vect)
       
    

class SegmentTEDS(MessageStructure):

    def __init__(self, vect):
        super().__init__(vect)
    
    
class XdcrOperate(MessageStructure):
    
    '''
    Implements Status Transducer Operator State Table 15 - 
    Standard command classe
    
    Esta classe deve ser executaca apenas quando o TransdutorChannel estiver
    em Estado de Operação

    Operate State table 31

    o TIM deve esta em modo de operação quando este comando estiver 
    em estado de ativação, se o msm não estive deve-se retorna uma mesg de 
    retorno informando o fato 
    Veja Table 5.13
       
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
       channel = self.destination()
       command = self.commdClass()
       function =  self.commandFunction()
       length = self.length()
       msg = self.commandDependent()
       
       if not length == len(msg):
           raise Exception("Error Xdcr Message length dependent comand")
       
       if not command  == '03':
           raise Exception 
       
       operating_state = {
           '01' : ''
           '02' :
           '03' :
           '04' :
           }
       
       if not function in states:
           raise Exception 
       
       
