
import re

class State:
    Stream = 0
    DetectContentType = 1
    

class Tokenizer:
    
    # ---
    def __init__(self):
        self.state = State.DetectContentType
        
        self.buffer = ''
        self.token = ''
        
        self.type = ''
        
        self.content_types = {
            'H3': '###',
            'H2': '##',
            'H1': '#',
            'Task': '- [ ]',
            'Divider': '---'
        }     

    # ---
    def token_update(self, token):
        self.buffer += token
        
        self.token = re.sub(r'[-#*\[\]]', '', token)
        self.token = re.sub(r'\s+', ' ', self.token)
    
    # ---
    def state_update(self, state):
        self.state = state
        
    # ---
    def type_update(self, type):        
        self.type = type
        self.buffer_erase_up_to(self.content_types[type] if type != 'Paragraph' else '')
        self.state_update(State.Stream)
        print(f'\n{type}: ', end="")
    
    # ---
    def buffer_erase_up_to(self, substring):
        occurrence = self.buffer.find(substring)
        self.buffer = self.buffer[occurrence + 2:].lstrip()
        
    def buffer_contains_alphabetic(self):
        return bool(re.search(r'[a-zA-Z]', self.buffer))
        
    def buffer_starts_alphabetic(self):
        return len(self.buffer) > 0 and self.buffer.lstrip()[0].isalpha()
        
    def buffer_starts_content_type(self):
        return self.buffer.lstrip().startswith('-') or self.buffer.lstrip().startswith('#')
    
    # ---
    def new_line_detector(self):
        if '\n' in self.buffer:
            self.state_update(State.DetectContentType)
            self.buffer_erase_up_to('\n')
    
    # ---
    def new_content_detector(self):
        
        if self.state == State.DetectContentType:
            
            if self.buffer_starts_alphabetic():
                self.type_update('Paragraph')
            
            elif self.buffer_starts_content_type():  
                    
                for type, pattern in self.content_types.items():
                    if pattern in self.buffer:
                        self.type_update(type)
                        break
    
    # ---
    def detect(self, token):
        
        self.token_update(token)
        
        self.new_content_detector()
        self.new_line_detector()
        
        if self.state == State.Stream:
            print(self.token, end="")

