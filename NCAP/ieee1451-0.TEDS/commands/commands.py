from message import MessageStructure
from utils import hex2dec

class CommonCmd(MessageStructure):

    def __init__(self, vect):
        super().__init__(vect)
        
        #Status code for CommonCMD
        self.statusCode = '01'

        self.codeStates = {
            
            '01' : 'QueryTEDS', 
            '02' : 'ReadTEDS',
            '03' : 'WriteTEDS',
            '04' : 'UpdateTEDS',
            '05' : 'Run Self-test',
            '06' : 'Write service',
            '07' : 'Read service',
            '08' : 'Read status-event',
            '09' : 'Read status-condition',
            '0A' : 'Clear status-event- protocol',
            '0B' : 'Write status',
            '0C' : 'Read status-event',
        }
        
        self.verify_message()
        
    def  verify_message(self):
       
       '''
       Precisamos verificar se o conteudo da formado na messagem esta 
       cozidenente com padrao IEEE 1451
       como por exemp se o tamanho de messagem possuem o memso tamanho do
       corpo da messagem 
       '''
       channel = self.destination()
       command = self.commandClass()
       function =  self.commandFunction()
       length = self.length()
       msg = self.commandDependent()
       
       length = hex2dec(length)

       if not length == len(msg):
           raise Exception("Error Xdcr Message length dependent comand")
       
       if not command  == self.statusCode:
           raise Exception(f"Error Xdcr status code Command is not equal $(self.statusCode) ") 
        
       if not function in self.codeStates.keys():
           raise Exception('Error Status Commands Functions in XdcrOperate')
 
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
        
        #Status Code 03 XdcrOperate 
        self.statusCode = '03'
        self.verify_message()
    
    def  verify_message(self):
       
       '''
       Precisamos verificar se o conteudo da formado na messagem esta 
       cozidenente com padrao IEEE 1451
       como por exemp se o tamanho de messagem possuem o memso tamanho do
       corpo da messagem 

       Require Destination TransducerChannel 
       '''
       channel = self.destination()
       command = self.commandClass()
       function =  self.commandFunction()
       length = self.length()
       msg = self.commandDependent()
       
       length = hex2dec(length)

       if not channel > 0: 
           raise Exception("Error XdcrOperate Channel is not greater 0")
       
       if not length == len(msg):
           raise Exception("Error XdcrOperate Message length dependent comand")
       
       if not command  == self.statusCode:
           raise Exception 
       functions  = ['01', '02' , '03']
       if not function in functions:
           raise Exception ('Error Status Commands Functions in XdcrOperate')
       
"""
class XdcrIdle(MessageStructure):

    def __init__(self, vect):
        super().__init__(vect)
        
        #Status code for CommonCMD
        self.statusCode = '02'

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
       
       if not command  == self.statusCode:
           raise Exception 
       
       operating_state = {
           '01' : ''
           '02' :
           '03' :
           '04' :
           }
       
       if not function in states:
           raise Exception 
       
"""
